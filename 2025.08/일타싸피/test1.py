import math  # 수학 연산(루트, 삼각함수, atan2 등)을 위해 math 모듈 사용

# =========================
# [공통] Stage 1~4 전 구간에서 공통 사용되는 상수/포켓 좌표
# =========================
TABLE_W, TABLE_H = 254.0, 127.0  # 테이블(가로, 세로) 크기(cm), 문제 가이드의 기본값
BALL_DIAM = 5.73  # 공 지름(= 2r). 고스트볼 계산 등에서 '지름' 단위로 쓰입니다.
BALL_R = BALL_DIAM / 2.0  # 공 반지름 r. 충돌 허용치 계산 등에 사용

# [공통] 포켓 위치(“절반 걸쳐도 포켓” 가이드 반영하여 약간 안쪽으로 보정)
_k = BALL_R * 0.30  # 포켓 좌표를 테이블 모서리에서 살짝 안쪽으로 당기는 보정값
POCKETS = [
    (0.0 + _k, 0.0 + _k),  # 좌하 포켓(왼쪽 아래)
    (TABLE_W / 2.0, 0.0 + _k / 2.0),  # 중하 포켓(가운데 아래)
    (TABLE_W - _k, 0.0 + _k),  # 우하 포켓(오른쪽 아래)
    (0.0 + _k, TABLE_H - _k),  # 좌상 포켓(왼쪽 위)
    (TABLE_W / 2.0, TABLE_H - _k / 2.0),  # 중상 포켓(가운데 위)
    (TABLE_W - _k, TABLE_H - _k),  # 우상 포켓(오른쪽 위)
]


# =========================
# [공통] 벡터/기하 유틸리티 (Stage 1~4 공통)
# =========================
def sub(a, b):
    """벡터 뺄셈: a - b (좌표 a에서 좌표 b를 뺀 결과)"""
    return a[0] - b[0], a[1] - b[1]


def add(a, b):
    """벡터 덧셈: a + b"""
    return a[0] + b[0], a[1] + b[1]


def norm(v):
    """벡터의 길이(노름): √(x^2 + y^2)"""
    return math.hypot(v[0], v[1])


def unit(v):
    """단위벡터: v / |v|. 길이를 1로 만든 방향 벡터(0벡터면 (0,0) 반환)"""
    n = norm(v)
    return (0.0, 0.0) if n == 0.0 else (v[0] / n, v[1] / n)


def dot(a, b):
    """내적: a·b = ax*bx + ay*by (방향 정렬 정도 측정에 사용)"""
    return a[0] * b[0] + a[1] * b[1]


def cross_z(a, b):
    """2D 벡터 외적의 z성분: ax*by - ay*bx (선분-점 최단거리 계산에 사용)"""
    return a[0] * b[1] - a[1] * b[0]


# =========================
# [공통] 각도 변환 (수학 → 게임 좌표계)
#        Stage 1~4 모두에서 샷 각도 산출에 사용
# =========================
def angle_to_game_deg(src, dst):
    """
    수학 좌표계 각도(→=0°, 반시계+)를 게임 각도(↑=0°, 시계+)로 변환합니다.
    1) atan2(dy, dx)로 수학 각도를 구합니다.
    2) (90 - deg) % 360으로 게임 좌표계 각도로 맞춥니다.
    """
    dx, dy = dst[0] - src[0], dst[1] - src[1]  # 목적 방향 벡터 = 목적점 - 시작점
    theta = math.atan2(dy, dx)  # 수학 좌표계 라디안 각도(-π ~ π)
    return (90.0 - math.degrees(theta)) % 360.0  # 게임 좌표계 도(degree) 각도


# =========================
# [공통] 라인 충돌 판정(선분 A→B에 다른 공이 걸치면 False)
#        Stage 1/2: “직선 2-세그먼트 포켓” 성립 여부 판단 핵심
#        Stage 3/4: 매 턴 동일 판단으로 반복 적용
# =========================
def line_clear(A, B, balls, ignore, clearance_coeff=2.0):
    """
    선분 A→B 경로에 다른 공이 '걸치면' False(막힘), 아니면 True(깨끗).
    - balls: 전체 공 좌표 리스트. 포켓된 공은 [-1, -1]로 들어옵니다.
    - ignore: 충돌 판정에서 제외할 인덱스 집합(예: 큐볼, 목표 공 등)
    - clearance_coeff: 허용치 배율(기본 2.0 * r = 지름 정도)
    핵심 아이디어:
      * 점 P(다른 공의 중심)에서 선분 A→B로 내린 수선의 길이가 임계치 이하이고,
        수선의 발이 선분 범위 안(0 ≤ t ≤ |AB|)에 있으면 '충돌'로 간주합니다.
    """
    ax, ay = A
    bx, by = B  # A, B 좌표 분해
    abx, aby = bx - ax, by - ay  # 벡터 AB
    L = math.hypot(abx, aby)  # 선분 길이 |AB|
    if L == 0.0:  # 시작=끝이면 경로가 없으므로 실패 처리
        return False
    ux, uy = abx / L, aby / L  # 단위 방향 벡터 û = AB / |AB|
    thr = clearance_coeff * BALL_R  # 임계 최단거리 = (계수)*r (기본 2r)

    for i, p in enumerate(balls):  # 테이블 위의 모든 공에 대해 검사
        if i in ignore:
            continue  # 무시 대상(큐볼/타겟)은 스킵
        x, y = p
        if x < 0 or y < 0:
            continue  # 포켓된 공은 스킵
        apx, apy = x - ax, y - ay  # 벡터 AP (A→P)
        t = apx * ux + apy * uy  # AP를 û에 투영한 길이 t
        if 0.0 <= t <= L:  # 투영점이 선분 내부에 있을 때만 충돌 후보
            perp = abs(apx * uy - apy * ux)  # 최단거리 = |AP × û|
            if perp <= thr:  # 최단거리가 임계치 이하라면 '걸친다'
                return False  # → 경로 막힘
    return True  # 모든 공을 통과 → 경로 깨끗


# =========================
# [Stage 1/2 핵심] 고스트볼(맞춤점) 계산
#   - 목적구 T를 포켓 H로 보내려면 수구는 G(고스트점)에 와서 T를 '정면'으로 맞아야 합니다.
#   - G = T - (2r)*u (u: T→H 단위벡터, 2r=지름)
# [Stage 3/4] 동일 로직을 매 턴 반복 적용
# =========================
def ghost_point(T, H):
    """
    고스트점 G를 계산합니다.
    1) 목적구 T에서 포켓 H 방향의 단위벡터 u를 구합니다.
    2) 목적구 중심에서 지름(BALL_DIAM)만큼 반대 방향으로 이동한 점이 G입니다.
    """
    ux, uy = unit(sub(H, T))  # u = unit(H - T)
    return T[0] - BALL_DIAM * ux, T[1] - BALL_DIAM * uy  # G = T - D*u


# =========================
# [Stage 3/4 핵심] 내 목적구 집합 결정
#   - 선공: 1,3 / 후공: 2,4
#   - 둘 다 포켓되면 8번이 목적구로 자동 전환
#   - 매 턴 호출되어 남은 목적구를 동적으로 반영
# [Stage 1/2]에서도 동일하게 대상 목적구를 선정
# =========================
def my_targets(order, balls):
    """
    현재 플레이어의 '목표 공' 인덱스 목록을 반환합니다.
    - 선공(order=1): 1, 3이 남아 있으면 그것들이 목표. 둘 다 포켓되면 8번(인덱스 5).
    - 후공(order=2): 2, 4가 남아 있으면 그것들이 목표. 둘 다 포켓되면 8번.
    """
    mine = [1, 3] if order == 1 else [2, 4]  # 내 세트(선공:1,3 / 후공:2,4)
    # 아직 포켓되지 않은 내 목적구만 추리기
    alive = [i for i in mine if not (balls[i][0] < 0 or balls[i][1] < 0)]
    # 둘 다 포켓되었다면 8번 공(인덱스 5)이 남아 있다면 그것이 목표
    if not alive and not (balls[5][0] < 0 or balls[5][1] < 0):
        return [5]  # 8번만 타겟
    return alive  # 아직 남은 내 목적구들


# =========================
# [공통] 파워 스케일 (거리 기반 간이 모델)
#   - Stage 1~4 전 구간에서 동일 사용
# =========================
def power_from_paths(c2g, t2h):
    """
    간단한 거리 기반 파워 모델:
      power = 18 + 0.40*|C→G| + 0.20*|T→H| (이후 10~100으로 클램프)
    - C→G가 멀수록, T→H가 멀수록 파워를 더 줍니다.
    - 실전 환경에 따라 base/k1/k2는 미세 조정 가능합니다.
    """
    base, k1, k2 = 18.0, 0.40, 0.20  # 기본값 및 민감도 계수
    p = base + k1 * norm(c2g) + k2 * norm(t2h)  # 거리 기반 파워 스케일
    if p < 10.0: p = 10.0  # 파워 하한(너무 약하면 실패)
    if p > 100.0: p = 100.0  # 파워 상한(게임 제한)
    return p


# =========================
# [공통] 한 턴 계산 시작 (Stage 1~4 모두 동일 흐름)
# =========================
cue = tuple(gameData.balls[0])  # 큐볼 좌표(인덱스 0). 예: (x0, y0)
balls = [tuple(p) for p in gameData.balls]  # 모든 공 좌표를 튜플로 복사 (0~5)

# [공통] 현재 턴의 내 목적구 후보(인덱스) 추출
targets = my_targets(gameData.order, balls)  # 내 목적구 인덱스 리스트 계산
candidates = []  # (선호도, 총거리, 각도, 파워) 후보 리스트

# -------------------------------------------------
# [Stage 1/2 핵심 로직] “직선 2-세그먼트 포켓” 탐색
#  - 목적구 T → 포켓 H 라인이 깨끗한가(line_clear)
#  - 고스트점 G 계산(ghost_point)
#  - 큐볼 C → G 라인이 깨끗한가(line_clear)
#  - 정렬 우선(align), 총거리 보조로 최적 후보 선정
# [Stage 3/4] 동일 로직을 ‘매 턴’ 반복 적용(그리디)
# -------------------------------------------------
for t_idx in targets:  # 내 목적구(또는 8번) 각각에 대해
    T = balls[t_idx]  # 해당 목적구 좌표
    if T[0] < 0 or T[1] < 0:  # 이미 포켓된 목적구는 스킵
        continue
    for H in POCKETS:  # 6개 포켓을 모두 시도(우회 전략)
        # [1] 목적구 T → 포켓 H 직선 경로 확보(막히면 다음 포켓)
        if not line_clear(T, H, balls, ignore={0, t_idx}):
            continue

        # [2] 고스트점 G 계산(T와 H로부터 G = T - D * unit(T→H))
        G = ghost_point(T, H)

        # [3] 큐볼 C → G 직선 경로 확보(막히면 다음 포켓)
        if not line_clear(cue, G, balls, ignore={0, t_idx}):
            continue

        # [4] 정렬(align) 우선, 총거리(total_len) 보조 기준으로 후보 평가
        u1 = unit(sub(G, cue))  # 큐볼 이동 방향(C→G)
        u2 = unit(sub(H, T))  # 목적구 이동 방향(T→H)
        align = dot(u1, u2)  # 정렬 정도(-1~1). 클수록 정면 히트.
        if align <= 0.0:  # 0 이하(역방향/직각)에 가까우면 배제
            continue
        total_len = norm(sub(G, cue)) + norm(sub(H, T))  # 총 이동 길이(짧을수록 유리)

        ang = angle_to_game_deg(cue, G)  # 게임 좌표계 샷 각도 계산
        pwr = power_from_paths(sub(G, cue), sub(H, T))  # 거리 기반 파워 계산
        candidates.append((-align, total_len, ang, pwr))  # 정렬 큰게 좋으니 -align로 정렬

# [Stage 1/2] 최적 샷 선택 (정렬 큰 것 → 거리 짧은 것)
# [Stage 3/4] 매 턴 동일 기준으로 1개씩 처리(그리디하게 두 공을 순차 포켓)
if candidates:  # 후보가 하나라도 있으면
    candidates.sort(key=lambda x: (x[0], x[1]))  # ( -정렬, 총거리 ) 오름차순 정렬
    angle, power = candidates[0][2], candidates[0][3]  # 최적 후보의 각도/파워 선택
else:
    # -------------------------------------------------
    # [모든 Stage 공통 안전장치]
    #  - 후보가 전혀 없을 때 파울 방지: 가장 가까운 내 목적구를 ‘맞히기만’ 시도
    #  - Stage 1/2/3/4 전부에서 동일하게 동작(파울 카운트 방지)
    # -------------------------------------------------
    fallback = []  # (거리, 인덱스, 좌표) 후보
    for t_idx in targets:  # 타겟 각각에 대해
        T = balls[t_idx]  # 좌표 조회
        if T[0] < 0 or T[1] < 0:  # 포켓된 경우 스킵
            continue
        d = norm(sub(T, cue))  # 큐볼-목적구 거리
        fallback.append((d, t_idx, T))  # 거리 기준으로 제일 가까운 것 선택 예정

    if fallback:  # 맞힐 목적구가 하나라도 있으면
        fallback.sort(key=lambda x: x[0])  # 거리 오름차순 정렬
        _, t_idx, T = fallback[0]  # 가장 가까운 목적구 선택
        # 직선이 막히면 살짝 오프셋(미세 편향)으로 맞히기 시도(라인 살짝 피하기)
        if not line_clear(cue, T, balls, ignore={0, t_idx}):
            eps = 0.001 * BALL_DIAM  # 지름의 0.1% 정도 미세 오프셋
            T = (T[0] + eps, T[1] + eps)
        angle, power = angle_to_game_deg(cue, T), 45.0  # 단순 맞히기: 중간 파워
    else:
        # 정말 칠 공이 없다면(모든 타겟 포켓 등) 무해한 약한 샷으로 마무리
        angle, power = 0.0, 10.0

# [공통] 샷 전송 (Stage 1~4 모두 동일) — 채점 서버가 conn.send를 제공합니다.
conn.send(angle, power)

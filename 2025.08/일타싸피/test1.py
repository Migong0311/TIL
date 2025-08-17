import math

# =========================
# [공통] Stage 1~4 전 구간에서 공통 사용되는 상수/포켓 좌표
# =========================
TABLE_W, TABLE_H = 254.0, 127.0
BALL_DIAM = 5.73  # 공 지름(= 2r)
BALL_R = BALL_DIAM / 2.0

# [공통] 포켓 위치(“절반 걸쳐도 포켓” 가이드 반영하여 약간 안쪽으로 보정)
_k = BALL_R * 0.30
POCKETS = [
    (0.0 + _k, 0.0 + _k),  # 좌하
    (TABLE_W / 2.0, 0.0 + _k / 2.0),  # 중하
    (TABLE_W - _k, 0.0 + _k),  # 우하
    (0.0 + _k, TABLE_H - _k),  # 좌상
    (TABLE_W / 2.0, TABLE_H - _k / 2.0),  # 중상
    (TABLE_W - _k, TABLE_H - _k),  # 우상
]


# =========================
# [공통] 벡터/기하 유틸리티 (Stage 1~4 공통)
# =========================
def sub(a, b): return (a[0] - b[0], a[1] - b[1])


def add(a, b): return (a[0] + b[0], a[1] + b[1])


def norm(v): return math.hypot(v[0], v[1])


def unit(v):
    n = norm(v)
    return (0.0, 0.0) if n == 0.0 else (v[0] / n, v[1] / n)


def dot(a, b): return a[0] * b[0] + a[1] * b[1]


def cross_z(a, b): return a[0] * b[1] - a[1] * b[0]


# =========================
# [공통] 각도 변환 (수학 → 게임 좌표계)
#        Stage 1~4 모두에서 샷 각도 산출에 사용
# =========================
def angle_to_game_deg(src, dst):
    dx, dy = dst[0] - src[0], dst[1] - src[1]
    theta = math.atan2(dy, dx)  # 수학: 오른쪽 0°, 반시계+
    return (90.0 - math.degrees(theta)) % 360.0  # 게임: 위 0°, 시계+


# =========================
# [공통] 라인 충돌 판정(선분 A→B에 다른 공이 걸치면 False)
#        Stage 1/2: “직선 2-세그먼트 포켓” 성립 여부 판단 핵심
#        Stage 3/4: 매 턴 동일 판단으로 반복 적용
# =========================
def line_clear(A, B, balls, ignore, clearance_coeff=2.0):
    ax, ay = A;
    bx, by = B
    abx, aby = bx - ax, by - ay
    L = math.hypot(abx, aby)
    if L == 0.0: return False
    ux, uy = abx / L, aby / L  # 단위 방향 벡터
    thr = clearance_coeff * BALL_R  # 허용 오차(기본 2.0r)

    for i, p in enumerate(balls):
        if i in ignore:
            continue
        x, y = p
        if x < 0 or y < 0:
            continue  # 포켓된 공은 무시
        apx, apy = x - ax, y - ay
        t = apx * ux + apy * uy  # 투영 길이
        if 0.0 <= t <= L:  # 선분 내부 투영일 때만 고려
            perp = abs(apx * uy - apy * ux)  # 최단거리 = |AP x u|
            if perp <= thr:
                return False  # 충돌
    return True


# =========================
# [Stage 1/2 핵심] 고스트볼(맞춤점) 계산
#   - 목적구 T를 포켓 H로 보내려면 수구는 G(고스트점)에 와서 T를 정면으로 맞아야 합니다.
#   - G = T - (2r)*u (u: T→H 단위벡터, 2r=지름)
# [Stage 3/4] 동일 로직을 매 턴 반복 적용
# =========================
def ghost_point(T, H):
    ux, uy = unit(sub(H, T))
    return T[0] - BALL_DIAM * ux, T[1] - BALL_DIAM * uy


# =========================
# [Stage 3/4 핵심] 내 목적구 집합 결정
#   - 선공: 1,3 / 후공: 2,4
#   - 둘 다 포켓되면 8번이 목적구로 자동 전환
#   - 매 턴 호출되어 남은 목적구를 동적으로 반영
# [Stage 1/2]에서도 동일하게 대상 목적구를 선정
# =========================
def my_targets(order, balls):
    mine = [1, 3] if order == 1 else [2, 4]
    alive = [i for i in mine if not (balls[i][0] < 0 or balls[i][1] < 0)]
    if not alive and not (balls[5][0] < 0 or balls[5][1] < 0):
        return [5]  # 8번
    return alive


# =========================
# [공통] 파워 스케일 (거리 기반 간이 모델)
#   - Stage 1~4 전 구간에서 동일 사용
# =========================
def power_from_paths(c2g, t2h):
    base, k1, k2 = 18.0, 0.40, 0.20
    p = base + k1 * norm(c2g) + k2 * norm(t2h)
    if p < 10.0: p = 10.0
    if p > 100.0: p = 100.0
    return p


# =========================
# [공통] 한 턴 계산 시작 (Stage 1~4 모두 동일 흐름)
# =========================
cue = tuple(gameData.balls[0])
balls = [tuple(p) for p in gameData.balls]  # 0:cue, 1~4:목적구, 5:8번

# [공통] 현재 턴의 내 목적구 후보(인덱스) 추출
targets = my_targets(gameData.order, balls)
candidates = []

# -------------------------------------------------
# [Stage 1/2 핵심 로직] “직선 2-세그먼트 포켓” 탐색
#  - 목적구 T → 포켓 H 라인이 깨끗한가(line_clear)
#  - 고스트점 G 계산(ghost_point)
#  - 큐볼 C → G 라인이 깨끗한가(line_clear)
#  - 정렬 우선(align), 총거리 보조로 최적 후보 선정
# [Stage 3/4] 동일 로직을 ‘매 턴’ 반복 적용(그리디)
# -------------------------------------------------
for t_idx in targets:
    T = balls[t_idx]
    if T[0] < 0 or T[1] < 0:
        continue
    for H in POCKETS:
        # [Stage 1/2] 목적구 T → 포켓 H 직선 경로 확보
        if not line_clear(T, H, balls, ignore={0, t_idx}):
            continue

        # [Stage 1/2] 고스트점 G 계산
        G = ghost_point(T, H)

        # [Stage 1/2] 큐볼 C → G 직선 경로 확보
        if not line_clear(cue, G, balls, ignore={0, t_idx}):
            continue

        # [Stage 1/2] 정렬(align) 우선, 총거리 보조
        u1 = unit(sub(G, cue))  # C→G
        u2 = unit(sub(H, T))  # T→H
        align = dot(u1, u2)  # 클수록 정면 히트(얇은 컷 배제)
        if align <= 0.0:
            continue
        total_len = norm(sub(G, cue)) + norm(sub(H, T))

        ang = angle_to_game_deg(cue, G)
        pwr = power_from_paths(sub(G, cue), sub(H, T))
        candidates.append((-align, total_len, ang, pwr))

# [Stage 1/2] 최적 샷 선택 (정렬 큰 것 → 거리 짧은 것)
# [Stage 3/4] 매 턴 동일 기준으로 1개씩 처리(그리디하게 두 공을 순차 포켓)
if candidates:
    candidates.sort(key=lambda x: (x[0], x[1]))
    angle, power = candidates[0][2], candidates[0][3]
else:
    # -------------------------------------------------
    # [모든 Stage 공통 안전장치]
    #  - 후보가 전혀 없을 때 파울 방지: 가장 가까운 내 목적구를 ‘맞히기만’ 시도
    #  - Stage 1/2/3/4 전부에서 동일하게 동작(파울 카운트 방지)
    # -------------------------------------------------
    fallback = []
    for t_idx in targets:
        T = balls[t_idx]
        if T[0] < 0 or T[1] < 0:
            continue
        d = norm(sub(T, cue))
        fallback.append((d, t_idx, T))

    if fallback:
        fallback.sort(key=lambda x: x[0])
        _, t_idx, T = fallback[0]
        # 직선이 막히면 살짝 오프셋(미세 편향)으로 맞히기 시도
        if not line_clear(cue, T, balls, ignore={0, t_idx}):
            eps = 0.001 * BALL_DIAM
            T = (T[0] + eps, T[1] + eps)
        angle, power = angle_to_game_deg(cue, T), 45.0
    else:
        # 정말 칠 공이 없으면 무해한 약한 샷
        angle, power = 0.0, 10.0

# [공통] 샷 전송 (Stage 1~4 모두 동일)
conn.send(angle, power)

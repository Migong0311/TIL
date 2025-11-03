# 🧠 SQL 기본 문법 요약

## 1️⃣ SELECT – 데이터 조회

```sql
SELECT * FROM tracks;
```

* **기능:** 테이블의 모든 컬럼(열)을 조회합니다.
* `*`는 모든 열을 의미합니다.
* `FROM`은 데이터를 가져올 테이블을 지정합니다.

📌 예시

```sql
SELECT Name, Milliseconds, UnitPrice FROM tracks;
```

→ 특정 열만 선택적으로 조회

---

## 2️⃣ WHERE – 조건 지정

```sql
SELECT * FROM tracks WHERE GenreId = 1;
```

* **기능:** 특정 조건을 만족하는 행(Row)만 필터링합니다.
* 비교 연산자 (`=`, `>`, `<`, `>=`, `<=`, `!=`) 사용 가능

📌 예시

```sql
SELECT * FROM songs WHERE genre = 'Pop';
SELECT * FROM songs WHERE duration >= 180;
```

→ 장르가 Pop이거나, 재생시간이 3분 이상인 노래 조회

---

## 3️⃣ ORDER BY – 정렬

```sql
SELECT * FROM tracks ORDER BY Name;
```

* **기능:** 지정한 컬럼을 기준으로 결과를 정렬합니다.
* `ASC` (오름차순, 기본값) / `DESC` (내림차순)

📌 예시

```sql
SELECT * FROM songs ORDER BY title DESC;
```

→ 제목을 기준으로 내림차순 정렬

---

## 4️⃣ LIMIT – 출력 개수 제한

```sql
SELECT * FROM tracks LIMIT 10;
```

* **기능:** 조회된 데이터 중 상위 N개만 출력합니다.
* MySQL, SQLite, PostgreSQL 등에서 사용됩니다.

---

## 5️⃣ LIKE – 패턴(문자열) 검색

| 패턴  | 의미        | 예시                      |
| --- | --------- | ----------------------- |
| `%` | 0개 이상의 문자 | `'하%'` → ‘하’로 시작        |
| `_` | 임의의 한 글자  | `'__남%'` → 세 번째 글자가 ‘남’ |

📌 예시

```sql
-- first_name이 '하'로 시작
SELECT * FROM users WHERE first_name LIKE '하%';

-- phone이 '555'로 끝남
SELECT * FROM users WHERE phone LIKE '%555';

-- country가 '경상'으로 시작
SELECT * FROM users WHERE country LIKE '경상%';

-- country가 '경' 또는 '충'으로 시작하고 세 번째 글자가 '남'
SELECT * 
FROM users
WHERE (country LIKE '경%' OR country LIKE '충%')
AND country LIKE '__남%';
```

---

## 6️⃣ GROUP BY – 그룹화 및 집계

> **데이터를 특정 기준으로 묶어 집계(합계, 평균, 개수 등)를 구할 때 사용**

📌 기본 구조

```sql
SELECT 컬럼명, 집계함수(컬럼명)
FROM 테이블명
GROUP BY 컬럼명;
```

📌 예시

```sql
-- 장르별 트랙 개수 구하기
SELECT GenreId, COUNT(*) AS track_count
FROM tracks
GROUP BY GenreId;

-- 국가별 사용자 수 구하기
SELECT country, COUNT(*) AS user_count
FROM users
GROUP BY country;
```

🧩 주요 집계 함수

| 함수      | 설명      | 예시               |
| ------- | ------- | ---------------- |
| COUNT() | 행 개수 계산 | `COUNT(*)`       |
| SUM()   | 합계 계산   | `SUM(UnitPrice)` |
| AVG()   | 평균 계산   | `AVG(duration)`  |
| MAX()   | 최대값     | `MAX(duration)`  |
| MIN()   | 최소값     | `MIN(duration)`  |

---

## 🧾 오늘의 핵심 요약

| 항목           | 핵심 기능        | 예시                         |
| ------------ | ------------ | -------------------------- |
| **SELECT**   | 테이블에서 데이터 조회 | `SELECT * FROM tracks;`    |
| **WHERE**    | 조건에 맞는 행만 선택 | `WHERE GenreId = 1`        |
| **ORDER BY** | 정렬 기준 지정     | `ORDER BY Name ASC`        |
| **LIMIT**    | 출력 개수 제한     | `LIMIT 10`                 |
| **LIKE**     | 문자열 패턴 검색    | `LIKE '하%'`, `LIKE '__남%'` |
| **GROUP BY** | 그룹화 후 집계     | `GROUP BY country`         |


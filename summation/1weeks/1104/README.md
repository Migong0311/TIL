
# 1104 DDL & DML + JOIN + Subquery

---

## 🧱 DDL (Data Definition Language)

> 데이터의 **구조(Structure)** 를 정의·수정·삭제하는 명령어

---

### ✅ 1. CREATE TABLE — 테이블 생성

```sql
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 고유번호 자동 증가
    title VARCHAR(100) NOT NULL,           -- 제목
    content VARCHAR(200) NOT NULL,         -- 내용
    createdAt DATE NOT NULL                -- 작성일
);
```

**핵심 포인트**

* `AUTOINCREMENT` : 고유한 정수 ID 자동 증가
* `NOT NULL` : 필수 입력 값
* `VARCHAR(n)` : 가변 문자열
* `DATE` : 날짜 형식 데이터

---

### ✅ 2. ALTER TABLE — 테이블 수정

#### (1) 컬럼 추가

```sql
ALTER TABLE examples
ADD COLUMN Country VARCHAR(100) NOT NULL DEFAULT 'default value';
```

→ `NOT NULL` 제약이 있으면 `DEFAULT` 필수 지정

#### (2) 컬럼 삭제

```sql
ALTER TABLE examples
DROP COLUMN PostCode;
```

#### (3) 테이블 이름 변경

```sql
ALTER TABLE examples
RENAME TO new_examples;
```

---

### ✅ 3. DROP TABLE — 테이블 삭제

```sql
DROP TABLE new_examples;
```

* 테이블 구조 및 데이터 완전 삭제
* **자동 COMMIT**, 복구 불가능

---

### 📘 DDL 요약표

| 명령어        | 기능             | 주요 예시                                      |
| ---------- | -------------- | ------------------------------------------ |
| **CREATE** | 테이블 생성         | `CREATE TABLE users (...);`                |
| **ALTER**  | 컬럼 추가/삭제/이름 변경 | `ALTER TABLE examples ADD COLUMN age INT;` |
| **DROP**   | 테이블 삭제         | `DROP TABLE users;`                        |

---

## 🔧 DML (Data Manipulation Language)

> 테이블 내부의 **데이터를 조작(추가, 수정, 삭제)** 하는 명령어

---

### ✅ 1. INSERT — 데이터 추가

```sql
INSERT INTO 
    articles (title, content, createdAt)
VALUES 
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');
```

* 여러 행을 한 번에 추가 가능
* `NOT NULL` 컬럼은 반드시 값 지정

---

### ✅ 2. UPDATE — 데이터 수정

```sql
UPDATE users
SET name = '권미숙'
WHERE name = '하석주';
```

* 조건(`WHERE`)이 없으면 모든 행이 수정됨
* 외래키(FK) 참조 시 연동 테이블도 자동 반영됨

---

### ✅ 3. DELETE — 데이터 삭제

```sql
DELETE FROM articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAt
    LIMIT 2
);
```

* 조건을 만족하는 행만 삭제
* 위 예시는 **가장 오래된 2개의 게시글 삭제**

---

### 📘 DML 요약표

| 명령어        | 기능     | 주요 예시                                      |
| ---------- | ------ | ------------------------------------------ |
| **INSERT** | 데이터 추가 | `INSERT INTO users (name) VALUES ('홍길동');` |
| **UPDATE** | 데이터 수정 | `UPDATE users SET name='권미숙' WHERE id=1;`  |
| **DELETE** | 데이터 삭제 | `DELETE FROM articles WHERE id=3;`         |

---

## 🔗 JOIN (테이블 간 결합)

> 여러 테이블의 데이터를 **공통 컬럼(FK, PK)** 기준으로 결합하는 명령어

---

### ✅ 1. INNER JOIN — 두 테이블 모두에 존재하는 데이터만 결합

```sql
SELECT articles.title, users.name
FROM articles
INNER JOIN users
ON users.id = articles.userId
WHERE users.id = 1;
```

**설명**

* `INNER JOIN`은 **두 테이블에서 공통된 데이터만** 결합
* `ON` 뒤에 **조인 조건** 지정 (`articles.userId = users.id`)
* `WHERE`로 특정 조건 추가 가능

---

### ✅ 2. LEFT JOIN — 왼쪽 테이블 기준으로 모든 데이터 결합

```sql
SELECT users.name
FROM users
LEFT JOIN articles
ON articles.userId = users.id
WHERE articles.userId IS NULL;
```

**설명**

* 왼쪽(users) 테이블의 모든 데이터 표시
* 오른쪽(articles)에 일치하는 값이 없으면 **NULL** 표시
* 주로 **게시글이 없는 회원 찾기**, **누락 데이터 확인** 등에 사용

---

### 📘 JOIN 요약표

| 구분             | 설명                             | 결과           |
| -------------- | ------------------------------ | ------------ |
| **INNER JOIN** | 양쪽 모두 존재하는 데이터만 표시             | 교집합          |
| **LEFT JOIN**  | 왼쪽 테이블의 모든 데이터 + 오른쪽 일치 데이터 표시 | 왼쪽 기준 전체 표시  |
| **RIGHT JOIN** | 오른쪽 테이블 기준 (SQLite 미지원)        | 오른쪽 기준 전체 표시 |

---

## 🧩 Subquery (서브쿼리)

> 쿼리 안에서 또 다른 **SELECT 문**을 실행하는 구조
> 주로 `WHERE`, `FROM`, `HAVING` 절 안에서 사용됩니다.

---

### ✅ 1. WHERE 절에서 사용 (조건 지정)

```sql
DELETE FROM articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAt
    LIMIT 2
);
```

* 서브쿼리에서 `id`를 조회한 뒤,
  그 결과에 해당하는 데이터만 **삭제**

---

### ✅ 2. SELECT 절에서 사용 (계산값 함께 출력)

```sql
SELECT 
    name,
    (SELECT COUNT(*) FROM articles WHERE userId = users.id) AS post_count
FROM users;
```

* 각 사용자별로 **작성한 게시글 개수**를 함께 조회

---

### ✅ 3. FROM 절에서 사용 (임시 테이블처럼 활용)

```sql
SELECT avg_price.GenreId, avg_price.avg_unit
FROM (
    SELECT GenreId, AVG(UnitPrice) AS avg_unit
    FROM tracks
    GROUP BY GenreId
) AS avg_price
WHERE avg_price.avg_unit > 1.0;
```

* 서브쿼리를 하나의 **가상 테이블(alias)** 로 두고 조회

---

### 📘 Subquery 요약표

| 구분           | 위치           | 활용 목적         | 예시                                                |
| ------------ | ------------ | ------------- | ------------------------------------------------- |
| **단일행 서브쿼리** | WHERE        | 한 개의 값 비교     | `WHERE price > (SELECT AVG(price) FROM products)` |
| **다중행 서브쿼리** | WHERE ... IN | 여러 값 비교       | `WHERE id IN (SELECT id FROM articles)`           |
| **중첩 서브쿼리**  | SELECT, FROM | 계산값 또는 가상 테이블 | `FROM (SELECT ...) AS alias`                      |

---

## ⚖️ 종합 비교 요약

| 구분           | 주요 역할               | 대표 명령어                  | 핵심 특징                         |
| ------------ | ------------------- | ----------------------- | ----------------------------- |
| **DDL**      | 데이터 구조 정의           | CREATE, ALTER, DROP     | 테이블의 틀(형식) 정의, 자동 COMMIT      |
| **DML**      | 데이터 조작 (추가, 수정, 삭제) | INSERT, UPDATE, DELETE  | 실제 데이터 변경, COMMIT/ROLLBACK 가능 |
| **JOIN**     | 테이블 간 관계 결합         | INNER JOIN, LEFT JOIN   | 여러 테이블 연결 조회                  |
| **Subquery** | 쿼리 내부의 쿼리           | SELECT ... (SELECT ...) | 조건, 집계, 가상 테이블로 활용            |

---

### ✅ 한줄 요약

* **DDL** → “데이터의 뼈대를 만든다.”
* **DML** → “그 뼈대 안의 데이터를 다룬다.”
* **JOIN** → “테이블을 연결한다.”
* **Subquery** → “쿼리 안에서 또 다른 쿼리를 돌린다.”



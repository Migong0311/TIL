-- 01. Querying data
-- employees 테이블에서 LastName(성), FirstName(이름) 컬럼만 조회
SELECT LastName, FirstName FROM employees;

-- employees 테이블의 모든 컬럼(*)을 조회
SELECT * FROM employees;

-- employees 테이블에서 FirstName 컬럼을 '이름'이라는 별칭으로 조회
SELECT FirstName AS '이름' FROM employees;

-- tracks 테이블에서 곡명(Name)과 재생시간(Milliseconds)을 분 단위로 변환하여 조회
-- Milliseconds / 60000 → 밀리초를 분으로 환산
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;


-- 02. Sorting data (데이터 정렬)

-- employees 테이블에서 FirstName(이름) 컬럼만 조회하고, 이름을 오름차순으로 정렬
SELECT FirstName FROM employees ORDER BY FirstName;
-- employees 테이블에서 FirstName(이름) 컬럼만 조회하고, 이름을 내림차순으로 정렬
SELECT FirstName FROM employees ORDER BY FirstName DESC;

-- 테이블 customers에서 country 필드를 기준으로 내림차순으로 정렬한 다음
-- city 필드 기준으로 오름차순 조회
SELECT 
    Country,City
FROM
    customers
ORDER BY
    "Country" DESC, City;

-- 테이블 tracks에서 Milliseconds 필드를 기준으로 내림차순으로 정렬한 다음
-- Name,Milliseconds 필드의 모든 데이터를 조회

SELECT 
    Name, Milliseconds / 60000 AS '재생 시간(분)' 
FROM 
    tracks
ORDER BY
    Milliseconds DESC;

-- NULL 정렬 예시

-- 03. Filtering data

-- 04. Grouping data


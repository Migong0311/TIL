-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL
);


-- 1. Insert data into table
INSERT INTO articles(title,content,createdAt)
VALUES('test','test_content','2000-01-01');

INSERT INTO 
    articles (title, content, createdAt)
VALUES 
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');

INSERT INTO articles(title,content,createdAt)
VALUES('now','now_content',DATE());
select * from articles;
-- 2. Update data in table

UPDATE articles
SET title = 'double_update_title',content = 'update_content'
WHERE id=2;
-- 3. Delete data from table
DELETE FROM articles
WHERE id = 1;
-- 심화
DELETE FROM articles
WHERE id IN(
    SELECT id FROM articles
    ORDER BY "createdAt"
    LIMIT 2
);
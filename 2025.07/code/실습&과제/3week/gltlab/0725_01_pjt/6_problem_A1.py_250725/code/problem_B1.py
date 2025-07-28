import json
from pathlib import Path

# 1. 파일 경로 설정
file_path = Path('./data/books_500.json')

# 파일 존재 여부 확인
if file_path.exists():
    # 2. 파일 열기 및 JSON 데이터 읽기
    with file_path.open('r', encoding='utf-8') as books:
        data = json.load(books)  # JSON 데이터를 파이썬 객체로 변환

    non_children_books = []  # 어린이 도서가 아닌 책을 저장할 리스트

    # 3. 데이터 순회하며 '어린이'가 카테고리에 없는 책 필터링
    for book in data:
        # 'category' 키가 있는 경우에만 체크
        if 'categoryName' in book:
            if '어린이' not in book['categoryName']:
                non_children_books.append(book)

    # 4. 결과 출력
    print("어린이 도서가 아닌 책 목록:")
    for book in non_children_books:
        # 책 제목과 카테고리가 있다고 가정
        title = book.get('title', '제목 없음')
        category = book.get('categoryName', '카테고리 없음')
        print(f"제목: {title}, 카테고리: {category}")
else:
    print(f"파일이 존재하지 않습니다: {file_path}")

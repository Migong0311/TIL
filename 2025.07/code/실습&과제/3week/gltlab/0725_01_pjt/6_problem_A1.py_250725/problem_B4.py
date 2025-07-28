from datetime import datetime  # 날짜와 시간 처리를 위한 라이브러리
import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리

# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('./data/books_500.json')

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    with file_path.open('r', encoding='utf-8') as books:
        # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)
        data = json.load(books)
  # JSON 데이터를 파이썬 딕셔너리로 변환 (json.load 사용)
    # 3. 출판일을 기준으로 최신 도서 10개 추출 (hint: sorted 함수 key 속성)
    # pubDate가 있는 도서만 추출
    books_with_pubdate = [book for book in data if 'pubDate' in book and 'title' in book]
    # pubDate를 datetime으로 변환하여 정렬
    for book in books_with_pubdate:
        book['pubDate_dt'] = datetime.strptime(book['pubDate'], "%Y-%m-%d")
     
    # pubDate 기준 내림차순 정렬 후 10개 추출
    latest_books = sorted(books_with_pubdate, key=lambda x: x['pubDate_dt'], reverse=True)[:10]

    # 4. 결과 출력
    print("최신 도서 10개:")
    for book in latest_books:
        print(f"{book['title']} ({book['pubDate']})")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

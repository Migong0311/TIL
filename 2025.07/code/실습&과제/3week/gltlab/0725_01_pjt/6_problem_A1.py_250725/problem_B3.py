import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리
import pprint as p
# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('./data/books_500.json')

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    with file_path.open('r', encoding='utf-8') as books:
        # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)
        data = json.load(books)

    # 3. 카테고리별 통계 집계
category_stats = {}  # 카테고리별 통계를 저장할 딕셔너리
category_price_sum = {}
for book in data:
    if 'categoryName' in book:
        category = book['categoryName']
        price = book['priceSales']
    if category in category_stats:
        category_stats[category] += 1
        category_price_sum[category] += price
    else:
        category_stats[category] = 1  # 카테고리별 도서 수 초기화
        category_price_sum[category] = price  # 카테고리별로 도서 수와 가격을 집계하는 코드

    # 4. 결과 출력
print("카테고리별 도서 통계:")
for category, stats in category_stats.items():
    count = category_stats[category]
    total_price = category_price_sum[category]
    average_price = total_price // count
    p.pprint(f"{category}: {count}권, {average_price}원") # 각 카테고리별 통계 출력
    
else:
    print(f"파일이 존재하지 않습니다: {file_path}")

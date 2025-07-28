import json
from pathlib import Path
from datetime import datetime  # ✅ 누락된 datetime 모듈 추가

# 1. 파일 경로 설정
file_path = Path('./data/books_2000.json')

# 2. 파일 존재 여부 확인 및 처리
if file_path.exists():
    with file_path.open('r', encoding='utf-8') as books:
        data = json.load(books)

    # 3. 월별 도서 가격과 수를 저장할 딕셔너리
    monthly_data = {}

    valid_data_found = False
    for book in data:
        if 'priceSales' in book and 'pubDate' in book:
            valid_data_found = True
            try:
                # 가격과 날짜 파싱
                price = float(book['priceSales'])
                pub_date = datetime.strptime(book['pubDate'], '%Y-%m-%d')
                month = pub_date.month

                if month not in monthly_data:
                    monthly_data[month] = {
                        'total_price': 0,
                        'count': 0
                    }

                monthly_data[month]['total_price'] += price
                monthly_data[month]['count'] += 1

            except Exception as e:
                print(f"[오류] 도서 데이터 처리 중 문제 발생: {e}")

    # 4. 출력
    if not valid_data_found:
        print("[안내] price와 pubDate가 모두 있는 도서 데이터가 없습니다.")
    else:
        print("월별 평균 가격 및 도서 수:")
        for month in range(1, 13):  # 1월 ~ 12월 순차 출력
            if month in monthly_data:
                total = monthly_data[month]['total_price']
                count = monthly_data[month]['count']
                average = total / count if count > 0 else 0
                print(f"{month}월: 평균 가격 {average:,.2f}원 (총 {count}권)")
            else:
                print(f"{month}월: 데이터 없음")

else:
    print(f"[오류] 파일이 존재하지 않습니다: {file_path}")

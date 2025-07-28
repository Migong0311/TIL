import json
from pathlib import Path
from collections import defaultdict

# 1. 파일 경로 설정
file_path = Path('./data/books_500.json')# 또는 books_2000.json

# 2. 파일 존재 여부 확인
if not file_path.exists():
    print("❌ 오류: 파일이 존재하지 않습니다.")
else:
    # 3. JSON 데이터 읽기
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    # 4. 도서 리스트 판단
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and 'item' in data:
        items = data['item']
    else:
        print("❌ 데이터 형식이 올바르지 않습니다.")
        exit()

    # 5. 시리즈 정보가 있는 도서만 분류
    series_result = {}

    for item in items:
        series_info = item.get("seriesInfo")
        if not series_info:
            continue

        series_id = str(series_info.get("seriesId"))
        series_name = series_info.get("seriesName", "이름 없음")

        book = {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "author": item.get("author", ""),
            "pubDate": item.get("pubDate", ""),
            "description": item.get("description", ""),
            "isbn": item.get("isbn", ""),
            "isbn13": item.get("isbn13", "")
        }

        if series_id not in series_result:
            series_result[series_id] = {
                "seriesId": int(series_id),
                "seriesName": series_name,
                "books": []
            }

        series_result[series_id]["books"].append(book)

    # 6. series.json 파일로 저장
    with open("series.json", "w", encoding="utf-8") as f:
        json.dump(series_result, f, ensure_ascii=False, indent=2)

    # 7. 완료 메시지 출력
    print("모든 시리즈 데이터가 series.json 파일로 병합되었습니다.")

import json
from pathlib import Path
from collections import defaultdict

# 1. 파일 경로 설정
file_path = Path('./data/books_500.json')
  # 또는 books_2000.json

# 2. 파일 존재 여부 확인
if not file_path.exists():
    print(f"❌ 오류: 파일이 존재하지 않습니다: {file_path}")
else:
    print(f"📁 파일 확인 완료: {file_path.name}")

    # 3. JSON 데이터 읽기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    items = data.get('item', [])
    print(f"📚 총 도서 수: {len(items)}권")

    # 4. 카테고리 기준 도서 분류
    category_books = defaultdict(list)

    for item in items:
        category_id = item.get('categoryId', '000000')
        category_name = item.get('categoryName', '미분류')
        category_key = f"{category_id}_{category_name}"

        book = {
            'title': item.get('title', ''),
            'author': item.get('author', ''),
            'publisher': item.get('publisher', ''),
            'pubDate': item.get('pubDate', ''),
            'isbn': item.get('isbn', ''),
            'price': item.get('priceStandard', 0)
        }

        category_books[category_key].append(book)

    # 5. 카테고리별 JSON 파일로 저장
    for category_key, books in category_books.items():
        # 파일 이름 안전하게 만들기
        safe_filename = "".join(c for c in category_key if c.isalnum() or c in ['_', '-'])
        output_file = Path(f"category_{safe_filename}.json")

        with output_file.open('w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)

        print(f"✅ 저장 완료 → {output_file.name} ({len(books)}권)")

    # 6. 완료 메시지
    print(f"\n🎉 총 {len(category_books)}개의 카테고리 JSON 파일이 생성되었습니다.")
    
print(f"[DEBUG] 현재 경로: {file_path.absolute()}")
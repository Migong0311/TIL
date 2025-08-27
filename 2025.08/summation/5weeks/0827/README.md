# 0827 요약

# 📘 CSS 및 웹 관련 개념 정리

| 개념              | 설명                                                          | 예시                                   |
| ----------------- | ------------------------------------------------------------- | -------------------------------------- |
| **Bootstrap**     | 미리 만들어진 CSS Framework (Toolkit)                         | Bootstrap은 CDN으로 설치가 가능        |
| **CDN**           | 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 기술 | Bootstrap CDN                          |
| **Reset CSS**     | HTML 요소의 스타일을 일관된 기준으로 재설정하는 규칙 시트     | `bootstrap-reboot.css`                 |
| **Semantic HTML** | 모양과 기능 이외의 의미를 가지는 요소                         | `<header>`, `<article>`, `<nav>`       |
| **OCSS**          | 객체지향적 접근법을 활용한 CSS 방법론                         | 구조: `.button` / 스킨: `.button-blue` |

---

## 📌 요약
- **Bootstrap**: CSS 작업을 빠르게 할 수 있는 툴킷  
- **CDN**: 빠르고 안전한 전송 기술  
- **Reset CSS**: 브라우저별 차이를 줄이는 CSS 초기화 규칙  
- **Semantic HTML**: 의미 중심의 HTML 태그  
- **OCSS**: 구조와 스킨을 분리하는 객체지향적 CSS 설계 방식  


---

# 📘 오늘 학습 개념 안내

오늘 학습한 내용은 단순히 문서로 정리하기보다는 **공식 Bootstrap 사이트**를 직접 참고하면서 실습하는 것이 훨씬 효과적입니다.  

👉 공식 사이트: [bootstrap Docs](https://getbootstrap.com/)

---

## ✅ 실습 방식 추천
1. 위 사이트에 접속한다.  
2. 문서(`Docs`) 메뉴에서 **Layout**과 **Utilities** 부분을 집중적으로 확인한다.  
3. `Spacing`, `Reset CSS`, `Normalize CSS` 등의 개념을 찾아보고 실제 코드 예제를 복사한다.  
4. `index.html` 파일을 생성해서 복사한 코드를 붙여넣고 브라우저에서 확인한다.  
5. 직접 margin, padding, reset 스타일을 바꿔가며 화면 변화를 확인한다.  

---

## 🛠️ 실습 예시
```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="mt-5 p-3 bg-primary text-white">
      Hello, Bootstrap Spacing!
    </div>
  </body>
</html>
```

---

## 📌 정리

* 오늘 다룬 개념은 단순히 `md` 파일로 정리하는 것보다 **공식 문서에서 예제를 직접 실행**해보는 것이 중요하다.
* 코드를 직접 작성하고 브라우저에서 확인하면서 **margin·padding·reset·normalize CSS의 차이**를 눈으로 익히자.


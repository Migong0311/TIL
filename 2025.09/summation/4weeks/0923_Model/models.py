# 내장된 django 패키지 안에 db 서브 페키지 안에 models.py 라는 모듈을 import
from django.db import models
"""
- 여기서 클래스명은 앱 이름과는 무관하나 관련 DB명으로 선언하면 인지하기 편할거임
- title,content 라는 컬럼을 생성함
- 즉 클래스 변수명은 테이블에 각 필드(열) 이름을 뜻함
- charfield,textfield 는 데이터 타입 정의하는거임 
- SQL로 따지면 varchar ,text,integer 이런 타입 설정하는거
- charfield 파라미터의 max_length 는 SQL과 동일하게 선택적 요소 
- 그치만 데이터 명확성 및 유효성검사로 인하여 명시하는걸 적극 권장
- charfield 는 field type을 그 파라미터 값은 field option을 뜻함
- field type은 db저장될 데이터의 종류 field option은 필드의 동작과 제약조건을 정의
- textfield 파라미터값은 SQL에 null,notnull 처럼 허용 여부 체크
"""


class Article(models.Model):  # extends class Model
    ############ 문자열 필드##############
    # charfield 파라미터값은 varchar(10) 같은거임
    title = models.CharField(max_length=10)
    content = models.TextField(null=True)  # 무한대는 아니며 사용하는 시스템에 따라 달라짐
    #################필드 추가###########
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터 처음 생성된 시간만 자동저장
    updated_at = models.DateTimeField(auto_now=True)  # 데이터가 저장될 때마다 수정시간 자동저장
    
    # ############# 숫자 필드#############
    # age = models.IntegerField()
    # point = models.FloatField()
    # ############## 날짜/시간 필드############
    # datetime = models.DateTimeField()
    # date = models.DateField()
    # time = models.TimeField()
    # ############## 파일 관련 필드############
    # file = models.FileField()
    # image = models.ImageField()

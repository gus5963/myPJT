from django.db import models

# Create your models here.
# class - table 연결작업

class WebUser(models.Model):
    user_id = models.TextField(max_length=100)
    user_pwd = models.TextField(max_length=100)
    user_name = models.TextField(max_length=100)
    user_point = models.IntegerField(default=1000)
    user_regdate = models.DateTimeField(auto_now=True)


"""
DB에서 보면 위의 class가 아래와 같은 것.
create table WebUser(
    user_id varChar2(100),
    user_pwd varChar2(100),
    user_name varChar2(100),
    user_point number default 1000,
    user_regdate date default sysdate    
);
"""


# 선언한 변수가 테이블의 컬럼이 된다. 그렇기 때문에 Type을 지정해줘야 한다.
# TextField = varChar2
# IntegerField = number
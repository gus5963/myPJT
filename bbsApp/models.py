from django.db import models

# Create your models here.
class WebBbd(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=40)
    writer = models.CharField(max_length=20)
    # writer는 user랑 연동되어 login된 사람만 작성할 수 있도록 한다.
    content = models.TextField()
    regdate = models.DateField(auto_now=True)
    viewcnt = models.IntegerField(default=0)


class WebComment(models.Model):
    id = models.BigAutoField(primary_key = True)
    txt = models.CharField(max_length=300)
    writer = models.CharField(max_length=20)
    # writer는 user랑 연동되어 login된 사람만 작성할 수 있도록 한다.
    bbs_id = models.ForeignKey
    regdate = models.DateField(auto_now=True)


# 게시글 하나당 코멘트를 여러게 달 수 있도록 id를 코멘트에 FK로 달아준다.
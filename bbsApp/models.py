from django.db import models

# Create your models here.
class WebBbs(models.Model):
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
    bbs_id = models.ForeignKey(WebBbs,on_delete=models.CASCADE, db_column='bbs_id')
    # option으로 on_delete=models.CASCADE를 준 것은 게시글 작성자가 게시글을 삭제할 수 있도록 한 것. 왜냐하면 게시글이 부모이기 때문이다.
    regdate = models.DateField(auto_now=True)


# 게시글 하나당 코멘트를 여러게 달 수 있도록 id를 코멘트에 FK로 달아준다.
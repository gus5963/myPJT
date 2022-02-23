from django.contrib import admin
from .models import *
# .models는 현재 경로에서 models를 import한다는 것이다.


# Register your models here.
admin.site.register(WebUser)
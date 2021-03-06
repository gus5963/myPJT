from django.shortcuts import render, redirect
from .models  import *

# Create your views here.

##########login

def index(request):
    print('โ Get User Index ๐๐')
    if request.session.get('user_name'):
        # ์ธ์์ ์ด๋ฆ์ผ๋ก ํ์ธ์ ํด์ผ ํ๋ค.
        print('๐ Login session Exist')
        context = {
            'session_user_name' : request.session.get('user_name'),
            'session_user_id': request.session.get('user_id')
        }
        # django๋ ํน์ดํ ์ ์ผ๋ก return ํ๋ ๊ณณ์ session์ ์ฌ์ฉํ๊ฒ ๋๋ค๋ฉด context์ ๋ค์ ๋ด์์ฃผ๋ ์์์ ํด์ค์ผ ํ๋ค.
        # request.session.get('user_id') = request.session['user_name']
        return render(request, 'user/ok.html', context)

    else:
        return render(request, 'user/index.html')

# select * from WebUser where id = x and pwd = x
# orm์ผ๋ก ์์ฑํ๋ค๋ฉด : modelName.objects.get()  <= get() ์ where์ ๊ฐ๋ค.
# select * from WebUser
#  => orm : WebUser.objects.all()
# session tracking mechanism
# session์ผ๋ก ๋ง์ ๊ฒ๋ค์ ์ฐ๋์ํฌ ์ ์๋ค. ์กฐ๊ฑด์ ์ฌ์ฉํ๋ฉด  ์ฌ๋ฌ๊ฐ์ง ํ  ์ ์๋ค.


def login(request):
    print('โ Get User Login ๐๐')
    if request.method == 'POST':
        print('๐ request post')
        # DB์ ํต์ ..
        id = request.POST['id']
        pwd = request.POST['pwd']
        print('โ๐ฅ request param : ', id, pwd)
        # model - DB(select)
        # ์ ๋ณด๋ฅผ ๋ด๋ ์์์ ํ์๋ก ํ๋ค.
        context = {}
        try:
            user = WebUser.objects.get(user_id = id, user_pwd = pwd)
            # ์ค์ํ์ง ๋ง์์ผ ํ  ๊ฒ.!!
            # table์ ๋ง๋ค์๊ณ  admin์์ id, pwd๋ฅผ ๋ฃ๊ณ  ์ ์ฅํ์ผ๋
            # ์์ get์ด where์ ๊ฐ์ ๋ง์ด๊ธฐ ๋๋ฌธ์ ๋๋ ํ์ด๋ธ์ ๋ฃ์๋ id์ pwd๋ฅผ input์ ์๋ ฅํ์ด์ผ ํ๋ค....
            # print('โ๏ธ model value : ', user.user_name)
            # context = {'loginUser' : user}
            # user์ ํ๋์ ๊ฐ์ฑ๋ก ๋์ด ์๊ธฐ ๋๋ฌธ์ ์์ ๋ก user_name์ ๊ฐ๊ณ ์ฌ ์ ์๋ค.
            request.session['user_name'] = user.user_name   # user์ user_name์ session์ ์ฌ์ด์ฃผ๋ ๊ฒ.๋ ๊ดํธ์์๋ ์์๋ก ์ด๋ฆ์ ์ ํด์ค ๊ฒ
            request.session['user_id'] = user.user_id
            # session์ ๋ง๋๋ ๊ณผ์ 
            context['session_user_name'] = request.session['user_name']
            context['session_user_id'] = request.session['user_id']
            # session์ ์ฌ๋ ๊ณผ์ 
            return render(request, 'user/ok.html', context)
        except Exception as e:
            context['error'] = str(e)
            return render(request, 'user/index.html', context)
        # if๋ฅผ ์ฌ์ฉํ์ฌ ๋ก๊ทธ์ธ์ ์ฑ๊ณต ์ฌ๋ถ๋ฅผ ์์ฑํด์ผ ํ๋ค.
        # session์ ๋ฃ์ผ๋ฉด ๋ชจ๋  ํ์ด์ง์์ ์ฌ์ฉํ  ์ ์๋ค.

def logout(request):
    print('โ Get User Log Out ๐๐')
    # Delete session
    request.session['user_name']={}
    request.session['user_id']={}
    request.session.modified = True

    # ์๋ก์ด request url์ ์ ์ํ  ๋
    return redirect('main')

######### list
def list(request):
    print('โ Get User List ๐๐')
    division = request.GET['category']
    print('๐ List param : ', division)
    # model - select * from table_name where category = 'sport'
    users = WebUser.objects.all()
    for u in users:
        print('๐ก User name',u.user_name)
    context = {
        'users' : users
    }
    return render(request, 'user/list.html',context)


def detail(request):
    print('โ Get User Detail ๐๐')
    id = request.GET['id']
    print('โ๐ฅ request param : ', id)
    user = WebUser.objects.get(user_id = id)
    if user is not None:
        context = {
            'user': user
        }
    else:
        context = {
            'warning' : '๊ด๋ฆฌ์ ์ ์ฉ์๋๋ค.'
        }
    return render(request, 'user/detail.html', context)
    # render๋ฅผ ํ๊ฒ๋๋ฉด url์ ์ ์งํ๊ณ  ๋ณด์ฌ์ง๋ ํ๋ฉด์ด html์ธ ๊ฒ.

######### sign up
def signUp(request):
    print('โ Get User Sign Up ๐๐')
    return  render(request, 'user/signUp.html')

def join(request):
    print('โ Get User Join ๐๐')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('โ๐ฅ request param : ', id, pwd, name)
    # insert into table_name(id, pwd, name) values(value1, 2, 3)
    # orm ๋ฐฉ์
    # orm : modelName(attr-value).save()
    WebUser(user_id= id, user_pwd=pwd, user_name=name).save()

    # ํ๋ฉด์ ๋ถ๊ธฐ์ํค๋ ๋ฐฉ๋ฒ์ 2๊ฐ์ง๊ฐ ์๋ฐ. render / redirect
    # return render(request, 'user/index.html')
    # render : page๋ฅผ ์ง์นญํ๋ค.
    return redirect('userIndex')
    # redirect : url์ ์ง์นญํ๋ค.
    # redirect๋ Url์ ๊ฐ๊ณ ์ค์ง๋ง urlpattern์ ์๋ url์ ๊ฐ๊ณ ์ฌ ์ ์์ง๋ง ํด๋น url์ name์ ์ฐพ์์ ๊ทธ values๋ฅผ ๊ฐ๊ณ ์จ๋ค.
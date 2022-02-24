from django.shortcuts import render, redirect
from .models  import *

# Create your views here.

##########login

def index(request):
    print('✅ Get User Index 🚀🚀')
    if request.session.get('user_name'):
        # 세션의 이름으로 확인을 해야 한다.
        print('🛑 Login session Exist')
        context = {
            'session_user_name' : request.session.get('user_name'),
            'session_user_id': request.session.get('user_id')
        }
        # django는 특이한 점으로 return 하는 곳에 session을 사용하게 된다면 context에 다시 담아주는 작업을 해줘야 한다.
        # request.session.get('user_id') = request.session['user_name']
        return render(request, 'user/ok.html', context)

    else:
        return render(request, 'user/index.html')

# select * from WebUser where id = x and pwd = x
# orm으로 작성한다면 : modelName.objects.get()  <= get() 은 where와 같다.
# select * from WebUser
#  => orm : WebUser.objects.all()
# session tracking mechanism
# session으로 많은 것들을 연동시킬 수 있다. 조건을 사용하면  여러가지 할 수 있다.


def login(request):
    print('✅ Get User Login 🚀🚀')
    if request.method == 'POST':
        print('🛑 request post')
        # DB와 통신..
        id = request.POST['id']
        pwd = request.POST['pwd']
        print('‍🔥 request param : ', id, pwd)
        # model - DB(select)
        # 정보를 담는 작업을 필요로 한다.
        context = {}
        try:
            user = WebUser.objects.get(user_id = id, user_pwd = pwd)
            # 실수하지 말아야 할 것.!!
            # table을 만들었고 admin에서 id, pwd를 넣고 저장했으니
            # 위의 get이 where와 같은 말이기 때문에 나는 테이블에 넣었던 id와 pwd를 input에 입력했어야 했다....
            # print('⛔️ model value : ', user.user_name)
            # context = {'loginUser' : user}
            # user은 하나의 객채로 되어 있기 때문에 소유로 user_name을 갖고올 수 있다.
            request.session['user_name'] = user.user_name   # user의 user_name을 session에 심어주는 것.대 괄호안에는 임의로 이름을 정해준 것
            request.session['user_id'] = user.user_id
            # session을 만드는 과정
            context['session_user_name'] = request.session['user_name']
            context['session_user_id'] = request.session['user_id']
            # session을 심는 과정
            return render(request, 'user/ok.html', context)
        except Exception as e:
            context['error'] = str(e)
            return render(request, 'user/index.html', context)
        # if를 사용하여 로그인의 성공 여부를 작성해야 한다.
        # session에 넣으면 모든 페이지에서 사용할 수 있다.

def logout(request):
    print('✅ Get User Log Out 🚀🚀')
    # Delete session
    request.session['user_name']={}
    request.session['user_id']={}
    request.session.modified = True

    # 새로운 request url을 정의할 때
    return redirect('main')

######### list
def list(request):
    print('✅ Get User List 🚀🚀')
    division = request.GET['category']
    print('🛑 List param : ', division)
    # model - select * from table_name where category = 'sport'
    users = WebUser.objects.all()
    for u in users:
        print('💡 User name',u.user_name)
    context = {
        'users' : users
    }
    return render(request, 'user/list.html',context)


def detail(request):
    print('✅ Get User Detail 🚀🚀')
    id = request.GET['id']
    print('‍🔥 request param : ', id)
    user = WebUser.objects.get(user_id = id)
    if user is not None:
        context = {
            'user': user
        }
    else:
        context = {
            'warning' : '관리자 전용입니다.'
        }
    return render(request, 'user/detail.html', context)
    # render를 하게되면 url은 유지하고 보여지는 화면이 html인 것.

######### sign up
def signUp(request):
    print('✅ Get User Sign Up 🚀🚀')
    return  render(request, 'user/signUp.html')

def join(request):
    print('✅ Get User Join 🚀🚀')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('‍🔥 request param : ', id, pwd, name)
    # insert into table_name(id, pwd, name) values(value1, 2, 3)
    # orm 방식
    # orm : modelName(attr-value).save()
    WebUser(user_id= id, user_pwd=pwd, user_name=name).save()

    # 화면을 분기시키는 방법은 2가지가 있따. render / redirect
    # return render(request, 'user/index.html')
    # render : page를 지칭한다.
    return redirect('userIndex')
    # redirect : url을 지칭한다.
    # redirect는 Url을 갖고오지만 urlpattern에 있는 url을 갖고올 수 없지만 해당 url의 name을 찾아서 그 values를 갖고온다.
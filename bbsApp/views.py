from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    print('✅ Get bbs Index 🚀🚀')
    # model orm
    boards = WebBbs.objects.all().order_by('-id')
    context = {
        'boards' : boards
    }
    return render(request, 'bbs/index.html', context)


def createForm(request):
    print('✅ Get bbs Create Form 🚀🚀')
    return render(request, 'bbs/createForm.html')


def bbsWrite(request):
    print('✅ Get bbs Write 🚀🚀')
    title = request.POST['title']
    writer = request.POST['writer']
    content = request.POST['content']
    WebBbs(title=title, writer=writer,content=content).save()
    return redirect('bbsIndex')


def bbsRead(request):
    print('✅ Get bbs Read 🚀🚀')
    id = request.GET['id']
    print('⛔️ request check', id)
    # select - orm - get(single finder) | filter(multi finder)
    # view Count
    board = WebBbs.objects.get(id=id)
    board.viewcnt += 1
    board.save()

    context = {'board':board}
    return render(request, 'bbs/read.html', context)


def bbsRemove(request):
    print('✅ Get bbs Remove 🚀🚀')
    id = request.GET['id']
    print('⛔️ request check', id)
    # orm - delete 사용하기
    board = WebBbs.objects.get(id=id)
    board.delete()
    return redirect('bbsIndex')

def bbsUpdate(request):
    print('✅ Get bbs Update 🚀🚀')
    id = request.GET['id']
    title = request.GET['title']
    content = request.GET['content']
    print('⛔️ request check', id, title, content)
    board = WebBbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save()
    return redirect('bbsIndex')

def bbsSearch(request):
    print('✅ Get bbs Search 🚀🚀')
    type = request.POST['type']
    keyword = request.POST['keyword']
    print('⛔️ request check', type, keyword)
    # orm 작업 like pattern 검색, render 은 사용 금지
    # script에서 사용할 수 있는 타입으로 작성해줘야 한다. 2가지 있음 dict / [dict]
    # orm => filter를 사용하자. __ 앞 에는 컬럼의 이름을 적으면 된다.
    # filter(__icontains) => %공지%
    # filter(__startswith) => 공지%
    # filter(__endswith) => %공지
    # select * from table where title like ''
    # select * from table where writer like ''
    if type == 'title':
        boards = WebBbs.objects.filter(title__icontains = keyword)
    if type == 'writer':
        boards = WebBbs.objects.filter(writer__startswith = keyword)
    jsonAry = []
    for board in boards:
        jsonAry.append({
            'id':board.id,
            'title':board.title,
            'writer':board.writer,
            'regdate':board.regdate,
            'viewcnt':board.viewcnt
        })
    return JsonResponse(jsonAry, safe=False)
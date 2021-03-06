from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    print('β Get bbs Index ππ')
    # model orm
    boards = WebBbs.objects.all().order_by('-id')
    context = {
        'boards' : boards
    }
    return render(request, 'bbs/index.html', context)


def createForm(request):
    print('β Get bbs Create Form ππ')
    return render(request, 'bbs/createForm.html')


def bbsWrite(request):
    print('β Get bbs Write ππ')
    title = request.POST['title']
    writer = request.POST['writer']
    content = request.POST['content']
    WebBbs(title=title, writer=writer,content=content).save()
    return redirect('bbsIndex')


def bbsRead(request):
    print('β Get bbs Read ππ')
    id = request.GET['id']
    print('βοΈ request check', id)
    # select - orm - get(single finder) | filter(multi finder)
    # view Count
    board = WebBbs.objects.get(id=id)
    board.viewcnt += 1
    board.save()

    context = {'board':board}
    return render(request, 'bbs/read.html', context)


def bbsRemove(request):
    print('β Get bbs Remove ππ')
    id = request.GET['id']
    print('βοΈ request check', id)
    # orm - delete μ¬μ©νκΈ°
    board = WebBbs.objects.get(id=id)
    board.delete()
    return redirect('bbsIndex')

def bbsUpdate(request):
    print('β Get bbs Update ππ')
    id = request.GET['id']
    title = request.GET['title']
    content = request.GET['content']
    print('βοΈ request check', id, title, content)
    board = WebBbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save()
    return redirect('bbsIndex')

def bbsSearch(request):
    print('β Get bbs Search ππ')
    type = request.POST['type']
    keyword = request.POST['keyword']
    print('βοΈ request check', type, keyword)
    # orm μμ like pattern κ²μ, render μ μ¬μ© κΈμ§
    # scriptμμ μ¬μ©ν  μ μλ νμμΌλ‘ μμ±ν΄μ€μΌ νλ€. 2κ°μ§ μμ dict / [dict]
    # orm => filterλ₯Ό μ¬μ©νμ. __ μ μλ μ»¬λΌμ μ΄λ¦μ μ μΌλ©΄ λλ€.
    # filter(__icontains) => %κ³΅μ§%
    # filter(__startswith) => κ³΅μ§%
    # filter(__endswith) => %κ³΅μ§
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
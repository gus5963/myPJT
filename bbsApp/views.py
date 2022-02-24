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
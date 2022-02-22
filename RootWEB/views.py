from django.shortcuts import render
def index(request):
    print('✅ Get Index 🚀🚀')
    context = {'intro' : 'hello world!!'}
    return render(request, 'index.html', context)  # context를 만들면 rendering시 index.html로 들어가게 된다.
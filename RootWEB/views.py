from django.shortcuts import render
def index(request):
    print('✅ Get Index 🚀🚀')
    context = {'intro' : 'hello world!!'}
    return render(request, 'index.html', context)  # context를 만들면 rendering시 index.html로 들어가게 된다.
    # render는 templates파일을 추적하는 것 같음... 그래서 route를 찾을 때 따로 templates라고 지정을 안한다.
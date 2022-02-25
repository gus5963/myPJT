from django.shortcuts import render

# Create your views here.

def index(request):
    print('✅ Get Static Index 🚀🚀')
    return render(request, 'nondynamic/index.html')


def line(request):
    print('✅ Get Static Line 🚀🚀')
    installation = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    context = {
        'installation': installation
    }
    # 위와같이 template 를 사용할 때 document에만 사용할 수 있는 것이 아닌, script 안에서도 사용이 가능하다.
    return render(request, 'nondynamic/line.html', context)


def bar(request):
    print('✅ Get Static Bar 🚀🚀')
    year = [3000, 3000, 3000, 3000, 3000]
    context = {
        'year' : year
    }
    # 위와같이 template 를 사용할 때 document에만 사용할 수 있는 것이 아닌, script 안에서도 사용이 가능하다.
    return render(request, 'nondynamic/bar.html', context)
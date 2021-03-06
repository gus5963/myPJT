from django.shortcuts import render

# Create your views here.

def index(request):
    print('β Get Static Index ππ')
    return render(request, 'nondynamic/index.html')


def line(request):
    print('β Get Static Line ππ')
    installation = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    context = {
        'installation': installation
    }
    # μμκ°μ΄ template λ₯Ό μ¬μ©ν  λ documentμλ§ μ¬μ©ν  μ μλ κ²μ΄ μλ, script μμμλ μ¬μ©μ΄ κ°λ₯νλ€.
    return render(request, 'nondynamic/line.html', context)


def bar(request):
    print('β Get Static Bar ππ')
    year = [3000, 3000, 3000, 3000, 3000]
    context = {
        'year' : year
    }
    # μμκ°μ΄ template λ₯Ό μ¬μ©ν  λ documentμλ§ μ¬μ©ν  μ μλ κ²μ΄ μλ, script μμμλ μ¬μ©μ΄ κ°λ₯νλ€.
    return render(request, 'nondynamic/bar.html', context)
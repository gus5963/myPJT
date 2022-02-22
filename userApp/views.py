from django.shortcuts import render

# Create your views here.


def index(request):
    print('✅ Get User Index 🚀🚀')
    return render(request, 'user/index.html')

def login(request):
    print('✅ Get User Login 🚀🚀')
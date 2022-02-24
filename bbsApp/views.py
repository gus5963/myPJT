from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print('✅ Get bbs Index 🚀🚀')
    return render(request, 'bbs/index.html')
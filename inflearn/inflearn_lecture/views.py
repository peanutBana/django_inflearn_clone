from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'inflearn_lecture/home_list.html',{'texts':texts})

def lecture_list(request):
    texts = myText.objects.filter()

    hot_lecture = myText.objects.filter(category="인기")
    print(texts)
    return render(request, 'inflearn_lecture/lecture_list.html',
                {'texts':texts, 'hot_lecture':hot_lecture})

def login(request):
    return render( request, 'inflearn_lecture/login.html')

def join(request):

    print("join 실행")
    if request.method =="POST":
        print("포스팅 요청")

        return redirect('/')

    print("join 마지막 부분")
    return render( request, 'inflearn_lecture/join.html')

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    #http://127.0.0.1:8000?username=xxx
    username=request.GET.get('username')
    print(username)
    if username:
        return HttpResponse("前台首页")
    else:
        # print(reversed('sigin'))
        return (reversed('front:signin'))
        # return redirect('/login/') #这个是写死了，如果一旦换成sigin 那么都要进行修改
    pass

def login(request):
    return HttpResponse("前台登陆首页")
    pass


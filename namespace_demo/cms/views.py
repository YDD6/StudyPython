from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    #http://127.0.0.1:8000?username=xxx
    username = request.GET.get('username')
    print(username)
    if username:
        return HttpResponse("后台首页")
    else:
        login_url = reverse('cms:signin')
        # print(reversed('sigin'))
        return redirect(login_url)
        # return redirect('/login/') #这个是写死了，如果一旦换成sigin 那么都要进行修改
        current_namespace = request.resolver_match.namespace
        # return redirect(reversed("%s:login" % current_namespace))


def login(request):
    return HttpResponse("后台登陆首页")
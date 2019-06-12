from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index(request):
    # http://127.0.0.1:8000?username=xxx
    username = request.GET.get('username')
    print(username)
    if username:
        return HttpResponse("前台首页")
    else:
        login_url = reverse('front:signin', kwargs={"actical_id": 1, "p": 6})
        # login_url = reverse('front:signin') + "?next/="
        # print(reversed('sigin'))
        return redirect(login_url)
        # return redirect('/login/') #这个是写死了，如果一旦换成sigin 那么都要进行修改


def login(request):
    return HttpResponse("前台登陆首页")


def actical_detail(request, artical_id, p):
    text = '你要查看的文章id是：%s ，页码是： %s' % (artical_id, p)
    return HttpResponse(text)

from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def article(request):
    return HttpResponse("首页")

def article_list(request, year):
    text='你输入的年份是：%s' % year
    return HttpResponse(text)
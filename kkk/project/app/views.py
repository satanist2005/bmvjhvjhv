from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    text = f' host: {host}, browser {user_agent}, path: {path}'
    return HttpResponse('jghkjhgjk')

def user(request, name, age):
    return HttpResponse(f'User: {name}. His age {age}')

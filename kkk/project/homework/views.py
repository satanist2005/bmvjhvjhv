from django.shortcuts import render
from django.http import HttpResponse

def error(request):
    return HttpResponse('uyuyu', status=400, reason="jlkhghjfhg fytytyj")
    # return HttpResponse("К сожалению произошла ошибка", status=412, reason="К сожалению произошла ошибка")

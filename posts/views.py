from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

app_name = 'posts'


@login_required
def test(request):
    return HttpResponse('It is alive')

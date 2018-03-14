from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
def signin(request,username):
    test = 1
    test1 = test + 1
    if User.objects.filter(username=username).exists():
        password = "edx"
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    else:
        userInsert = User.objects.create_user(username, username + '@lacviet.com.vn', 'edx')
        userInsert.save()
        user = authenticate(username=userInsert.username,password='edx')
        login(request, user)
    return  HttpResponse("<h1>sang</h1>")
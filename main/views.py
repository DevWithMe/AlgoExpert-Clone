from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
import requests
from django.urls import reverse

GITHUB_OAUTH_ID = ""
GITHUB_OAUTH_SECRET = ""

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def info(request, section):
    if section != "problem":
        return HttpResponse("Hello World")
    return HttpResponse("Hello Problem!")

def login_view(request):
    return HttpResponseRedirect(f"https://github.com/login/oauth/authorize?client_id={GITHUB_OAUTH_ID}")

def github(request):
    code = request.GET["code"]
    info = requests.post(f"https://github.com/login/oauth/access_token?client_id={GITHUB_OAUTH_ID}&client_secret={GITHUB_OAUTH_SECRET}&code={code}", headers={"Accept": "application/json"}).json()
    print(info)
    access_token = info["access_token"]
    info = requests.get("https://api.github.com/user", headers={"Authorization": f"token {access_token}"}).json()
    # print(info)
    # is user in the database
    try:
        user = (User.objects.get(username=info["login"]))
        profile = Profile.objects.get(user=user)
        login(request, user)
        request.session["avator"] = profile.avator
        return HttpResponseRedirect(reverse("index"))
    except User.DoesNotExist:
        user = User.objects.create_user(username=info["login"], password=info["node_id"], email=info["email"])
        user.save()
        profile = Profile(user=user, paid="False", avator=info["avatar_url"])
        profile.save()
        login(request, user)
        request.session["avator"] = profile.avator
        return HttpResponseRedirect(reverse("index"))

    return HttpResponse(str(info))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
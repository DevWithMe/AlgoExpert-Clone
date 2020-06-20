from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import requests

GITHUB_OAUTH_ID = ""
GITHUB_OAUTH_SECRET = ""

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def info(request, section):
    if section != "problem":
        return HttpResponse("Hello World")
    return HttpResponse("Hello Problem!")

def login(request):
    return HttpResponseRedirect(f"https://github.com/login/oauth/authorize?client_id={GITHUB_OAUTH_ID}")

def github(request):
    code = request.GET["code"]
    info = requests.post(f"https://github.com/login/oauth/access_token?client_id={GITHUB_OAUTH_ID}&client_secret={GITHUB_OAUTH_SECRET}&code={code}", headers={"Accept": "application/json"}).json()
    print(info)
    access_token = info["access_token"]
    info = requests.get("https://api.github.com/user", headers={"Authorization": f"token {access_token}"}).json()
    # print(User.objects.get(username='fsmith'))
    return HttpResponse(str(info))
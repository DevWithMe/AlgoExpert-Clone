from django.shortcuts import render
from django.http import HttpResponse
from subprocess import Popen
import subprocess

# Create your views here.
def index(request):
    return render(request, "CodeEditor/index.html")

def run_code(request):
    code = request.GET["code"]
    problem = request.GET["problem"]
    solution = open("solution.py", mode="w")
    solution.write(code)
    solution.close()
    out = Popen(["python3", "test.py"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return HttpResponse(stdout)
    info = str(stdout).split('======================================================================')
    for i in range(1, len(info)):
        message = info[i].split("line")[2]
        print("line" + ("<br />".join(message.split("\\n"))))
        print("end")
    return HttpResponse(code)


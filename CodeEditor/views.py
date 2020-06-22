from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess
from termcolor import colored

# Create your views here.
def index(request):
    return render(request, "CodeEditor/index.html")

def run_code(request):
    code = request.GET["code"]
    #problem = request.GET["problem"]
    solution = open("solution.py", mode="w")
    print(colored(code, "red"))
    solution.write(code)
    solution.close()
    out = Popen(["python3", "test.py"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    data = str(stdout).split("======================================================================")

    messages = {}
    for i in range(1, len(data)):
        messages[i-1] = ("<br />".join(data[i].split("\\n")).split("----------------------------------------------------------------------")[1])
        # return HttpResponse(data[3])
    print(stdout)
    return JsonResponse(data=messages, safe=False)


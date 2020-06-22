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

    response = {
        "error": {}, # test_# : error message / passed,
        "input": {"1": 2, "2": 9, 3: "random", 4: "random", 5: "random", 6: "random", 7: "random"}
    }
    for i in range(1, len(data)):
        info = ("<br />".join(data[i].split("\\n")).split("----------------------------------------------------------------------")[1])
        number = int(info.split("test_")[1][0])
        response["error"][number] = info
        # print(colored(info, "green"))
        # return HttpResponse(data[3])
    for i in range(1, 8):
        try:
            response["error"][i]
        except KeyError:
            response["error"][i] = "passed"
    return JsonResponse(data=response)


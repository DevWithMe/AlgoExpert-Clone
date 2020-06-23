from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess
from termcolor import colored
from .models import Code, Passed
from django.contrib.auth.decorators import login_required
from api.views import PROBLEMS

# Create your views here.
@login_required(redirect_field_name='login')
def index(request, problem_id):
    try:
        PROBLEMS[problem_id-1]
    except IndexError:
        return HttpResponse("Problem doesn't exist")
    try:
        existing_code = Code.objects.get(user_id=request.user.id, problem_id=problem_id)
    except:
        return render(request, "CodeEditor/index.html", {
            "title": PROBLEMS[problem_id-1]["title"],
            "description": PROBLEMS[problem_id-1]["description"],
            "id": PROBLEMS[problem_id-1]["id"],
            "starter": PROBLEMS[problem_id-1]["starter"]
        })
    return render(request, "CodeEditor/index.html", {
        "title": PROBLEMS[problem_id-1]["title"],
        "description": PROBLEMS[problem_id-1]["description"],
        "id": PROBLEMS[problem_id-1]["id"],
        "exist": existing_code
    })


@login_required(redirect_field_name='login')
def run_code(request):
    code = request.GET["code"]
    problem = int(request.GET["problem"])
    try:
        existing_code = Code.objects.get(user_id=request.user.id, problem_id=problem)
        existing_code = Code.objects.filter(user_id=request.user.id, problem_id=problem).update(code=code)
    except:
        code_ = Code(user_id=request.user.id, problem_id=problem, code=code)
        code_.save()

    solution = open("solution.py", mode="w")
    solution.write(code)
    solution.close()
    if problem == 1:
        out = Popen(["python3", "-m", "unittest", "-q", "test.NthFib"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 2:
        out = Popen(["python3", "-m", "unittest", "-q", "test.PalindromeChecker"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    data = str(stdout).split("======================================================================")

    response = {
        "error": {}, # test_# : error message / passed,
        "input": {"1": 2, "2": 9, 3: "random", 4: "random", 5: "random", 6: "random", 7: "random"}
    }

    print(stdout)

    for i in range(1, len(data)):
        info = ("<br />".join(data[i].split("\\n")).split("----------------------------------------------------------------------")[1])
        number = int(info.split("test_")[1][0])
        response["error"][number] = info
    for i in range(1, 8):
        try:
            response["error"][i]
        except KeyError:
            response["error"][i] = "passed"

    if b"SyntaxError" in stdout or b"NameError" in stdout:
        for i in range(1, 8):
            response["error"][i] = "SyntaxError/NameError"

    passed = True
    for i in response["error"]:
        if response["error"][i] != "passed":
            passed = False

    try:
        exist = Passed.objects.get(user_id=request.user.id, problem_id=problem)
    except:
        passed = Passed(user_id=request.user.id, problem_id=problem)
        passed.save()

    return JsonResponse(data=response)
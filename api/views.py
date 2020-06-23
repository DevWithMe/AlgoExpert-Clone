from django.shortcuts import render
from django.http import JsonResponse
from CodeEditor.models import Passed

# Create your views here.
PROBLEMS = [
    {
        "id": 1,
        "title": "Nth Fibonacci Sequence",
        "description": "<h4>Find nth fib</h4>",
        "starter": "def nth_fib(n):\n\tpass",
    },
    {
        "id": 2,
        "title": "Palindrome Checker",
        "description": "Check palindrome",
        "starter": "def palindrome(n):\n\tpass"
    }
]


def problems(request):
    pros = PROBLEMS.copy()
    for i in pros:
        try:
            Passed.objects.get(user_id=request.user.id, problem_id=i["id"])
            i["complete"] = "True"
        except Passed.DoesNotExist:
            i["complete"] = "False"
    return JsonResponse(pros, safe=False)

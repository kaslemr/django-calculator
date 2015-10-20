
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index_view(request):
    x = request.GET.get("number1")
    y = request.GET.get("number2")
    z = request.GET.get("operator")
    if x:
        x = int(x)
    if y:
        y = int(y)
    if x and y and z:
        if z == "+":
            result = x + y
        elif z == "-":
            result = x - y
        elif z == "/":
            result = x / y
        elif z == "x":
            result = x * y
        else:
            result = x**y
    elif x and not y:
        result = x
    elif y and not x:
        result = y
    else:
        result = 0
    context = {"first_num": x, "second_num": y, "print_result": result, "operator": z}
    return render_to_response(template_name="calculator.html", context=context)


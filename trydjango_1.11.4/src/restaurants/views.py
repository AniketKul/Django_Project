import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view

# def home_old(request):
#
#     html_var = 'VARIABLE SUBSTITUTION'
#
#     html_ = f"""
#     <html>
#         <head>
#         </head>
#         <body>
#             <h1>Welcome to my restaurant</h1>
#             <p>This is {html_var} coming through</p>
#         </body>
#     </html>
#     """
#
#     #f strings
#     #return HttpResponse("hello")
#     return HttpResponse(html_)
#     #return render(request, "home.html", {})#response

def home(request):
    num = random.randint(0, 3321)
    #some_list = [1,2,3,4,5,6,7,8,9]
    some_list = [num, random.randint(0, 3321), random.randint(0, 3321)]
    #some_list = []

    context = {
        "bool_item": True,
        "num": num,
        "some_list": some_list
    }

    return render(request, "base.html", context)

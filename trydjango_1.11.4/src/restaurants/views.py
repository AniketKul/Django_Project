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
    return render(request, "base.html", {"html_var":"CONTEXT VARIABLE SUBSTITUTION", "num":num})

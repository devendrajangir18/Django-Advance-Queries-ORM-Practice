from django.shortcuts import render, redirect

from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

# TO USE DJANGO TEMPLATES WE USE RENDER METHOD
# django template apne aap utha leta hai to "templates" name hi folder banana pdta hai 
# and baki ka path mention krdo

# FUNTION TO SEND EMAIL

# def send_email(request):
#     send_email_to_client()
#     return redirect('/')

# FUNTION TO SEND EMAIL WITH ATTAACHMENT

def send_email(request):
    subject = "This email is from Django server with Attachment"
    message = "Hey please find this attach file with this email"
    recipient_list = [""]
    file_path = f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')

def home(request):
    # seed_db(100) # call seed function to create Student Dummy data

    peoples = [
        {'name': 'Ram', 'age': 26},
        {'name': 'Shaym', 'age': 16},
        {'name': 'Hari', 'age': 56},
        {'name': 'Krishna', 'age': 12},
        {'name': 'Shiv', 'age': 28}
    ]

    # for people in peoples:
    #     if people['age']:
    #         print("Yes")

    return render(request, "home/index.html", context = {'page': 'Home', 'peoples': peoples }) 

def about(request):
    context = {'page': 'About'}
    return render(request,"home/about.html", context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)




# def home(request):  
#     return HttpResponse("<h1>This is home page.</h1>")
                        
# WE DONOT USE THIS HTML AND CSS SO WE USE JINJA TEMPLATE 
# FOR STYLES AND WE RENDER IT FROM DJANGO BACKEND SERVER

# def home(request):
#     return HttpResponse("""<h1>This is home page.</h1>
#             <p> Hey this is coming from dajango server</P>
#             <hr>
#             <h3 style="color:red"> Hope you are loving it :) </h3>           
#     """)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h2> this page successfully loaded</h1>")
from django.shortcuts import render

from django.http import HttpResponse


# TO USE DJANGO TEMPLATES WE USE RENDER METHOD
# django template apne aap utha leta hai to "templates" name hi folder banana pdta hai 
# and baki ka path mention krdo

def home(request):

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
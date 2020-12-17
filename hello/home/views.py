from django.shortcuts import render, HttpResponse
from home.models import Contact, Library, category
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    
    return render(request, "index.html")
    #return HttpResponse("Home page")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("about page")
def Books(request):
    return render(request, "books.html")

def Category(request):
    lis = Library.objects.all()
    
    return render(request, "category.html", {"lis":lis})
    #return HttpResponse("Books page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        contact = Contact(name=name, email= email, phone= phone, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, "contact.html")
    #return HttpResponse("contact page")

def signup(request):
    return render(request, "signup.html")
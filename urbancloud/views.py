from django.shortcuts import render
from urbancloud.models import Contactus
from django.contrib import messages
from email import message

# Create your views here.
def index(request):
    return render (request, 'index.html')

def aboutus(request):
    return render (request, 'aboutus.html')

def service(request):
    return render (request, 'service.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contactus = Contactus(name=name,email=email,subject=subject,message=message)
        contactus.save()
        messages.success(request, 'Thank you for sharing your feedback with us !! ')
    return render (request, 'contactus.html')


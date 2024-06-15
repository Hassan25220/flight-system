from django.shortcuts import render, redirect
from .email_utils import send_email_to_client
# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def send_email(request):
    send_email_to_client()
    return redirect("/")

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
   return render(request,'generator/home.html')

def about(request):
   return render(request,'generator/about.html')

def password(request):
   plst = list('abcdefghijklmnopqrstuvwxyz')
   thepassword = ''
   length =int(request.GET.get('length',9)) #very imp to covert , u get everything as str
   if request.GET.get('uppercase'):
       plst.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
   if request.GET.get('chars'):
       plst.extend('!@#$%^&*{[]}?/:+-/)')
   if request.GET.get('number'):
       plst.extend('0123456789')
    
   for x in range(length):
       thepassword += random.choice(plst)
   return render(request,'generator/password.html',{'password':thepassword})


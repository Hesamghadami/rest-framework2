from django.shortcuts import render , redirect
from .models import Services, NewsLetter
from courses.models import Course,Trainer
from courses.models import Category
from accounts.models import CustomeUser
from .forms import NewsLetterForm, ContactUsForm
from django.contrib import messages
from django.views.generic import TemplateView, RedirectView

# Create your views here.



# def home (request):
#     if request.method == 'GET':

#         return render(request,"root/index.html")
#     elif request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             messages.add_message(request,messages.SUCCESS,'your email submited')
#             return redirect('root:home')   
#         else :
#             messages.add_message(request,messages.ERROR,'Invalid email address')
#             return redirect('root:home')


class HomeView(TemplateView):
    template_name = 'root/index.html'




def about (request):
    if request.method == 'GET' :
        trainer = Trainer.objects.filter(status=True)
        context = {
            'trainer':trainer,
        }
        return render(request,"root/about.html",context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:about')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:about')

def contact(request):
    if request.method =='GET':

        return render(request,"root/contact.html")
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')
        
        
    



def trainer(request):
    if request.method =='GET':
        trainer = Trainer.objects.filter(status=True)
        context = {
            'trainer':trainer,
        }
        return render(request,"root/trainers.html",context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:trainer')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:trainer')
from django.shortcuts import redirect
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import  Profile
from .forms import AuthenticationForm
from django.views.generic import FormView, CreateView, UpdateView, TemplateView




# def Login(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     elif request.method == 'GET':
#         form = AuthenticationForm()
#         return render(request,'registration/login.html', context={'form': form})
#     elif request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')      
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 messages.add_message(request, messages.ERROR, 'Invalid email or password')
#                 return redirect(request.path_info)

class LoginView(FormView):
     template_name = 'registration/login.html'
     form_class = AuthenticationForm
     success_url = '/'

     def form_valid(self, form):
         email = self.request.POST.get('email')
         password = self.request.POST.get('password')
         user = authenticate(email=email, password=password)
         if user is not None:
              login(self.request, user)
              return super().form_valid(form)
         
         
     
     

# @login_required
# def Logout(request):
#     logout(request)
#     return redirect('/')

class LogOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     elif request.method == 'GET':
#         form = CustomUserCreation()
#         return render(request,'registration/signup.html', context={'form': form})
#     else:
#             form = CustomUserCreation(request.POST,request.FILES)
#             if form.is_valid():
#                 form.save()
#                 email = request.POST.get('email')
#                 password = request.POST.get('password1')
#                 user = authenticate(email=email, password=password)
#                 login(request,user)
#                 return redirect('/accounts/signup/edit-profile/%i'%request.user.id)

#             else:
#                 messages.add_message(request, messages.ERROR, 'Invalid email or password')
#                 return redirect(request.path_info)
            
class SignUpView(CreateView):
     template_name = 'registration/signup.html'
     form_class = CustomUserCreation
     success_url = '/accounts/login/' #'registration/login' 

     def form_valid(self, form):
        form.save()
        email = self.request.POST.get('email')
        password = self.request.POST.get('password1')   
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request,user)
            return redirect('/accounts/edit-profile/%i'%(user.id-1))
        
     def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid email or password')
        return super().form_invalid(form)

          


class EditProfileView(UpdateView):
    template_name = 'registration/edit_profile.html'
    model = Profile
    fields = [ 'user','first_name', 'last_name', 'image', 'phone', 'address']
    success_url = '/'

            
# def edit_profile(request, pk):
#      if request.method == 'GET':
#           form = EditProfile()
#           return render(request,'registration/edit_profile.html', context={'form': form})
#      elif request.method == 'POST':
#           profile = Profile.objects.get(user=pk)
#           form = EditProfile(request.POST, request.FILES, instance=profile)
#           if form.is_valid():
#                form.save()
#                return redirect('root:home')

            
        

        


# Create your views here.

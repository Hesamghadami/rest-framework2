from typing import Any
from django.db import models
from django.shortcuts import render , get_object_or_404, redirect
from .models import Course, Comment, Category, Reply
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from root.models import NewsLetter
from root.forms import NewsLetterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .cart import Cart

# def courses(request,cat=None,teacher=None):
#     if request.method == 'GET':
#         if cat:
#             course = Course.objects.filter(category__name=cat)
#         elif teacher:
#             course = Course.objects.filter(teacher__info__username=teacher) 

#         elif request.GET.get('search'):
#             course = Course.objects.filter(content__contains=request.GET.get('search')) 

#         else:
#             course = Course.objects.filter(status=True) 


#         course = Paginator(course,2)
#         first_page = 1
#         last_page = course.num_pages
#         try:
#             page_number = request.GET.get('page')
#             course = course.get_page(page_number)

#         except EmptyPage:
#             course = course.get_page(1) 

#         except PageNotAnInteger:
#             course = course.get_page(1) 


#         context ={"courses": course,
#                   'first_page': first_page,
#                   'last_page': last_page,
#         }
#         return render(request,'course/courses.html',context=context)
    
#     elif request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             messages.add_message(request,messages.SUCCESS,'your email submited')
#             return redirect('courses:courses')   
#         else :
#             messages.add_message(request,messages.ERROR,'Invalid email address')
#             return redirect('courses:courses')


# def course_detail(request, id):
#     if request.method == 'GET':
#         try:
#             course = Course.objects.get(id=id)
#             comments = Comment.objects.filter(which_course=id, status=True)
#             reply = Reply.objects.filter(status=True)
#             id_list = []
#             courses = Course.objects.filter(status=True)
#             for cr in courses:
#                 id_list.append(cr.id)   

#             id_list.reverse()

#             if id_list[0] == id :
#                 next_course = Course.objects.get(id = id_list[1])
#                 previous_course = None  

#             elif id_list[-1] == id :
#                 next_course = None
#                 previous_course = Course.objects.get(id = id_list[-2])  

#             else:
#                 next_course = Course.objects.get(id=id_list[id_list.index(id)+1])
#                 previous_course = Course.objects.get(id=id_list[id_list.index(id)-1])   


#             course.counted_views += 1
#             course.save()
#             context ={"course": course,
#                       'next_course': next_course,
#                       'previous_course': previous_course,
#                       'comments': comments,
#                       'reply' : reply,
#             }
#             return render(request,'course/course-details.html',context=context)
#         except:
#             return render(request,'course/404.html')
        
#     elif request.method == 'POST' and len(request.POST) > 2:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'yor comment submited and publish as soon')
#             return redirect (request.path_info)
#         else:
#             messages.add_message(request,messages.ERROR,'yor comment data is not valid')
#             return redirect (request.path_info)
        
#     elif request.method == 'POST' and len(request.POST) == 2:
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             messages.add_message(request,messages.SUCCESS,'your email submited')
#             return redirect(request.path_info)   
#         else :
#             messages.add_message(request,messages.ERROR,'Invalid email address')
#             return redirect(request.path_info)
        

# @login_required
# def delete_comment(request, id):
#     comment = Comment.objects.get(id=id)
#     cid = comment.which_course.id
#     comment.delete()
#     return redirect (f'/courses/course-detail/{cid}')



class DeleteCommentView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = 'course/comment_confirm_delete.html'
    success_url = '/courses/'
 


# @login_required
# def edit(request, id):
#     comment = Comment.objects.get(id=id)
#     if request.method == 'GET':
        

#         context = {
#             'comment' : comment,
#         }
#         return render(request,'course/edit.html',context=context)
    
#     elif request.method == 'POST' :
#         form = CommentForm(request.POST,instance=comment)
#         if form.is_valid():
#             form.save()
#             cid = comment.which_course.id
#             return redirect (f'/courses/course-detail/{cid}')
#         else:
#             messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
#             return redirect (request.path_info)

class CommentEditView(LoginRequiredMixin,UpdateView):
    template_name = 'course/edit.html'
    model = Comment
    fields = ['which_course', 'name', 'email', 'subject', 'message']
    success_url = '/courses/'
    context_object_name = 'comment'


# @login_required
# def reply(request, id):
#     comment = Comment.objects.get(id=id)
#     if request.method == 'GET':
#         form = ReplyForm()

#         context = {
#             'comment' : comment,
#             'form' : form,
#         }
#         return render(request,'course/reply.html',context=context)
    
#     elif request.method == 'POST' :
#         form = ReplyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             cid = comment.which_course.id
#             return redirect (f'/courses/course-detail/{cid}')
#         else:
#             messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
#             return redirect (request.path_info)
        
class ReplyView(LoginRequiredMixin,DetailView):
    template_name = 'course/reply.html'
    model = Comment
    context_object_name = 'comment'

    def post(self, request, *args, **kwargs):
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)



class CourseListView(ListView):
    
    template_name = 'course/courses.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Course.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Course.objects.filter(teacher__info__email = self.kwargs.get('teacher'))
        elif self.request.GET.get('search'):
            return Course.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Course.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = CourseDetailView()
        return post_detail.post(request,*args,**kwargs)
    

    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course-details.html'
    context_object_name = 'course'

    
    def post(self, request, *args, **kwargs):

        cart = Cart(request)

        
        if 'id' in request.POST :
            product = get_object_or_404(Course, id=request.POST['id'])    
            cart.delete_from_cart(product)
            
        else:
            product = get_object_or_404(Course, id=request.POST['pk'], )
            cart.add_to_cart_some_quantity(product, quantity=request.POST['q'])

        return redirect(request.path_info)

    
# class PaymentView(TemplateView):
#     template_name = 'course/cart.html'

def vart(request):
    if request.method == 'GET':
        return render(request, 'course/cart.html')
    elif request.method == 'POST':
        cart = Cart(request)
        cart.clear()
        return render(request, 'course/cart.html')

    







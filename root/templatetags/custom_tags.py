from django import template
from courses.models import Course, Trainer, Category
from root.models import Services
from accounts.models import CustomeUser


register = template.Library()


@register.simple_tag
def last_three_course(number:int):
    last_three = Course.objects.filter(status=True)[:number]
    return last_three


@register.simple_tag
def last_three_trainer():
    last_triner = Trainer.objects.filter(status=True)[:3]
    return last_triner


@register.simple_tag
def category():
    category = Category.objects.all()
    return category

@register.simple_tag
def service():
    service = Services.objects.filter(status=True)
    return service

@register.filter
def truncate(content:str, number:int):
    return content[:number] 

@register.filter
def truncate2(content:str, number:int):
    lst = content.split()[:number]
    lst = " ".join(lst) 
    return lst

@register.inclusion_tag('counter.html')
def counter():
        service_count = Services.objects.filter(status=True).count()
        course_count = Course.objects.filter(status=True).count()
        trainer_count = Trainer.objects.filter(status=True).count()
        user_count = CustomeUser.objects.filter(is_active=True).count()  
        context = {
            'sc' : service_count,
            'cc' : course_count,
            'tc' : trainer_count,
            'uc' : user_count,
        }
        return context
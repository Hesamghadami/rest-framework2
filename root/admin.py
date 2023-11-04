from django.contrib import admin
from .models import Services, NewsLetter, ContactUs

# Register your models here.


class AdminServices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_filter = ['status']
    search_fields = ['title']


admin.site.register(Services,AdminServices)
admin.site.register(NewsLetter)
admin.site.register(ContactUs)
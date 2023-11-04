from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from courses.models import Course

class StaticSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'root:trainer',
            'courses:courses',
        ]
    
    def location(self,item):
        return reverse(item)
    
class DynamicSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Course.objects.filter(status=True)
    
    def location(self,obj):
        return '/courses/course_detail/%s' % obj.id

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from root.sitemap import StaticSiteMap, DynamicSiteMap


sitemaps = {
    'static' : StaticSiteMap,
    'dynamic' : DynamicSiteMap,
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("root.urls")),
    path("courses/",include("courses.urls")),
    path("accounts/",include("accounts.urls")),
    path("accounts/",include("django.contrib.auth.urls")),
    path('robots.txt/', include("robots.urls")),
    path(
    "sitemap.xml/",
    sitemap,
    {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",
),
    path('captcha/', include('captcha.urls')),
    
]



urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)


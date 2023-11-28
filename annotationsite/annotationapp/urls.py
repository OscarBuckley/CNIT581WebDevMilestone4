from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('CNIT581-048-Milestone4', views.video, name='homepage'),
    path('', views.video, name='default'),
    path('annotationList', views.list, name='annotationList'),
    path('video', views.video, name='annotationVideo'),
    path('addAnnotation', views.addAnnotation, name='addAnnotation'),
    path('viewAnnotation', views.viewAnnotation, name='viewAnnotation'),
    path('editAnnotation', views.editAnnotation, name='editAnnotation'),
    path("admin/", admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    # the following three are APIs that return JSON
    path('getAnnotation', views.getAnnotation, name='getAnnotation'),
    path('getChat', views.getChat, name='getChat'),
    path('liveSearch', views.liveSearch, name='liveSearch'),
]

# Login tutorial taken from this site: https://learndjango.com/tutorials/django-login-and-logout-tutorial
# I used BingAI for finding out which django file does what and how to parse Querydict objects (Seriously what the heck were those?)
# Get API from Return Youtube Dislike (https://www.returnyoutubedislike.com/)
# Code from this section and general know how is obtained from https://reintech.io/blog/connecting-to-external-api-in-django
from django.shortcuts import render
from .data import ANNOTATIONS
from django.http import Http404, JsonResponse
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.

def list(request):
    annotations = annotation.objects.all().order_by("timestamp")
    return render(request,"list.html", {"annotations": annotations})

def video(request):
    # Get API from Return Youtube Dislike (https://www.returnyoutubedislike.com/)
    # Code from this section and general know how is obtained from https://reintech.io/blog/connecting-to-external-api-in-django
    apiurl = "https://returnyoutubedislikeapi.com/votes?videoId=eU2NUGRc6XA"
    response = requests.get(apiurl)
    data = response.json()

    annotations = annotation.objects.all()
    chats = chat.objects.all().order_by("posted")
    return render(request,"video.html", {"chats": chats, "api": data})

def addAnnotation(request):

    annotations = annotation.objects.all().order_by("timestamp")

    if request.method=="POST" and request.user.is_authenticated:
        newAnnotation = annotation()
        newAnnotation.timestamp = request.POST.get('timestamp')
        newAnnotation.annotation = request.POST.get('annotation')
        newAnnotation.citation = request.POST.get('citation')
        newAnnotation.author_id = 1
        newAnnotation.save()

    return render(request,"addAnnotation.html", {"annotations": annotations})

def index(request):
    return render(request,"index.html")

def viewAnnotation(request):
    # URL PARAMETERS ARE DEFAULT STRINGS
    id = int(request.GET.get("id", default=None))

    if annotation.objects.filter(id=id).exists():
        annotationSelected = annotation.objects.get(id=id)
        return render(request,"viewAnnotation.html", {"id":id, "annotation":annotationSelected})
    else:
        raise Http404("The requested item cannot be found.")

def editAnnotation(request):
    id = int(request.GET.get("id", default=None))
    annotations = annotation.objects.all().order_by("timestamp")
    # URL PARAMETERS ARE DEFAULT STRINGS
    # according to all online sources this code should work. It's just that SQLite is a piece of shit and can't handle multithreading.
    if request.method=="POST" and request.user.is_authenticated:
        editAnnotation = annotation.objects.get(id=id)
        editAnnotation.timestamp = request.POST.get('timestamp')
        editAnnotation.annotation = request.POST.get('annotation')
        editAnnotation.citation = request.POST.get('citation')
        editAnnotation.save()
        
    if annotation.objects.filter(id=id).exists():
        annotationSelected = annotation.objects.get(id=id)
        return render(request,"editAnnotation.html", {"id":id, "annotation":annotationSelected, "annotations": annotations})
    else:
        raise Http404("The requested item cannot be found.")

# Guide for converting Django Objects into JSON are taken from here https://www.letscodemore.com/blog/object-of-type-queryset-is-not-json-serializable/
def getAnnotation(request):
    annotations = annotation.objects.all().order_by("timestamp")
    annotations = serialize("json", annotations)
    annotations = json.loads(annotations)
    return JsonResponse(annotations, safe=False)

def getChat(request):
    chats = chat.objects.all().order_by("posted")
    chats = serialize("json", chats)
    chats = json.loads(chats)
    return JsonResponse(chats, safe=False)

# I had to use Bing Ai for this one because I needed help with understanding what's even happening in the QueryDict to properly write the code
# Like seriously what the heck was this supposed to mean?
# <QueryDict: {'------WebKitFormBoundaryYh80BHR8A5Bcbz5Z\r\nContent-Disposition: form-data; name': ['"annotationSearch"\r\n\r\nsss\r\n------WebKitFormBoundaryYh80BHR8A5Bcbz5Z--\r\n']}>
# Okay so apparently this thing has like 1 key and 1 value and it's been a clusterfuck trying to untangle this and format it properly. (4 A.M. Oscar Typing this)
@login_required
def liveSearch(request):
    if request.method=="POST":
        raw = request.POST
        for key in raw:
            query = raw[key].split("\r\n")[2]
        annotations = annotation.objects.filter(annotation__contains = query)
        annotations = serialize("json", annotations)
        annotations = json.loads(annotations)
        return JsonResponse(annotations, safe=False)
    else:
        raise Http404("Invalid Operation")

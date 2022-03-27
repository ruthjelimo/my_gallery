from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Author,Image,Location,Category
import datetime as dt


# Create your views here.
def my_gallery(request):
    pub_date= dt.date.today()
    images = Image.objects.all()
    return render(request, 'gallery.html', {"pub_date": pub_date,"images":images})

def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        descrption=request.GET.get("descrption")
        searched_images = Image.search_images_by_location(location)
        message = f"{location}"
        print("Image.......",searched_images)
        return render(request, 'location.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image location"
        return render(request, 'location.html', {"message": message})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_images_by_category(category)
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})
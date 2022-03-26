from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Author,Image,Location,Category


# Create your views here.
def images(request):
    category = Category.get_categories()
    images = Image.all_images()
    location_images = Location.get_location()

    return render(request,'pics.html',{'images': images, 'category': category, 'location_images':location_images })


def single_image(request,id):
    try:
        pic = Image.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_pic.html", {"pic":pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_image = Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_image})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})

def viewImg_by_location(request,location):
    locationimage = Image.view_image_by_location(location)
    return render(request,"location_pics.html",{"locationpic":locationpic})


def viewImg_by_category(request,category):
    photos =Image.view_image_by_category(category)
    return render (request,'category.html',{"photos":photos})
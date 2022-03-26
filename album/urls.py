from django.urls import path,re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.images,name='images'),
    path('single_image/(\d+)',views.single_image,name='single_image'),
    path('search/',views.search_results,name = 'search_results'),
    path('location/(\d+)',views.viewImg_by_location,name='locationimage'),
    path('category/(\d+)',views.viewImg_by_category, name = 'categoryimage')
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
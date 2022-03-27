from django.urls import path,re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.my_gallery, name = 'myGallery'),
    path('search/', views.search_results, name='search_results'),
    path('search/location', views.search_location, name='search_location'),
#     path('search/category',views.search_category, name = 'search_category')
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




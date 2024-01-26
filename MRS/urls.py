from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('movies/', include('movie.urls')),
    path('celebrity/', include('celebrity.urls') ),
    # path(''),
    path('admin/', admin.site.urls),
]
#  admin side titles
admin.site.index_title = "MRS Admin"
admin.site.site_header = "MRS Admin"
admin.site.site_title = "Users"
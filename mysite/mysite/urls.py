"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login', views.loginPage, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logoutPage, name='logout'),
    path('details/<int:property_id>', views.details, name='details'),
    path('search', views.search, name='search'),
    path('place-bid/<int:platform_id>/', views.place_bid, name='place_bid'),
    path('platforms/', include('platforms.urls')),
    path('favorites/add/<int:platform_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorite_list, name='favorites'),
    path('unfavorite/<int:property_id>/', views.unfavorite_property, name='unfavorite_property'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include  
from django.conf import settings
from django.conf.urls.static import static

#from hello_world.Csvs.models import Csvs

#from hello_world.Csvs.models import Csvs
from . import views
#from hello_world.hello_world.settings import MEDIA_URL

urlpatterns = [
path('', views.index,name='Home'),
path('', views.index, name="index"),
path('index', views.index, name="index"),
path('admin/', admin.site.urls),
#path('Csvs/',include("csvs.urls",namespace=csvs)),

path('', include('david.urls'))  ,
path('', include('shop.urls'))  ,
path('shop/',include('shop.urls')),
path('david/',include('david.urls')),
#path('customer/',include('customer.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
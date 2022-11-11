

from django.urls import path, include  
from .import views
from django.contrib import admin
from django.template import loader
urlpatterns = [
  path('', views.index,name='Home'),
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('update/<int:id>', views.update, name='update'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('admin/', admin.site.urls),
]
from django.urls import path
from .views import upload_file_view
from django.contrib import admin

app_name="Csvs"

urlspatterns=[
    path('admin/', admin.site.urls),
    path ("",upload_file_view,name="upload_view"),
    path()
]
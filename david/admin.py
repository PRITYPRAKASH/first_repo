from django.contrib import admin
from .models import sale

from .models import Product # New
# Register your models here.
admin.site.register(Product)  # New

from .models import David
admin.site.register(David)
admin.site.register(sale)
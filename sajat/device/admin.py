from django.contrib import admin

# Register your models here.

from .models import AreaDevice, Dev_attr, Dev_attr_float, Dev_attr_char

admin.site.register(AreaDevice)
admin.site.register(Dev_attr)
admin.site.register(Dev_attr_float)
admin.site.register(Dev_attr_char)
from django.contrib import admin
from .models import Phone, Samsung, Apple
# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
  list_display = ('brand', 'model', 'storage_capacity', 'color')

class SamsungAdmin(admin.ModelAdmin):
  pass

class AppleAdmin(admin.ModelAdmin):
  pass

admin.site.register(Phone, PhoneAdmin)
admin.site.register(Samsung, SamsungAdmin)
admin.site.register(Apple, AppleAdmin)
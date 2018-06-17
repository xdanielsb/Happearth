from django.contrib import admin
from house.models import House
# Register your models here.
class HouseAdmin(admin.ModelAdmin):
  pass

admin.site.register(House, HouseAdmin)

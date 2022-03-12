from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main_app.models import *

# Register your models here.

@admin.register(Maqola)
class Maqola_admin(ModelAdmin):
    pass

@admin.register(Images)
class Image_admin(ModelAdmin):
    pass

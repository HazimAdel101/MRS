from django.contrib import admin
from .models import Celebrity
# Register your models here.



class CelebrityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Celebrity, CelebrityAdmin)
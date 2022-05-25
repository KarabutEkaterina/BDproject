from django.contrib import admin
from .models import Task, Place, Reviews, Cuisine, Grade

# Register your models here.


admin.site.register(Task)
admin.site.register(Place)
admin.site.register(Reviews)
admin.site.register(Cuisine)
admin.site.register(Grade)


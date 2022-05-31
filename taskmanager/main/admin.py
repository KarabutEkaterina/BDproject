from django.contrib import admin
from .models import Task, Place, Reviews, Cuisine, Grade, Services, Event, Menu, UserProfile

# Register your models here.


admin.site.register(Task)
admin.site.register(Place)
admin.site.register(Reviews)
admin.site.register(Cuisine)
admin.site.register(Grade)
admin.site.register(Services)
admin.site.register(Event)
admin.site.register(Menu)
admin.site.register(UserProfile)


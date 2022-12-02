from django.contrib import admin
from .models import Category, State, Iso, Site, Region
# Register your models here.
admin.site.register(Category)
admin.site.register(Site)
admin.site.register(State)
admin.site.register(Iso)
admin.site.register(Region)

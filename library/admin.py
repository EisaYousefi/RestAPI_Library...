from django.contrib import admin

# Register your models here.
from .models import Books,Azo,Amanat

admin.site.register(Books)
admin.site.register(Azo)
admin.site.register(Amanat)
from django.contrib import admin
from .models import Customer
from .models import ModelFile

admin.site.register(Customer)
admin.site.register(ModelFile)
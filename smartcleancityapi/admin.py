from django.contrib import admin
from . models import User, Complaint, Bin
# Register your models here.

admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(Bin)


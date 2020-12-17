from django.contrib import admin
from home.models import Contact, Library, category, signup

# Register your models here.
admin.site.register(Contact)
admin.site.register(category)
admin.site.register(Library)
admin.site.register(signup)
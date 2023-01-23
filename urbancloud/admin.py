from django.contrib import admin
from urbancloud.models import Contactus
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'name','email')

admin.site.register(Contactus,AuthorAdmin)



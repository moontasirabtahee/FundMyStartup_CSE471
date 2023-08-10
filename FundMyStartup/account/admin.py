from django.contrib import admin
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccounInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profile'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccounInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)


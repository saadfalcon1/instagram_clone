from django.contrib import admin
from .models import User, UserConfirmation


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'id']


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation)

from django.contrib import admin
from .models import UserBase

# Register your models here.


class UserbaseAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_created', 'last_login', 'is_active')
    exclude = ('password', 'groups', 'user-permissions')
    readonly_fields = ('email', 'username', 'first_name',
                       'last_name',  'phone_number', 'last_login', 'is_active')
    search_fields = ('email', 'first_name','last_name', 'username')

    ordering = ('-date_created',)


admin.site.register(UserBase, UserbaseAdmin)

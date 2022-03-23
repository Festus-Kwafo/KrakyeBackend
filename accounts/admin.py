from django.contrib import admin
from .models import UserBase

# Register your models here.


class UserbaseAdmin(admin.ModelAdmin):
    exclude = ('password', 'groups', 'user-permissions')
    readonly_fields = ('email', 'username', 'first_name',
                       'other_name', 'country', 'phone_number', 'postcode', 'address_line_1', 'address_line_2', 'town_city')


admin.site.register(UserBase, UserbaseAdmin)

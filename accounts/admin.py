from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from accounts.forms import UserCreationFormExtended

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2','email',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

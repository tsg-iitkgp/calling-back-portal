from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm


from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    list_display = ['username', 'email', 'role', 'hall', 'department', 'is_superuser']
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("username", "password1", "password2", "role", 'hall', 'department'),
                },
            ),
        )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
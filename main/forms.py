from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__' # UserCreationForm.Meta.fields + ('role', 'department', 'hall')

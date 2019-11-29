from django.forms import ModelForm

from HSSapp.models import User


class RegForm(ModelForm):
    class Meta():
        model=User
        fields=['username','password','email','phone','state','district','area']
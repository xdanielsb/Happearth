
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=("E-mail"), max_length=75)



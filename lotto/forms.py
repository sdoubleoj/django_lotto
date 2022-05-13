from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta: #ModelForm > class Meta > model & fields는 약속된 양식!!
        model = GuessNumbers
        fields = ('name','text')
            #GuessNumbers의 name과 test열만 받아들임, 항상 튜플로!

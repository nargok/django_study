from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
  find = forms.CharField(label='Find', required=False)

class HelloForm(forms.Form):
  name = forms.CharField(label='Name')
  mail = forms.EmailField(label='Email')
  gender = forms.BooleanField(label='Gender', required=False)
  age = forms.IntegerField(label='Age')
  birthday = forms.DateField(label='Birth')
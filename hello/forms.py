from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
  find = forms.CharField(label='Find', required=False)

class CheckForm(forms.Form):
  # 文字列
  # empty = forms.CharField(label="Empty", empty_value=True)
  # min = forms.CharField(label="Min", min_length=10)
  # max = forms.CharField(label="Max", max_length=10)

  # 整数値
  # required = forms.IntegerField(label="Required")
  # intMin = forms.IntegerField(label="intMin", min_value=100)
  # intMax = forms.IntegerField(label="intMax", max_value=1000)

  # 日付、時刻
  # date = forms.DateField(label="Date", input_formats=['%d'])
  # time = forms.TimeField(label="Tiem")
  # datetime = forms.DateTimeField(label="DateTiem")

  # validation error
  str =  forms.CharField(label="String")

  # clean メソッドで値の検証をする
  def clean(self):
    cleaned_data = super().clean()
    str = cleaned_data['str']
    if (str.lower().startswith('no')):
      raise forms.ValidationError('You input "No"!')


class HelloForm(forms.Form):
  name = forms.CharField(label='Name')
  mail = forms.EmailField(label='Email')
  gender = forms.BooleanField(label='Gender', required=False)
  age = forms.IntegerField(label='Age')
  birthday = forms.DateField(label='Birth')
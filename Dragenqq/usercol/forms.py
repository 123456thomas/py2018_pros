from django import forms

class Userform(forms.Form):
    username = forms.CharField(max_length=20, min_length=2,label='姓名')
    email = forms.EmailField(label='邮箱')
    age = forms.IntegerField(max_value=130,label='年龄')
    pwd = forms.CharField(max_length=40,label='密码')
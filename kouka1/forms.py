from cProfile import label
import email
import os
from email import message
from turtle import title
from unicodedata import name
from django import forms
from django.core.mail import EmailMessage

class Kouka1Form(forms.Form):
    name = forms.TextField(label='お名前', max_length=30)
    age = forms.IntegerField(label='年齢')
    number = forms.TextField(label='電話番号', max_length=11)
    email = forms.EmailField(label='メールアドレス')
    address = forms.TextField(label='住所', maxlength=100)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢をここに入力してください。'
        
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'
        
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = '住所をここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        age = self.cleaned_data['age']
        number = self.cleaned_data['number']
        email = self.cleaned_data['email']
        address = self.cleaned_data['address']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name,email,message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
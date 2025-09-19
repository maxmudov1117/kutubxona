from django import forms
from main.models import *


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'
        widgets = {
            'tugilgan_sana': forms.DateInput(attrs={'type': 'date'})
        }


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'olingan_sana': forms.DateInput(attrs={'type': 'date'}),
            'qaytatrish_sanasi': forms.DateInput(attrs={'type': 'date'})
        }


class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = '__all__'


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

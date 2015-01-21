from joins.models import Join

__author__ = 'k1'
from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()


class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email', ]
        exclude = ['ip_address',]
from django import forms

class OrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

from django import forms

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = ['adress', 'name', 'phone']


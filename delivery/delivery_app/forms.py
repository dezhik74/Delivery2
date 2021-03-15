from django import forms


class DeliveryForm(forms.Form):
    address = forms.CharField(label='Адрес доставки',
                              widget=forms.Textarea(attrs={'class': 'form-address-input', 'rows': '3'}))
    phone = forms.CharField(label='Телефон для связи', max_length=20)
    name = forms.CharField(label='Имя', max_length=20)
    comment = forms.CharField(label='Комментарий',
                              widget=forms.Textarea(attrs={'class': 'form-address-input', 'rows': '3'}),
                              required=False)

    phone.widget.attrs.update({'class': 'form-address-input'})
    name.widget.attrs.update({'class': 'form-address-input'})




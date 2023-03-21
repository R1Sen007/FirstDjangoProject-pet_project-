from django import forms
from django.contrib.admin import widgets, site as admin_site
from .models import Shop


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'adress',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['adress']:
            self.fields[field].widget.attrs.update({'onchange':'createNewObject();'})


class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'adress',
            'image',
        ]


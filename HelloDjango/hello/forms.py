from django import forms
from django.contrib.admin import widgets, site as admin_site
from .models import Person, Shop

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
#     password = forms.CharField(widget= forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'age'
        ]

class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'adress'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['adress']:
            self.fields[field].widget.attrs.update({'onchange':'createNewObject();'})
            
            

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in ['adress']:
    #         self.fields[field].widget = widgets.RelatedFieldWidgetWrapper(
    #             self.fields[field].widget,
    #             self.instance._meta.get_field(field).remote_field,
    #             admin_site
    #         )
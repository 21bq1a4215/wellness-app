from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django.forms import Textarea
from .models import Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        widgets = {
            'review': Textarea(attrs={'cols': 7, 'rows': 7}),
        }
        fields = ['subject', 'review', 'rate']
        labels = {
            'rate': 'Choose your rating'
        }

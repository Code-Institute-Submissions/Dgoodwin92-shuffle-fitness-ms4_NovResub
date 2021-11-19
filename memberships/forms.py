from django import forms
from .models import Membership, Category


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_name = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

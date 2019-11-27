from django import forms
#from uploads.core.models import Document

#class DocumentForm(forms.ModelForm):
#    class Meta:
#        model = Document
#        fields = ('description', 'document', )
        
# from upload form
from .models import Book, Profile, UserProfile
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
#        fields = ('title', 'author', 'pdf', 'cover')
#        fields = ('title', 'pdf', 'category', 'desc','price', 'price_exclusive', 'minutes_exclusive', 'incident_date','country')
        fields = ('title', 'pdf', 'category', 'desc','price', 'price_exclusive', 'minutes_exclusive','incident_date','country')
#################

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
#        fields = ('title', 'author', 'pdf', 'cover')
#        fields = ('title', 'pdf', 'category', 'desc','price', 'price_exclusive', 'minutes_exclusive', 'incident_date','country')
        fields = ('type_news','web', 'alt_email', 'country')
#################


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)


    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('type_news','web', 'alt_email', 'country')
#################
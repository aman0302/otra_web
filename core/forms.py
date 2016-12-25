from django import forms
from .models import Register, Request

class RequestForm(forms.ModelForm):

    class Meta:
        model=Request
        fields=['company_name', 'contact_person', 'contact_number', 'contact_email', 'budget', 'duration', 'need_design']
        labels = {
            "need_design":"Do you need to get your vinyl designed as well?"
        }

        widgets = {
            'contact_number': forms.NumberInput(attrs={'max': 9999999999, 'min': 7000000000})
        }


    '''
    company_name =forms.CharField(label='Company Name',max_length=128)
    contact_person=forms.CharField(max_length=128 )
    contact_number=forms.IntegerField()
    contact_email=forms.EmailField(max_length=128, required=False)
    budget=forms.IntegerField( required=False)
    duration=forms.IntegerField(required=False )
    need_design=forms.BooleanField(initial=False, required=False)
    '''
    
    
class RegisterForm(forms.ModelForm):

    class Meta:
        model=Register
        fields=['name','contact_number','car_model','commercial_or_private']
        labels ={
            'contact_number':'Contact Mobile Number +91 '
        }

        widgets={
            'contact_number':forms.NumberInput(attrs={'max':9999999999,'min':7000000000})
        }

    '''
    name =forms.CharField(max_length=128)
    contact_number =forms.IntegerField( )
    car_model =forms.CharField(max_length=128, required=False )
    commercial_or_private = forms.CharField(max_length=64, required=False)
    '''
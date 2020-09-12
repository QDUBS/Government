from django import forms
from django.forms import ModelForm
from .models import Visitor



GENDER_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
)

STATE_CHOICES = (
    ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'),
    ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'),
    ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'),
    ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'),
    ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'),
    ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'),
    ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'),
    ('Nassarawa', 'Nassarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'),
    ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'),
    ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'),
    ('F.C.T', 'F.C.T')
)

STATUS_CHOICES = (
    ('Checked In', 'Checked In'),
    ('Checked Out', 'Checked Out'),
)

class VisitorRegForm(forms.ModelForm):
    gender = forms.ChoiceField(choices = GENDER_CHOICES, widget=forms.Select(attrs={'style': 'width:500', 'placeholder': 'Gender'}))
    state = forms.ChoiceField(choices = STATE_CHOICES, widget=forms.Select(attrs={'style': 'width:500', 'placeholder': 'State'}))
    #location_visited = forms.ChoiceField(choices = GENDER_CHOICES, widget=forms.SelectMultiple(attrs={'style': 'width:500', 'placeholder': 'Location'}))
    status = forms.ChoiceField(choices = STATUS_CHOICES)

    class Meta:
        model = Visitor
        fields = ['firstname', 'lastname', 'middlename', 'birth_date', 'gender', 'phone', 'address', 'city_town', 'state', 'tag_no', 'purpose_of_visit', 'location_visited', 'status']

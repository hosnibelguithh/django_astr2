from ast import Not
from dataclasses import fields
from django import forms
from accounts.models import User
from .models import Prospect



from django.forms import ModelForm, DateInput
from .models import Event

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Prospect
        exclude = ['Agent']
        fields = '__all__'


class LeadModelAdminForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = '__all__'
    def __init__(self, *args, **kwargs):
      super(LeadModelAdminForm, self).__init__(*args, **kwargs)
      self.fields['Agent'].queryset = User.objects.filter(is_agent = True)

class LeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Prospect
        
        fields = [
          'status',
          'Agent',
        ]
    def __init__(self, *args, **kwargs):
        super(LeadUpdateForm, self).__init__(*args, **kwargs)
        self.fields['Agent'].queryset = User.objects.filter(is_agent = True)

class LeadUpdateFormUser(forms.ModelForm):
    class Meta:
        model = Prospect
        
        fields = [
          'status',
        ]
    def __init__(self, *args, **kwargs):
        super(LeadUpdateFormUser, self).__init__(*args, **kwargs)
    









from django.forms import ModelForm, DateInput
from .models import Event

YEARS= [x for x in range(2022,2030)]


class EventForm(ModelForm):
  Prospect = forms.ModelChoiceField(
        queryset=Prospect.objects.none()
    )
  Proposition = forms.BooleanField(required=False)

  class Meta:
    model = Event
    

    fields = '__all__'
    
  def __init__(self,*args,**kwargs):
    user = kwargs.pop('Agent')

    forms.ModelForm.__init__(self, *args, **kwargs)
    self.fields['Prospect'].queryset = Prospect.objects.filter(Agent = user)
   
 
    

class EventFormAdmin(ModelForm):

  class Meta:
    model = Event
    fields = '__all__'
    
    #DateDeProspection = forms.DateField(label='DateDeProspection', widget=forms.SelectDateWidget(years=YEARS))
  def __init__(self, *args, **kwargs):
    super(EventFormAdmin, self).__init__(*args, **kwargs)

    # input_formats parses HTML5 datetime-local input to datetime field
    #self.fields['Agent'].queryset = User.objects.filter(is_agent = True)
    #self.fields['DateDeProspection'].input_formats = ('%Y-%m-%dT%H:%M',)

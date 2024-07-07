from django.forms import ModelForm, EmailInput

from personas.models import Persona

#referencias de widgets a utilizar
#https://docs.djangoproject.com/en/3.0/ref/forms/widgets/

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs = {'type':'email'})
        }
from django import forms
from material import Layout, Fieldset, Row, Span6

from danibraz.persons.models import Client
#from danibraz.users.models import User
#type="text" class="form-control"

class PersonsForm(forms.ModelForm):
    name = forms.CharField(label='Nome', required=True)
    birthday = forms.DateField(label='Nascimento', required=False)
    address = forms.CharField(label='Endereço completo')
    purchase_limit = forms.DecimalField(label='Limite de compra')
    compra_sempre = forms.BooleanField(label='Compra sempre?', required=False)

    class Meta:
        model = Client
        fields = '__all__'


from crispy_forms import layout
from django.forms.models import formset_factory
from django import forms
from django.forms import ModelForm, Field
from viewform import Span6

from danibraz.persons.models import Client, Author, Book, Employee

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row


class ClientsForm(forms.ModelForm):
    name = forms.CharField(label='Nome', required=True)
    birthday = forms.DateField(label='Nascimento', required=False)
    address1 = forms.CharField(label='Endereço completo')
    purchase_limit = forms.DecimalField(label='Limite de compra')
    compra_sempre = forms.BooleanField(label='Compra sempre?', required=False)

    class Meta:
        model = Client
        fields = '__all__'

    layout = Layout(
        Fieldset("Inclua um cliente",
                 Row('name', ),
                 Row('birthday','purchase_limit'),
                 Row('address1', ),
                 Row('compra_sempre', ),
                 )
    )


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(label='Nome', required=True)
    birthday = forms.DateField(label='Nascimento', required=False)
    address1 = forms.CharField(label='Endereço completo')
    purchase_limit = forms.DecimalField(label='Limite de compra')
    ctps = forms.CharField(label='Carteira de trabalho', required=False)
    salary = forms.DecimalField(label='Salário')

    class Meta:
        model = Employee
        fields = '__all__'

    layout = Layout(
        Fieldset("Inclua um funcionário",
                 Row('name', ),
                 Row(Span6('birthday'), Span6('ctps'), ),
                 Row(Span6('purchase_limit'),Span6('salary'),),
                 Row('address1', ),
                 )
    )


"""----------------------------------------------------------------------------------"""


class AuthorForm(ModelForm):
    name = forms.CharField(label='Nome do Autor', required=False)


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row('name', 'title_author'),
        )
        super(AuthorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )

        super(BookForm, self).__init__(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.form_tag = False
    #     self.helper.layout = Layout(
    #         Field('title'),
    #     )
    #     super(BookForm, self).__init__(*args, **kwargs)

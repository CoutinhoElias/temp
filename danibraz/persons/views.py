import extra_views
from django.forms import inlineformset_factory
from material import *
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.

from danibraz.persons.forms import ClientsForm, EmployeeForm, BookForm, AuthorForm
from danibraz.persons.models import Address, Person, Author, Book
from danibraz.static.material import Inline


class ItemInline(extra_views.InlineFormSet):
    model = Address #Model Address
    fields = '__all__'
    # Desnecessário
    #fields = ['id', 'qualificacao', 'campo_novo_um', 'campo_novo_dois', 'campo_novo_tres'] #Campos do endereço

    #Desnecessário
    # layout = Layout(
    #     # Campos do Persons
    #     Row('qualificacao', 'campo_novo_um'),
    #     Row('campo_novo_dois', 'campo_novo_tres'),
    #
    # )
    extra = 3# Define aquantidade de linhas a apresentar.

##
from django import forms
class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    layout = Layout(
        Fieldset("Inclua uma Pessoa",
                 Row('name', ),
                 Row('birthday','address1'),
                 Row('purchase_limit'),
                 ),
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    layout = Layout(
        # Campos do Persons
        Fieldset("Inclua os Endereços",
                 Row('kynd', ),
                 Row('public_place','number'),
                 Row('city','state', ),
                 Row('zipcode', 'country', ),
                 Row('phone', ),
                 ),
    )

class AddressQInline(extra_views.InlineFormSet):
    model = Address  # Model Address
    # form_class = AddressForm
    # fields = '__all__'
    fields = ['kynd', 'public_place', 'number', 'city', 'state', 'zipcode', 'country', 'phone', ]
    extra = 1
    can_delete = False
#

class NewProfissoesPessoaView(
                       extra_views.NamedFormsetsMixin,
                       extra_views.CreateWithInlinesView):
    model = Person
    form_class = PersonModelForm
    inlines = [AddressQInline]
    inlines_names = ['endereco_inline']
    template_name = "persons/form_create_person_address.html"
    success_url = reverse_lazy("home")

    def get_success_url(self):
        sucess_url = super().get_success_url()
        print("Objeto salvo:")
        print(self.object)
        return sucess_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class NewProfissoesPessoaView(LoginRequiredMixin,
#                               LayoutMixin,
#                       extra_views.NamedFormsetsMixin,
#                       extra_views.CreateWithInlinesView):
#
#     title = "Novo Cliente"
#     model = Person # model Person
#
#     #print('Chegou na linha 334')
#
#     layout = Layout(
#         # Campos do Persons
#         Fieldset("Inclua um cliente",
#                  Row('name', ),
#                  Row('birthday','purchase_limit'),
#                  Row('address1', ),
#                  ),
#         #Inline dos endereços
#         Inline('Endereços', ItemInline),
#     )
#     #print('Chegou na linha 340')
#
#     def forms_valid(self, form, inlines):
#         self.object = form.save(commit=False)
#         #self.object.pessoa_id = self.request.user.id
#         self.object.save()
#         return super(NewProfissoesPessoaView, self).forms_valid(form, inlines)
#
#     def get_success_url(self):
#         return self.object.get_absolute_url()


def clients(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('/reserva/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'persons/person.html', {'form':form})
    else:
        context = {'form': ClientsForm()}
        return render(request, 'persons/person.html', context)

# def scheduling_edit(request, id_booking):
#     booking = Booking.objects.get(id=id_booking)
#     if request.method == 'GET':
#         form = BookingsForm(instance=booking)
#     else:
#         form = BookingsForm(request.POST, instance=booking)
#         if form.is_valid():
#             new = form.save(commit=False)
#             new.save()
#             form.save_m2m()
#         return HttpResponseRedirect('/reserva/listagem/')
#     return render(request, 'bookings/scheduling_form.html', {'form': form})


def employees(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('/reserva/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'persons/person.html', {'form':form})
    else:
        context = {'form': EmployeeForm()}
        return render(request, 'persons/person.html', context)


"""--------------------------------------------------------------------------------------------------"""

class AddressInline(extra_views.InlineFormSet):
    model = Address #Model Address
    # Desnecessário
    #fields = ['kynd', 'public_place', 'number', 'city', 'state', 'zipcode', 'country', 'phone', 'delete'] #Campos do endereço

    #Desnecessário
    # layout = Layout(
    #     # Campos do Persons
    #     Row('qualificacao', 'campo_novo_um'),
    #     Row('campo_novo_dois', 'campo_novo_tres'),
    #
    # )
    # extra = 3# Define aquantidade de linhas a apresentar.
    can_delete = True


#LoginRequiredMixin faz a mesma função de @login_required(login_url=LOGIN_URL). a ndiferença que LoginRequiredMixin não precisa apontar na url
class NewCadastroPessoaView(LayoutMixin,
                      extra_views.NamedFormsetsMixin,
                      extra_views.CreateWithInlinesView):
    title = "Nova Pessoa"

    model = Person# model Person

    layout = Layout(
        # Campos do Persons
        Fieldset("Inclua uma pessoa",
                 Row('name', ),
                 Row('birthday','purchase_limit'),
                 Row('address1', ),
                 ),
        #Inline dos endereços
        Inline('Endereços', AddressInline,),

    )

    #print('Chegou na linha 340')

    def forms_valid(self, form, inlines):
        self.object = form.save(commit=False)
        #self.object.pessoa_id = self.request.user.id
        self.object.save()
        return super(NewCadastroPessoaView, self).forms_valid(form, inlines)

    def get_success_url(self):
        return self.object.get_absolute_url()
"""--------------------------------------------------------------------------------------------------"""

# class FormsetView(LayoutMixin,
#                 extra_views.NamedFormsetsMixin,
#                 extra_views.CreateWithInlinesView):
#     model = Shipment
#
# class ItemInline(extra_views.InlineFormSet):
#     model = ShipmentItem
#     fields = ['name', 'quantity']
#
#     layout = Layout(
#         Row(Column('name', 'city'),
#         Column('address_line1', 'address_line2')),
#     Inline('Items', ItemInline)
#     )

def manage_books(request, id_author=None):
    if id_author is None:
        author = Author()
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=False)
    else:
        author = Author.objects.get(pk=id_author)
        BookInlineFormSet = inlineformset_factory(Author, Book, form=BookForm, extra=3, can_delete=False)

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author, prefix="main")
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('/cadastro/bookauthor/')
    else:
        form = AuthorForm(instance=author, prefix="main")
        formset = BookInlineFormSet(instance=author, prefix="nested")

    return render(request, "persons/manage_books.html", {"form": form, "formset": formset})
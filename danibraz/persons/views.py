from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from danibraz.persons.forms import PersonsForm


def persons(request):
    if request.method == 'POST':
        form = PersonsForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('/reserva/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'persons/client.html', {'form':form})
    else:
        context = {'form': PersonsForm()}
        return render(request, 'persons/client.html', context)



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

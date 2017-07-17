from django.contrib import admin

# Register your models here.
from danibraz.persons.models import Client, Employee, Person


class PersonModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonModelAdmin)


class ClientModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientModelAdmin)

class EmployeeModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeModelAdmin)
# from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    # class Meta:
    #     abstract = True

    name = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    purchase_limit = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'

    def __str__(self):
        return self.name

    def get_child(self):
        if hasattr(self, 'client'):
            return self.client
        elif hasattr(self, 'employee'):
            return self.employee
        else:
            return None

    def get_type(self):
        if hasattr(self, 'client'):
            return 'client'
        elif hasattr(self, 'employee'):
            return 'employee'
        else:
            return None


class Client(Person):
    compra_sempre = models.BooleanField(default=False)
    # person = models.ForeignKey('persons.Person', verbose_name='Pessoa', related_name='Person')
    def save(self, *args, **kwargs):
        # self.operacao = CONTA_OPERACAO_DEBITO
        super(Client, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'



class Employee(Person):
    ctps = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=15, decimal_places=2)


    def save(self, *args, **kwargs):
        # self.operacao = CONTA_OPERACAO_DEBITO
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

from django.db import models

from PetClinicAPI.resources.base_model import BaseModel
from client.models import Pet

class Veterinary(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    phone = models.CharField(max_length=255, verbose_name='Telefone')

    class Meta:
        app_label = 'clinic'

class Drug(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Nome')

    class Meta:
        app_label = 'clinic'

class Appointment(BaseModel):
    date = models.DateField(verbose_name='Data')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    diagnosis = models.TextField(verbose_name='Diagnóstico', null=True, blank=True)
    drugs = models.ManyToManyField(Drug, verbose_name='Remédios', null=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Paciente')
    veterinary = models.ForeignKey(Veterinary, on_delete=models.CASCADE, related_name='appointments', verbose_name='Veterinário')

    class Meta:
        app_label = 'clinic'
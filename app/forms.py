from django.forms import ModelForm, ValidationError
from app.models import Lab
from app.utils import validateCPF


class LabForm(ModelForm):
     class Meta:
         model = Lab
         fields = ['nome', 'sobrenome', 'idade', 'cpf', 'cidade', 'estado', 'celular']

     def clean_cpf(self):
         cpf = self.cleaned_data['cpf']
         cpf_valido = validateCPF(cpf)
         print(cpf_valido)
         if not cpf_valido:
             raise ValidationError("CPF INVÁLIDO")
         return cpf

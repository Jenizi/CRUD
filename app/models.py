from django.db import models


CHOICES = [('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('MG', 'Minas Gerais'),
    ('RJ', 'Rio de Janeiro'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('PA', 'Pará'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RO', 'Rondônia'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('MS', 'Mato Grosso do Sul'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('AP', 'Amapá'),
    ('MT', 'Mato Grosso'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('RR', 'Roraima')]


class Lab(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=CHOICES)
    celular = models.CharField(max_length=9, blank=True, null=True)

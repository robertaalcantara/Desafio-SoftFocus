from datetime import date
from django.db import models


class Comunicacao(models.Model):
    '''description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()'''

    EVENTOS = (
        ('chuva', 'Chuva Excessiva'),
        ('geada', 'Geada'),
        ('granizo', 'Granizo'),
        ('seca', 'Seca'),
        ('vendaval', 'Vendaval'),
        ('raio', 'Raio'),
    )

    nome_produtor = models.CharField(max_length=30, default='')
    email_produtor = models.EmailField(max_length=50, default='')
    cpf_produtor = models.CharField(max_length=14, default='')
    latitude_lavoura = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    longitude_lavoura = models.DecimalField(max_digits=11, decimal_places=8, default=0)
    tipo_lavoura = models.CharField(max_length=20, default='')
    data_colheita = models.DateField(default=date.today)
    evento = models.CharField(max_length=15, choices=EVENTOS, default='chuva')

    def __unicode__(self):
        return '{} {} {} {}'.format(self.nome_produtor, self.cpf_produtor, self.data_colheita, self.evento)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nome_cat=models.CharField(max_length=100,verbose_name="Nome")
    descr_cat=models.TextField(verbose_name="Descriçao")
    def __str__(self):
        return self.nome_cat
    

class Tipo(models.Model):
    tipo=models.fields.CharField(max_length=50)
    def __str__(self):
        return self.tipo
    
   

class Pagamento(models.Model):
    nome_pag=models.CharField(max_length=100,verbose_name="descricao")
    descr_pag=models.TextField(verbose_name="Observação", blank=True,null=True)
    valor_total=models.fields.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor total",help_text="Valor total associado")
    Data_pag=models.fields.DateField(verbose_name="Data Pagamento",help_text="Data de vencimento ou pagamento")
    tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE)
    pago=models.fields.BooleanField(default=False)

    def __str__(self):
        return self.nome_pag
    


class Cartao(models.Model):
    nome_ca=models.fields.CharField(max_length=80, verbose_name="Nome Cartao")
    def __str__(self) :
        return self.nome_ca



class Gasto(models.Model):
    nome_gc =models.fields.CharField(max_length=100, verbose_name="Nome")
    data_gc=models.fields.DateField(verbose_name="Data" )
    valor_gc= models.fields.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor")
    cartao= models.ForeignKey(Cartao ,on_delete=models.CASCADE,blank=True, null=True,help_text="Somente preencher se for usado crédito.")
    categoria =models.ForeignKey(Categoria,on_delete=models.CASCADE,help_text="Classificar o tipo de gasto")
    pagamento=models.ForeignKey(Pagamento,on_delete=models.CASCADE,help_text="Qual centro de pagamento está associado")

    def __str__(self):
        return self.nome_gc
    

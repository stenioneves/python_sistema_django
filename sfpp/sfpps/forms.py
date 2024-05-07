from django import forms
from .models import Gasto,Pagamento


class GastoForm( forms.ModelForm):
    class Meta:
        model= Gasto
        fields=['nome_gc','valor_gc','data_gc','categoria','cartao','pagamento']


class PagamentoForm(forms.ModelForm):
    class Meta:
        model=Pagamento
        fields=[
            'nome_pag',
            'valor_total',
            'Data_pag',
            'descr_pag',
            'tipo',
            'pago'

        ]
    

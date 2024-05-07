from django.urls import path
from .views import AdicionarGastorView,AdicionarPagamentoView,ListarPagamentosView
#importe suas views
#URL para apontar a sua view
urlpatterns = [
    path('gerenciar/gastos/adicionar/', view=AdicionarGastorView.as_view(),name='adicionar_gasto'),
    path('gerenciar/pagamentos/adicionar/', view=AdicionarPagamentoView.as_view(), name='adicionar_pagamento'),
    path('gerenciar/pagamentos/listar',view=ListarPagamentosView.as_view(),name='listar_pagamentos')
]

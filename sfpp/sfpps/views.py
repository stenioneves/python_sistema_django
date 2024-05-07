from django.shortcuts import render,redirect
from django.views import View
from .forms import GastoForm, PagamentoForm
from .models import Pagamento,Gasto

# Create your views here.


class AdicionarGastorView(View):
     template_name ="gastos/adicionar.html"
     def get(self,request):
          form =GastoForm()
          return render(request, self.template_name,{'form':form})

class AdicionarPagamentoView(View):
     template_name='pagamentos/adicionar.html' 
     def get(self, request):
          form=PagamentoForm()
          return render(request,self.template_name,{'form':form}) 

class ListarPagamentosView(View):
     template_name='pagamentos/listar_pagamentos.html' 
     def get(self, request):
        pagamentos= Pagamento.objects.get_queryset()
        return render(request,self.template_name,{'pagamentos':pagamentos})     
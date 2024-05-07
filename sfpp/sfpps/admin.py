from django.contrib import admin
from .models import Categoria,Tipo,Pagamento,Gasto,Cartao

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Pagamento)
admin.site.register(Gasto)
admin.site.register(Cartao)
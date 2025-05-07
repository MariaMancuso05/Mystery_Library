from django.contrib import admin

# Register your models here.
from .models import Libreria,Categoria,Trame, Store, Autori, Votazione, Acquisti, Profilo, CartaFittizia
admin.site.register(Libreria)
admin.site.register(Categoria)
admin.site.register(Trame)
admin.site.register(Store)
admin.site.register(Autori)
admin.site.register(Votazione)
admin.site.register(Acquisti)
admin.site.register(Profilo)
admin.site.register(CartaFittizia)

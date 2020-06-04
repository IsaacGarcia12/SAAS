from django.contrib import admin
from .models import Secuencia, Blast, Cath, InterPro, Clustal

admin.site.register(Secuencia)
admin.site.register(Blast)
admin.site.register(Cath)
admin.site.register(InterPro)
admin.site.register(Clustal)
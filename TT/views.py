#Modulos de django
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Secuencia
from .forms import IngresarForm

#Modulos de python generales
import os
import subprocess
from io import StringIO
import sys
import time

#Modulos de biopython
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def Funcionamiento(request):
    cadena = request.POST.get('cadena')
    mail = request.POST.get('mail')
    nombre = request.POST.get('nombre')

    #Aqui mandamos a llamar a blast
    #record = SeqIO.read(cad, format="fasta")
    result_handle = NCBIWWW.qblast("blastp", "nr", cadena.format("fasta"))
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    with open('/home/isaac/Escritorio/SAmin/TT/salida'+moment+'.xml', 'w') as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    pipe = subprocess.Popen(["perl", "/home/isaac/Escritorio/SAmin/TT/cath.pl", cadena], stdin=subprocess.PIPE)
    pi   = subprocess.Popen(['python', '/home/isaac/Escritorio/SAmin/TT/interpro.py', '--email', mail, cadena])
                                        
    #mandamos a llamar a clustal: Modificar para que reciba ambas cadenas
    #pi = subprocess.Popen(['python', '/home/isaac/Escritorio/SAmin/TT/interpro.py', '--email', mail, cadena])
    cadena_obj = Secuencia(Secuencia = cadena, Nombre = nombre, Correo = mail)
    cadena_obj.save()
    return render(request, 'TT/cadena.html', {'cadena':cadena})

def crearPDF(request):
    return render(request, 'TT/generarPDF.html')

def index(request):
    return render(request, 'TT/index.html')

def about(request):
    return render(request, 'TT/about.html')

def contacto(request):
    return render(request, 'TT/contacto.html')
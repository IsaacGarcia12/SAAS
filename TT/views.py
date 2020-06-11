#Modulos de django
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

#Importaciones
from .models import Secuencia, Blast
from .forms import IngresarForm
from .utils import render_pdf
from . import crearPDF

#Modulos de python generales
import os
import subprocess
from io import StringIO
import sys
import time
import cairosvg
from urllib import request

#Modulos de biopython
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def Funcionamiento(request):
    cadena  = request.POST.get('cadena')
    mail    = request.POST.get('mail')
    nombre  = request.POST.get('nombre')
    cadena1    = request.POST.get('cadena1')

    #Aqui mandamos a llamar a blast
    #record = SeqIO.read(cad, format="fasta")
    result_handle = NCBIWWW.qblast("blastp", "nr", cadena.format("fasta"))
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    with open('/home/isaac/Escritorio/SAmin/TT/salida'+moment+'.xml', 'w') as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    int   = subprocess.Popen(['python', '/home/isaac/Escritorio/SAmin/TT/interpro.py', '--email', mail, cadena])                               
    cath = subprocess.Popen(["perl", "/home/isaac/Escritorio/SAmin/TT/cath.pl", cadena], stdin=subprocess.PIPE)
    with open('archivo.fasta', 'w') as envio:
        #envio.write(cadena)
        envio.write(cadena1, cadena)
    #clus = subprocess.Popen(['python', '/home/isaac/Escritorio/SAmin/TT/clustalo.py', '--email', mail, cadena, cadena1], stdin=subprocess.PIPE)
    rap = subprocess.Popen(["curl", '-d', 'jobname', nombre, 'email', mail, 'useProfile', 'False', 'sequences', cadena, '-X', 'POST', 'http://raptorx.uchicago.edu/StructPredV2/predict/'], stdin=subprocess.PIPE)

    cadena_obj = Secuencia(Secuencia = cadena, Nombre = nombre, Correo = mail)
    cadena_obj.save()
    
    #return render(request, 'TT/clustal.html', {'cadena':cadena})
    return render(request, 'TT/cadena.html', {'cadena':cadena})

def clustalO(request):
    cad1 = request.POST.get('cadena1')
    cad2 = request.POST.get('cadena2')
    mail = 'cob.log.cof@gmail.com'
    nombre = 'pruebas'
    #mandamos a llamar a clustal: Modificar para que reciba ambas cadenas
    
    return render(request, 'TT/generarPDF.html')

def creaPDF(request):
    cairosvg.svg2png(url='/home/isaac/Escritorio/SAmin/iprscan5-R20200608-185227-0730-22289433-p2m.svg.svg', write_to='/home/isaac/Escritorio/SAmin/TT/static/TT/prueba1.png')
    return render(request, 'TT/generarPDF.html')

def index(request):
    return render(request, 'TT/index.html')

def about(request):
    return render(request, 'TT/about.html')

def contacto(request):
    return render(request, 'TT/contacto.html')
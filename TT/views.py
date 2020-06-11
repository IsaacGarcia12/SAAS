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
import requests

#Modulos de biopython
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo


def Funcionamiento(request):
    cadena  = request.POST.get('cadena')
    mail    = request.POST.get('mail')
    nombre  = request.POST.get('nombre')
    cadena1 = request.POST.get('cadena1')

    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

    #Hacemos un archivo para algunas apis
    with open('creacion.fasta', 'w') as crea:
        crea.write(cadena+'\n'+cadena1)

    #Aqui mandamos a llamar a BLAST
    #record = SeqIO.read(cad, format="fasta")
    result_handle = NCBIWWW.qblast("blastp", "nr", cadena.format("fasta"))
    with open('/home/isaac/Escritorio/SAmin/TT/salida'+moment+'.xml', 'w') as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    #Interpro
    interpro = subprocess.Popen(['python', '/home/isaac/Escritorio/SAmin/TT/interpro.py', '--email', mail, cadena, cadena1])                               
    
    #CATH:
    file_fasta = '/home/isaac/Escritorio/SAmin/TT/new.fasta'
    req = requests.post('http://www.cathdb.info/search/by_funfhmmer', json={'fasta': file_fasta})
    print(r.text)
    moment = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    with open('/home/isaac/Escritorio/SAmin/TT/static/TT/salida'+moment+'.json', 'w') as out:
        out.write(r.text)

    #cath = subprocess.Popen(["perl", "/home/isaac/Escritorio/SAmin/TT/cath.pl", cadena], stdin=subprocess.PIPE)
    
    #CLUSTAL Obtencion del phylotree:
    cline = ClustalwCommandline("clustalw", infile="new.fasta", outfile="new.aln")
    print (cline)
    stdout, stderr = cline()
    print(stdout)

    #Con esto leemos el phytlotree
    tree = Phylo.read("new.dnd", "newick")
    tree.rooted = True

    #Con esto lo convertimos a otro tipo de notacion
    Phylo.convert('new.dnd', 'newick', 'new.xml', 'phyloxml')

    #Imprimimos el Arbol
    Phylo.draw_ascii(tree)

    cadena_obj = Secuencia(Secuencia = cadena, Nombre = nombre, Correo = mail)
    cadena_obj.save()
    
    return render(request, 'TT/cadena.html', {'cadena':cadena})

def creaPDF(request):
    cairosvg.svg2png(url='/home/isaac/Escritorio/SAmin/iprscan5-R20200608-185227-0730-22289433-p2m.svg.svg', write_to='/home/isaac/Escritorio/SAmin/TT/static/TT/prueba1.png')
    return render(request, 'TT/generarPDF.html')

def index(request):
    return render(request, 'TT/index.html')

def about(request):
    return render(request, 'TT/about.html')

def contacto(request):
    return render(request, 'TT/contacto.html')
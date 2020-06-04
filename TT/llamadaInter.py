import subprocess
from sys import argv

mail = argv[0]
#i = 'new.fasta'
"""
archivo='/home/isaac/Escritorio/SAmin/TT/entradaBlast.fasta'
f = open(archivo, 'r')
cadena = f.read()
f.close()
print(cadena)
"""
cadena = argv[1]
pi = subprocess.Popen(['python', 'interpro.py', '--email', mail, cadena])
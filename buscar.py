import glob
import os

#Archivos de Blast
archivosBlast = glob.glob('/home/isaac/Escritorio/SAmin/TT/static/TT/blast_result/*.xml') 
latest_file = max(archivosBlast, key=os.path.getctime)
print(latest_file)

#Obtenemos el archivo SVG
archivosSVG = glob.glob('/home/isaac/Escritorio/SAmin/TT/static/TT/interPro/*.svg')
ultimo_SVG = max(archivosSVG, key=os.path.getctime)
print(ultimo_SVG)

#Obtenermos el archivo
archivoJson = glob.glob('/home/isaac/Escritorio/SAmin/TT/static/TT/cath_results/*.json')
ultimo_json = max(archivoJson, key=os.path.getctime)
print(ultimo_json)





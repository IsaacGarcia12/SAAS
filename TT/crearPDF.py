#Import para poder crear el PDF
from reportlab.pdfgen import canvas

#para importar un el TTF que se requiera
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

#Para poder darle color al texto de manera mas sencilla
from reportlab.lib import colors

#Import para transformar imagenes
import cairo
from PIL import Image

import time


def dibujar(pdf):
	#Coordenadas para X
	pdf.drawString(100, 810, 'x100')
	pdf.drawString(200, 810, 'x200')
	pdf.drawString(300, 810, 'x300')
	pdf.drawString(400, 810, 'x400')
	pdf.drawString(500, 810, 'x500')

	#Coordenadas para Y
	pdf.drawString(10, 100, 'y100')
	pdf.drawString(10, 200, 'y200')
	pdf.drawString(10, 300, 'y300')
	pdf.drawString(10, 400, 'y400')
	pdf.drawString(10, 500, 'y500')
	pdf.drawString(10, 600, 'y600')
	pdf.drawString(10, 700, 'y700')
	pdf.drawString(10, 800, 'y800')

moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
filename = 'PDF_Prueba'+moment+'.pdf'
documenttitle = 'SAAS'
title = 'Trabajo Terminal 2'
subTitle = 'Anotaciones'
cathId = '1aec322834de7471cfa3d703d6659b6a'
#Para poder escribir se manda como array
textLines = ['Blast: ', 'Cath Task Id: ' + cathId, 'Familia: ', 'Arbol: ']
imageFam = '/home/isaac/Escritorio/SAmin/TT/static/TT/prueba1.png'
imageTree  = '/home/isaac/Escritorio/SAmin/TT/static/TT/Figure_1.png'
pdf = canvas.Canvas(filename)
pdf.setTitle(documenttitle)

"""
En la siguiente linea de codigo se muestra como "pintar"
algo, las coordenadas son en X y Y, el limite para y = 800
limite para x = 500
"""

pdf.drawCentredString(300,770, title) 

#Esta funcion de setFillColor
#Da colo al texto RGB Duh
pdf.setFillColorRGB(255, 0, 0)
pdf.setFont('Courier-Bold', 24)
pdf.drawCentredString(290, 720, subTitle)

#Ora vamos a dibujar una linea
pdf.line(30, 710, 550, 710)

#Ora el texto:
text = pdf.beginText(40, 680)
text.setFont('Courier', 12)

#Este metodo sale de colors declarado arriba
#Recuerda que el texto tiene que ser mandado
#a traves de un array
for line in textLines:
	text.textLine(line)
pdf.drawText(text)


#Ahora para poner una imagen
#pdf.drawImage(imageI, 130, 400, width=100,height=66.62, mask='auto')
pdf.drawImage(imageFam, 120, 100, width=300, height=300)
#pdf.drawInlineImage(imageTree, 120, 400)

pdf.save()
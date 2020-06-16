#Import para poder crear el PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

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

#Aqui empieza la construccion del PDF
documenttitle = 'SAAS'
title = 'Anotaciones'
cathId = '1aec322834de7471cfa3d703d6659b6a'
imageFam = '/home/isaac/Escritorio/SAmin/TT/static/TT/prueba1.png'
imageTree  = 'tree3.png'
pdf = canvas.Canvas(filename)
pdf.setTitle(documenttitle)

dibujar(pdf)
pdf.drawCentredString(300,770, title) 

pdf.setFillColorRGB(0, 0, 0)
pdf.setFont('Courier', 12)
text = pdf.beginText(50, 700)

#Familia(SalidaInterpro)
pdf.drawString(50, 720, 'Resultado Interpro:')
pdf.drawInlineImage(imageFam, 50, 400, width=550, height=310) 	#Imagen donde se muestra la familia

#
pdf.drawString(50, 380, 'Árbol filogenético:')
pdf.drawInlineImage(imageTree, 50, 150, width=350, height=210)



pdf.save()
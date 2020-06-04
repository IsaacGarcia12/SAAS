from reportlab.pdfgen import canvas

#para importar un el TTF que quiera
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

#Para poder darle color al texto de manera mas sencilla
from reportlab.lib import colors

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


filename = 'primerPDF.pdf'
documenttitle = 'nuevo Generado'
title = 'Mi primer PDF'
subTitle = 'Este es un subtitulo'
textLines = ['Red velvet es el mejor grupo al igual que aborted', 
'y hypocrisy', 
'y lamb of god']
#image = 'C:/Users/isaac/Documents/pythonProjects/djangoPDF/joy.jpg'
pdf = canvas.Canvas(filename)
pdf.setTitle(documenttitle)
"""
En la siguiente linea de codigo se muestra como "pintar"
algo, las coordenadas son en X y Y, el limite para y = 800
limite para x = 500
"""
#Para poder registrar un font nuevo
#Sale de los modulos importados para poder registrar el font
pdfmetrics.registerFont(
	#Supongo que abc es el nombre del 
	#font que le otorgamos para este codigo
	TTFont('abc', 'PTS55F.ttf'))
"""
#Ira carnal ahi te van los fonts
for font in pdf.getAvailableFonts():
	print(font)
dibujar(pdf)
"""
#ESto es para el titulo
pdf.setFont('abc', 36)
pdf.drawCentredString(300,770, title) 

#Esta funcion de setFillColor
#Da colo al texto RGB Duh
pdf.setFillColorRGB(255, 0, 0)
pdf.setFont('Courier-Bold', 24)
pdf.drawCentredString(290, 720, subTitle)

#Ora vamos a dibujar una linea :v
pdf.line(30, 710, 550, 710)

#Ora el texto:
text = pdf.beginText(40, 680)
text.setFont('Courier', 12)

#Este metodo sale de colors declarado arriba
#Recuerda que el texto tiene que ser mandado
#a traves de un array
text.setFillColor(colors.green)
for line in textLines:
	text.textLine(line)
pdf.drawText(text)

"""
#Ahora para poner una imagen
image._restrictSize(1*inch, 2*inch)
pdf.drawInlineImage(image, 130,400)
"""

pdf.save()
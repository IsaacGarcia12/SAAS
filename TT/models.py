from django.db import models

#Modelo donde se guarda la secuencia introducida
class Secuencia(models.Model):
    Secuencia = models.CharField(default=0, max_length=200)
    Correo = models.EmailField()
    idSecuencia = models.IntegerField(default=0)
    Nombre = models.CharField(default=0, max_length=250, primary_key=True)

#Modelo que guarda Blast
class Blast(models.Model):
    idBlast = models.CharField(max_length=100)
    secuencia = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)
    #archivo = models.FileField(upload_to='SAmin/files/')
    #Ver como guardar el archivo

#Modelo donde se guardara salida de SwissModel
class Swiss(models.Model):
    idSwissModel = models.CharField(max_length=200)
    SecIdRes = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)

class Cath(models.Model):
    secIdRes = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)

class InterPro(models.Model):
    idSeqFamilia = models.CharField(max_length=200)
    idSeqDominio = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)

class Clustal(models.Model):
    idSecPhylo = models.CharField(max_length=200)
    idSecMatriz = models.CharField(max_length=200)
    idSecTree = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)

class Raptor(models.Model):
    idSecSsb = models.CharField(max_length=200)
    idSecAcc = models.CharField(max_length=200)
    idSecDisc = models.CharField(max_length=200)
    nombre = models.ForeignKey('Secuencia', on_delete=models.CASCADE, default=0)
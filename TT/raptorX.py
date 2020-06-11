import requests
import time

file_fasta = '/home/isaac/Escritorio/SAmin/TT/new.fasta'
values = {'-- form jobname' : 'Dude',
          '--form email' : 'cob.log.cof@gmail.com',
          '--form useProfile' : 'False',
          '--form sequences' : file_fasta,
          }
r = requests.post('http://raptorx.uchicago.edu/StructPropertyPred/predict/', values)
print(r.text)
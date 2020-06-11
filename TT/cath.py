import requests
import time

file_fasta = '/home/isaac/Escritorio/SAmin/TT/new.fasta'
r = requests.post('http://www.cathdb.info/search/by_funfhmmer', json={'fasta': file_fasta})
print(r.text)
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
with open('/home/isaac/Escritorio/SAmin/TT/static/TT/salida'+moment+'.json', 'w') as out:
    out.write(r.text)
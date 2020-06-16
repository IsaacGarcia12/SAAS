 
import requests
import time


moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
file_fasta = '/home/isaac/Escritorio/SAmin/TT/new.fasta'
url = 'https://swissmodel.expasy.org/interactive'
r = requests.post(url, json={'fasta': file_fasta})
print(r.text)
#print(r.json())
#print(r_dict['task_id'])
#
#with open('/home/isaac/Escritorio/SAmin/TT/static/TT/salida'+r_dict['task_id']+'.json', 'w') as out:
    #out.write(r_dict)
#    out.write(r_dict['task_id'])
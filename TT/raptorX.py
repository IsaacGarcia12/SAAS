"""
from urllib import request
from sys import argv

nombre = 'prueba'
mail = 'cob.log.cof@gmail.com'
cadena = '>tr|D3ZI84|D3ZI84_RAT C-C motif chemokine OS=Rattus norvegicus OX=10116 GN=Ccl19 PE=3 SV=1 MASRVTPLLAFSLLVLWTFSAPALGGANDAEDCCLSVTQRPIPGNIVKAFRYLLIQDGCRVPAVVFTTLRGYQLCAPLDQPWVERIIRRLKKSSSKSKGGSTKRGPVS'
data = {'--form jobname=', nombre, '--form email=', mail, '--form useProfile=', 'False', '--form sequences=', cadena}
url = 'http://raptorx2.uchicago.edu/StructurePropertyPred/curl/'
req = request.Request(url, data)
"""
from urllib import request
from urllib import parse

#{'-- form jobname': 'Dude', '--form email': 'cob.log.cof@gmail.com', '--form useProfile': 'False', '--form sequences': '>tr|D3ZI84|D3ZI84_RAT C-C motif chemokine OS=Rattus norvegicus OX=10116 GN=Ccl19 PE=3 SV=1 MASRVTPLLAFSLLVLWTFSAPALGGANDAEDCCLSVTQRPIPGNIVKAFRYLLIQDGCRVPAVVFTTLRGYQLCAPLDQPWVERIIRRLKKSSSKSKGGSTKRGPVS'}
url = 'http://raptorx.uchicago.edu/StructPredV2/predict/'
values = {'-- form jobname' : 'Dude',
          '--form email' : 'cob.log.cof@gmail.com',
          '--form useProfile' : 'False',
          '--form sequences' : '>tr|D3ZI84|D3ZI84_RAT C-C motif chemokine OS=Rattus norvegicus OX=10116 GN=Ccl19 PE=3 SV=1 MASRVTPLLAFSLLVLWTFSAPALGGANDAEDCCLSVTQRPIPGNIVKAFRYLLIQDGCRVPAVVFTTLRGYQLCAPLDQPWVERIIRRLKKSSSKSKGGSTKRGPVS',
          }

data = parse.urlencode(values).encode("utf-8")
req = request.Request(url, data)
response = request.urlopen(req)
the_page = response.read()

#data = {'--form jobname=', nombre, '--form email=', mail, '--form useProfile=', 'true', '--form sequences=', cadena}
    #url = 'http://raptorx2.uchicago.edu/StructurePropertyPred/curl/'
    #req = request.request(url, data)
#>tr|D3ZI84|D3ZI84_RAT C-C motif chemokine OS=Rattus norvegicus OX=10116 GN=Ccl19 PE=3 SV=1 MASRVTPLLAFSLLVLWTFSAPALGGANDAEDCCLSVTQRPIPGNIVKAFRYLLIQDGCRVPAVVFTTLRGYQLCAPLDQPWVERIIRRLKKSSSKSKGGSTKRGPVS
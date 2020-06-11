from urllib import request

data = {'--form jobname=', nombre, '--form email=', mail, '--form useProfile=', 'true', '--form sequences=', cadena}
url = 'http://raptorx2.uchicago.edu/StructurePropertyPred/curl/'
req = request.Request(url, data)

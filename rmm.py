import json
import urllib2
import sys

respuestaServer = json.load(urllib2.urlopen('http://www.apilayer.net/api/live?access_key=66f63d06191a711d7890254929763272&source=USD&currencies=EUR'))
valorDolarEuro = str(respuestaServer['quotes']["USDEUR"])

numero = sys.argv[1]
conversion = round(float(numero)*float(valorDolarEuro),2)
print(conversion)

pEntera = int(conversion)
pDecimal = int((conversion-int(conversion))*100)

archivo = open('/etc/asterisk/valor.txt', 'w')
archivo.write(str(pEntera))
archivo.write('\n')
archivo.write(str(pDecimal))
archivo.close()

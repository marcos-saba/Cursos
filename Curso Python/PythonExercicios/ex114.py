import urllib
import urllib.request
try:
    r = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("\033[31mO site Pudim não está acessível.")
else:
    print('\033[32mO site Pudim está acessível!')
#    print(r.read())

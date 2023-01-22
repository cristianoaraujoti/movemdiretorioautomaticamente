import os
import shutil
from shutil import copytree

path = "C:/Users/Cristiano/Documents/Py/arquivo.txt"
source = "C:/Users/Cristiano/Documents/Py/Source/arquivo.txt"
Destination = "C:/Users/Cristiano/Documents/Py/Destination/arquivo.txt"
rename = "C:/Users/Cristiano/Documents/Py/Destination/re-arquivo.txt"

#Verificar se existi o arquivo shutil no diretório /Py
if os.path.exists(path):
    print('O diretório{} existi'.format(path))
else:
    print('O diretório {} não existi'.format(path))

if os.path.exists(rename):
    os.remove(rename)
else:
    pass

#Verifica se existi o arquivo com o mesmo nome no diretório /Destination
if os.path.exists(Destination):
    os.rename(Destination, rename)
    # print('O diretório {} existir'.format(source))
else:
    print('O diretório {} não existi'.format(Destination))

if os.path.exists(path):
    shutil.move(path, Destination)
else:
    pass
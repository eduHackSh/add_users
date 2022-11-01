import os
import sys
import subprocess



#Funciones
def add_us(user, passwd, desc):

    proc = subprocess.Popen(['/usr/sbin/useradd', '-p', f'{passwd}', '-c', f'{desc}', '-m', f'{user}'])
    try:
        outs, errs = proc.communicate(timeout=15)
    except TimeOutExpired:
        proc.kill()
        outs, errs = proc.communicate()


#Abrir el archivo de usuarios
archivo = open('lista.txt', 'rt')
content = archivo.read()

#Contar las lineas del archivo
cLineas = 0
cList = content.split('\n')
for l in cList:
    if l:
        cLineas += 1
print(cLineas)
archivo.close()
i = 0

#Recorriendo el archivo
archivo = open('lista.txt')

while i < cLineas:
    linea = archivo.readline().rstrip('\n')
    lArray = linea.split(';')
    nombre= lArray[0]
    apellido= lArray[1]
    correo= lArray[2]
    user= lArray[3]
    cargo=lArray[5]
    passwd = lArray[4]
    desc = f'{nombre} {apellido} - {cargo}'
    add_us(user, passwd, desc)
    i += 1




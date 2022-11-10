import os
import sys
import subprocess
import smtplib, ssl
from dotenv import load_dotenv
from email.message import EmailMessage
import time
import body
import readex


#Funciones
def add_us(user, passwd, desc):

    proc = subprocess.Popen(['/usr/sbin/useradd', '-p', f'{passwd}', '-c', f'{desc}', '-m', f'{user}'])
    try:
        outs, errs = proc.communicate(timeout=15)
    except TimeOutExpired:
        proc.kill()
        outs, errs = proc.communicate()

confirmMail = True

def send_email(receiver, name, surname, user, passwd):
    if confirmMail:
        smtp_address = 'smtp.gmail.com'
        smtp_port = 465
        
        email_address = "piedadedutest@gmail.com"
        load_dotenv()
        email_pass = os.getenv("MAIL_PASSWORD")
        context = ssl.create_default_context()
        bodyMess = body.get_message()
        msg = EmailMessage()
        msg['Subject'] = bodyMess[0]
        msg['From'] = email_address
        msg['To'] = receiver
        bodyM = bodyMess[1]
        bodyM = bodyM.replace('$NAME', name)
        bodyM = bodyM.replace('$SURNAME', surname)
        bodyM = bodyM.replace('$USER', user)
        bodyM = bodyM.replace('$PASSWORD', passwd)
        msg.set_content(bodyM)
        

        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            
            server.login(email_address, email_pass)
            server.send_message(msg)
            server.close()

whatRead = input('Que tipo de archivo deberia leer?\n[E] = excel file\n[T] = txt file\n')
whatRead.upper()

if whatRead == "T":
#Abrir el archivo de usuarios
    archivo = open('lista.txt', 'rt')
    content = archivo.read()

#Contar las lineas del archivo
    cLineas = 0
    cList = content.split('\n')
    for l in cList:
        if l:
            cLineas += 1
    
    archivo.close()
    i = 0

    archivo = open("lista.txt")
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
        print(f"Se registraran un total de {cLineas} usuarios")
        confirm = input("Confirmar [S/N]\n")
        confirm.upper()
        if confirm == "S":
            add_us(user, passwd, desc)
            send_email(correo, nombre, apellido, user, passwd)
            i += 1
        else:
            print("Saliendo...")
            time.sleep(2)
            exit(0)

    archivo.close()

elif whatRead == "E":
    maxRow = readex.maxRow()
    print(f'Se registraran un total de {maxRow - 1} usuarios')
    confirm = input("Confirmar [S/N]\n")
    confirm.upper()
    if confirm == "S":
        lst = readex.Obtain_Users()
        for r in lst:
            nombre = r["nombre"]
            apellido = r["apellido"]
            email = r["email"]
            cargo = r["cargo"]
            user = r["user"]
            passwd = r["password"]
            desc = f"{nombre} {apellido} - {cargo}"

            print(desc)
    else:
        print("Saliendo...")
        time.sleep(2)




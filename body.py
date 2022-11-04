import re

def get_message():
    archivo = open("body.txt", "rt")
    texto = archivo.read()
    archivo.close()
    r = re.findall('{([^}]*)}', texto)
    return r






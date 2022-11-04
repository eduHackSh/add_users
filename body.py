import re

subject = ""
body = ""

archivo = open("body.txt", "rt")

texto = archivo.read()



r = re.findall('[^ASUNTO:] [?\}](.*)(?!})', texto)

print(r[0])


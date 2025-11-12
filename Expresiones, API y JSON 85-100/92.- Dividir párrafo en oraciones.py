import re

texto = input("Escribe un párrafo: ")
oraciones = re.split(r'[.!?]+', texto)
for o in oraciones:
    o = o.strip()
    if o:
        print(o)

numero_um = int(input("Informe o primeiro número: "))
numero_dois = int(input("Informe o segundo número: "))

if numero_um > numero_dois:
    multiplos = numero_um / numero_dois
else:
    multiplos = numero_dois / numero_um
if multiplos.is_integer():
  print("São multiplos")
else:
  print("Não são multiplos")


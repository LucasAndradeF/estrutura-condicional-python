numero_um = int(input("Informe o primeiro n�mero: "))
numero_dois = int(input("Informe o segundo n�mero: "))

if numero_um > numero_dois:
    multiplos = numero_um / numero_dois
else:
    multiplos = numero_dois / numero_um
if multiplos.is_integer():
  print("S�o multiplos")
else:
  print("N�o s�o multiplos")


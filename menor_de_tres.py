primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

if primeiro_numero <= segundo_numero <= terceiro_numero:
  print("Menor: ", primeiro_numero)
elif segundo_numero <= terceiro_numero:
  print("Menor: ", segundo_numero)
else:
  print("Menor: ", terceiro_numero)

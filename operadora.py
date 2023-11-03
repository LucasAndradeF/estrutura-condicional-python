quantidade_minutos = int(input("Informe os minutos utilizados: "))

if quantidade_minutos > 100:
  total_minutos = 50 + ((quantidade_minutos % 100) * 2) 
  print(f"O valor a ser pago é: R$ {total_minutos:.2f}.")
else:
  print("O valor a ser pago é: R$ 50,00.")
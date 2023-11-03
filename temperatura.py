tipo_temperatura = input("Informe o tipo da temperatura C/F: ")
tipo_temperatura = tipo_temperatura.upper()
if tipo_temperatura == 'C':
  temperatura_c = float(input("Informe a temperatura em Celsius: "))  
  temperatura_f = 9 * temperatura_c / 5 + 32   
  print(f"\nA temperatura em Fahrenheit é: {temperatura_f:.2f}")
elif tipo_temperatura == 'F':
  temperatura_f = float(input("Informe a temperatura em Celsius: "))  
  temperatura_c = 5 / 9 * (temperatura_f - 32)
  print(f"\nA temperatura em Celsius é: {temperatura_c:.2f}")
else:
  print("Caractere incorreto")
produto_um = 5.00
produto_dois = 3.50
produto_tres = 4.80
produto_quatro = 8.90
produto_cinco = 7.32
valor_compra = float

codigo_produto = int(input("Informe o código do produto: "))
quantidade_comprada = int(input("Informe a quantidade comprada: "))
if codigo_produto == 1:
  valor_compra = produto_um * quantidade_comprada
  print(f"Valor a pagar: R$ {valor_compra:.2f}")
elif codigo_produto == 2:
  valor_compra = produto_dois * quantidade_comprada
  print(f"Valor a pagar: R$ {valor_compra:.2f}")
elif codigo_produto == 3:
  valor_compra = produto_tres * quantidade_comprada
  print(f"Valor a pagar: R$ {valor_compra:.2f}")
elif codigo_produto == 4:
  valor_compra = produto_quatro * quantidade_comprada
  print(f"Valor a pagar: R$ {valor_compra:.2f}")
else:
  valor_compra = produto_cinco * quantidade_comprada
  print(f"Valor a pagar: R$ {valor_compra:.2f}")


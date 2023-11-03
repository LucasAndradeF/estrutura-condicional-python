preco_produto = float(input("Informe o valor do produto: "))
quantidade_comprada = float(input("Informe a quantidade comprada: "))
valor_pagamento = float(input("Informe o valor do pagamento: "))

valor_da_compra = preco_produto * quantidade_comprada
troco = valor_pagamento - valor_da_compra

if valor_pagamento < valor_da_compra:
  troco_formatado = -troco
  print(f"Dinheiro insuficiente. Faltam R$ {troco_formatado:.2f} reais.")
else:
  print(f"Troco: R$ {troco:.2f} reais.")
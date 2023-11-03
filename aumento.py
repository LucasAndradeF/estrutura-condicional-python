salario_atual = float(input("Informe o seu salário atual: "))

if salario_atual <= 1000:
    novo_salario = (salario_atual * 0.20) + salario_atual
    valor_aumento = novo_salario - salario_atual
    print(f"Novo salário: R$ {novo_salario:.2f} \nValor do aumento: R$ {valor_aumento:.2f} \nAumento de: 20%.")
elif 1000 < salario_atual <= 3000:
    novo_salario = (salario_atual * 0.15) + salario_atual
    valor_aumento = novo_salario - salario_atual
    print(f"Novo salário: R$ {novo_salario:.2f} \nValor do aumento: R$ {valor_aumento:.2f} \nAumento de: 15%.")
elif 3000 < salario_atual <= 8000:
    novo_salario = (salario_atual * 0.10) + salario_atual
    valor_aumento = novo_salario - salario_atual
    print(f"Novo salário: R$ {novo_salario:.2f} \nValor do aumento: R$ {valor_aumento:.2f} \nAumento de: 10%.")
else:
  novo_salario = (salario_atual * 0.5) + salario_atual
  valor_aumento = novo_salario - salario_atual
  print(f"Novo salário: R$ {novo_salario:.2f} \nValor do aumento: R$ {valor_aumento:.2f} \nAumento de: 5%.")
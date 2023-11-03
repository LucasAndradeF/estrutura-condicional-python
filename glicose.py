medida_glicose = float(input("Digite a medida da glicose: "))

if medida_glicose <= 100:
  print(f"Classificação: Normal")
elif medida_glicose > 100 and medida_glicose <= 140:
  print("Classificação: Elevado")
else:
  print("Classificação: Diabetes")




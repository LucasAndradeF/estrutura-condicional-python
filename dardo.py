arremesso_dardo_um = float(input("Digite a distância do primeiro arremesso: "))
arremesso_dardo_dois = float(input("Digite a distância do segundo arremesso: "))
arremesso_dardo_tres = float(input("Digite a distância do terceiro arremesso: "))

if arremesso_dardo_um > arremesso_dardo_dois > arremesso_dardo_tres:
  print(f"\nMaior distância: {arremesso_dardo_um:.2f}")
elif arremesso_dardo_dois > arremesso_dardo_tres:
  print(f"\nMaior distância: {arremesso_dardo_dois:.2f}")
else:
  print(f"\nMaior distância: {arremesso_dardo_tres:.2f}")

import math

coeficiente_a = float(input("Digite o valor de A: "))
coeficiente_b = float(input("Digite o valor de B: "))
coeficiente_c = float(input("Digite o valor de C: "))

delta = coeficiente_b **2 - 4* coeficiente_a * coeficiente_c

if coeficiente_a == 0 or delta < 0:
    print("Essa equação não possui raízes reais.")
else:
    x1 = (-coeficiente_b + math.sqrt(delta)) / (2 * coeficiente_a)
    x2 = (-coeficiente_b - math.sqrt(delta)) / (2 * coeficiente_a)
    print(f"X1 = {x1:.4f} \nX2 = {x2:.4f}")




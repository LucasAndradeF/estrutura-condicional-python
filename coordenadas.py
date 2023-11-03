ponto_x = float(input("Informe o valor de X: "))
ponto_y = float(input("Informe o valor de Y: "))

if ponto_x > 0 and ponto_y > 0:
    print("Q1")
elif ponto_x < 0 and ponto_y > 0:
    print("Q2")
elif ponto_x < 0 and ponto_y < 0:
    print("Q3")
elif ponto_x > 0 and ponto_y < 0:
    print("Q4")
elif ponto_x == 0 and ponto_y == 0:
    print("Origem")
elif ponto_x == 0 and ponto_y !=0:
    print("Eixo Y")
else:
    print("Eixo X")    
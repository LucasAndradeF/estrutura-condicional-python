nota_um = float(input("Informe a primeira nota: "))
nota_dois = float(input("Informe a segunda nota: "))

nota_final = nota_um + nota_dois

if nota_final < 60.00:
    print(f"Nota final: {nota_final} \nREPROVADO")
else:
    print(f"Nota final: {nota_final} \nAluno Aprovado")

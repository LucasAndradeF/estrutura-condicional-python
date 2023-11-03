hora_incial = int(input("Digite a hora inicial do jogo: "))
hora_final = int(input("Digite a hora final do jogo: "))

if hora_final > hora_incial:
    duracao_jogo = hora_final - hora_incial
    print(f"O jogo durou {duracao_jogo} horas.")
else: 
    duracao_jogo = 24 - hora_incial + hora_final 
    print(f"O jogo durou {duracao_jogo} horas.")
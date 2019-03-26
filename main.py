import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#numero_secreto = 42
numero_secreto = round(random.randrange(1,101))
#total_tentativas = 5

print("\nSelecione um nível de dificuldade:")
print("(1)Fácil (2)Médio (3)Difícil\n")
nivel = int(input("Nível desejado: "))

if (nivel == 1):
    total_tentativas = 15
elif (nivel == 2):
    total_tentativas = 8
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_tentativas))
    chute  = int(input("Digite um número entre 1 e 100: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("\n*-*-*Parabéns! Você acertou!*-*-*")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
print("\n-----------------------------")
print("-------- FIM DO JOGO --------")
print("-----------------------------")
print("Número secreto: {}".format(numero_secreto))
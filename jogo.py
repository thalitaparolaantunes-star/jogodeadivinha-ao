print("**********************************")
print("bem vindo ao jogo de adivinhação")
print("**********************************") 

numerosecreto = 40 

chute = input("Digite o seu número: ") 
print("você digitou: ", chute ) 

chuteNumerico = int(chute)

# print(chute) 

acertou = chuteNumerico = numerosecreto
maior = chuteNumerico > numerosecreto
menor = chuteNumerico < numerosecreto
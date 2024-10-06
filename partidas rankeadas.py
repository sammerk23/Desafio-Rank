#Calculadora de partidas Rankeadas

i = 1

def calc_rank (name):
    vitorias = int(input("Quantas vitórias o herói obteve?: "))
    derrotas = int(input("Quantas derrotas o herói obteve?: "))
    saldo = vitorias - derrotas

    rank = rankname(saldo)

    return ("\nO Herói {} tem de saldo de "+ str(saldo) +" vitórias e está no nível de {}!").format(name, rank)

def rankname(a):

    if (a <= 10):
        rank = "Ferro"

    elif (a > 10 and a <=20):
        rank = "Bronze"
        
    elif (a > 20 and a <=50):
        rank = "Prata"
            
    elif (a > 50 and a <=80):
        rank = "Ouro"
            
    elif (a > 80 and a <=90):
        rank = "Diamante"
            
    elif (a > 90 and a <=100):
        rank = "Lendário"
            
    else:
        rank = "Imortal"
    return rank

while i == 1:
    name = str(input("Digite o nome do Herói: "))
    print(calc_rank(name))
        
    i = int(input("\n\nVocê deseja inserir novos valores?\n" + "Digite '1' para SIM    Digite '0' para NÃO\nOpção: "))
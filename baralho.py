import random as r
cartas=[('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('10',10),('J',11),('Q',12),('K',13),('HaHaHaHa',0)];
naipe=[('ouro',1),('copas',2),('paus',2),('espadas',1)]
p=0
def baralho_aleatorio(pontuacao):
    escolha_valor = r.choice(cartas)
    escolha_naipe = r.choice(naipe)
    print(escolha_valor[0]+' de '+escolha_naipe[0])
    pontos = escolha_valor[1] * escolha_naipe[1]
    print(str(escolha_valor[1]) +' * '+ str(escolha_naipe[1])+' = '+str(pontos))
    if (escolha_valor[0] == 'HaHaHaHa') and (escolha_naipe[1] == 2):
        pontuacao = 0
    elif (escolha_valor[0] == 'HaHaHaHa') and (escolha_naipe[1] == 1):
        pontuacao = -100

    if ((escolha_naipe[0] == 'paus') or (escolha_naipe[0] == 'espadas')):
        pontuacao -= pontos
    elif ((escolha_naipe[0] == 'copas') or (escolha_naipe[0] == 'ouro')):
        pontuacao += pontos
    
    return pontuacao

def baralho_vinteum(pontos):
    if pontos > 21:
        print('Você estourou, já tem mais de 21!!')
    else:
        escolha_valor=r.choice(cartas)
        pontos=pontos+escolha_valor[1]
        print(f'Puxei a carta {escolha_valor[0]} e que soma {escolha_valor[1]} pontos a você!')
        if pontos > 21:
            print('Você estourou, já tem mais de 21!!')
    return pontos


parar=0
while(parar==0):
    p=baralho_vinteum(p)
    print('Você tem ',str(p),' pontos. Deseja continuar?')
    continua=input()
    if continua == 'n':
        parar=1
print('Parou com ',str(p),' pontos')

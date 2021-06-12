from user import User
from banco import ve_pontos21
import random as r
from carta import Carta
cartas=[('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('10',10),('J',11),('Q',12),('K',13),('Coringa',0)];
naipe=[('ouro',1),('copas',2),('paus',2),('espadas',1)]
p=0
def baralho_aleatorio(carta, usuario):
    escolha_valor = r.choice(cartas)
    escolha_naipe = r.choice(naipe)
    print(escolha_valor[0]+' de '+escolha_naipe[0])
    pontos = escolha_valor[1] * escolha_naipe[1]
    print(str(escolha_valor[1]) +' * '+ str(escolha_naipe[1])+' = '+str(pontos))
    carta.descricao=escolha_naipe[0]
    carta.numero=escolha_valor[0]
    carta.pontos=pontos
    return carta

# já implementado
def baralho_vinteum(carta,usuario):
    p=ve_pontos21(usuario)
    if p > 21:
        print('Você estourou, já tem mais de 21!!')
        carta.descricao = carta.descricao + f' você estourou, já tem mais de 21!!'
    else:
        carta_escolhida=r.choice(cartas)
        carta.pontos = carta.pontos + carta_escolhida[1]
        carta.numero=carta_escolhida[1]
        
        carta.descricao = f'Embaralhei e puxei a carta {carta_escolhida[0]} e que soma {carta_escolhida[1]} pontos a você! E você tem {carta.pontos}'
        if carta.pontos > 21:
            carta.descricao = carta.descricao + f' você estourou, já tem mais de 21!!'
        elif carta.pontos == 21:
            carta.descricao = carta.descricao + f' você tem {carta.pontos} pontos parabéns, poucos conseguem!'
    return carta
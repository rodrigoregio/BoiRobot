import random as r
cartas=[('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('10',10),('J',11),('Q',12),('K',13),('Joker',0)];
naipe=[('ouro',4),('copas',3),('paus',2),('espadas',1)]
def baralho_aleatorio():
    escolha_valor = r.choice(cartas)
    escolha_naipe = r.choice(naipe)
    print(escolha_valor[0]+' de '+escolha_naipe[0])
    pontos = escolha_valor[1] * escolha_naipe[1]
    print(str(escolha_valor[1]) +' * '+ str(escolha_naipe[1])+' = '+str(pontos))
    if()

baralho_aleatorio()
import sqlite3 as sql3
from sqlite3.dbapi2 import Cursor
from user import User

#def conecta():
#    '''Retorna uma lista de 2 itens sendo que o indice 0 é a conexao e o 1 é o cursor'''
#    con=[]
#    con[0]=sql3.connect('twitchdata.db')
#    con[1]=con.cursor()
#    return con

def cria_tabela():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS ensinamentos(id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'+
        'id_usuario TEXT NOT NULL,'+
        'ensinamento TEXT NOT NULL);'
    )
    print('tabela criada com sucesso!')
    con.close()

def insere_usuario(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    #conexao=conecta()
    cursor.execute("""INSERT OR IGNORE INTO usuario (id_usuario,display_name) VALUES (?,?)""",(user.id, user.displayName))
    con.commit()
    con.close()

def insere_ponto(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""INSERT OR IGNORE INTO GAME (id_usuario,pontuacao) VALUES (?,?)""",(user.id,0))
    con.commit()
    con.close()

def insere_ponto_baralho(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""INSERT OR IGNORE INTO baralho_pontos (id_usuario,pontos,pontos21,recorde,recorde21) VALUES (?,?,?,?,?)""", (user.id,0,0,0,0))
    con.commit()
    con.close()

def baralho_ponto():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS baralho_pontos(id_usuario TEXT NOT NULL PRIMARY KEY,'+
        'pontos INTEGER NOT NULL,'+
        'pontos21 INTEGER NOT NULL,'+
        'recorde INTEGER NOT NULL,'+
        'recorde21 INTEGER NOT NULL);'
    )
    con.commit()
    con.close()

def minha_pontuacao(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT (pontuacao) FROM GAME WHERE id_usuario LIKE ?""",(user.id))
    meu_ponto=0
    for linha in cursor.fetchall():
        meu_ponto=int(linha)
    con.close()
    return meu_ponto

def aumenta_pontos21(user, carta):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE baralho_pontos SET  pontos21=pontos21+? WHERE id_usuario like ?""", (carta.numero, user.id))
    con.commit()
    cursor.close()
    con.close()

def aumenta_pontos_bale(user, numero):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE baralho_pontos SET  pontos=pontos+? WHERE id_usuario like ?""", (numero, user.id))
    con.commit()
    cursor.close()
    con.close()

def aumenta_pontos(user, numero_gerado):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE GAME SET pontuacao=pontuacao+? WHERE id_usuario LIKE ?""",(numero_gerado,user.id))
    con.commit()
    con.close()

def ve_pontos21(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT pontos21 FROM baralho_pontos WHERE id_usuario LIKE ?""",(str(user.id),))
    meu_ponto=0
    for linha in cursor.fetchall():
        meu_ponto=linha
    cursor.close()
    con.close()
    return meu_ponto[0]

def zera_meus21(user):
    con = sql3.connect('twitchdata.db')
    cursor = con.cursor()
    cursor.execute("""UPDATE baralho_pontos SET pontos21=0 WHERE id_usuario LIKE  ?""",(user.id,))
    con.commit()
    con.close()

def zera_pontos(user):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE GAME SET pontuacao=? WHERE id_usuario LIKE ?""",(0, user.id))
    con.commit()
    con.close()

def zera_todos_pontos():
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE GAME SET pontuacao=?""",(str(0)))
    cursor.execute("""UPDATE baralho_pontos SET pontos=? and pontos21=?""",(str(0)))
    con.commit()
    con.close()

def pegaTresMaioresPontosDados():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT display_name,pontuacao FROM GAME INNER JOIN usuario ON usuario.id_usuario=GAME.id_usuario ORDER BY pontuacao DESC LIMIT 3""")
    maiores=[]
    for linha in cursor.fetchall():
        maiores.append(linha)
        
    con.close()
    return maiores

baralho_ponto()
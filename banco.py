import sqlite3 as sql3
from conceitoFrases import FraseConceito as Conceito

#def conecta():
#    '''Retorna uma lista de 2 itens sendo que o indice 0 é a conexao e o 1 é o cursor'''
#    con=[]
#    con[0]=sql3.connect('twitchdata.db')
#    con[1]=con.cursor()
#    return con

def cria_tabelaConceito(): # tabela de conceitos
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS conceitos('+
        'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'+       
        'palavra TEXT NOT NULL,'+                               # palavra ou contexto (frase) que pode-se aumentar ou abaixar o nivel de conceito
        'pontuacao TEXT NOT NULL);')                              # pontuação que pode aumentar ou diminuir o nivel no meu conceito
    print('Tabela de conceitos criada com sucesso!')
    con.close()

def cria_tabelaConceitoUsuario():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS conceito_usuario('+
        'id_usuario TEXT NOT NULL PRIMARY KEY,'+
        'nivel INTEGER NOT NULL,'+
        'ultimo TEXT NOT NULL)')
    con.commit()
    con.close()

def pegaConceitos():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute('SELECT palavra from conceitos')
    conceitos=[]
    for linha in cursor.fetchall():
        conceitos.append(linha)
    con.close()
    return conceitos

def atualizaConceitoUsuario(usuario,conceito):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute()

def cria_tabelaEnsinamentos(): # ensinamentos
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS ensinamentos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'+
        'id_usuario TEXT NOT NULL,'+
        'ensinamento TEXT NOT NULL);'
    )
    print('tabela criada com sucesso!')
    con.close()

def cria_tabelaUsuarios(): # usuarios
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS usuario(id_usuario TEXT NOT NULL PRIMARY KEY,'+
        'display_name TEXT NOT NULL);'
    )
    print('tabela criada com sucesso!')
    con.close()

def cria_tabelaGame(): # usuarios
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Game(id_usuario TEXT NOT NULL PRIMARY KEY,'+
        'pontuacao INTEGER NOT NULL DEFAULT 0);'
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

def insere_pontoGame(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""INSERT OR IGNORE INTO Game (id_usuario,pontuacao) VALUES (?,?)""",(user.id,0))
    con.commit()
    con.close()

def minha_pontuacaoDado(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT (pontuacao) FROM Game WHERE id_usuario LIKE ?""",(user.id))
    meu_ponto=0
    for linha in cursor.fetchall():
        meu_ponto=int(linha)
    con.close()
    return meu_ponto

def aumenta_pontos(user, numero_gerado):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE Game SET pontuacao=pontuacao+? WHERE id_usuario LIKE ?""",(numero_gerado,user.id))
    con.commit()
    con.close()

def zera_pontos(user):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE Game SET pontuacao=? WHERE id_usuario LIKE ?""",(0, user.id))
    con.commit()
    con.close()

def zera_todos_pontos():
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE Game SET pontuacao=?""",(str(0)))
    con.commit()
    con.close()

def pegaTresMaioresPontos():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT display_name,pontuacao FROM Game INNER JOIN usuario ON usuario.id_usuario=Game.id_usuario ORDER BY pontuacao DESC LIMIT 3""")
    maiores=[]
    for linha in cursor.fetchall():
        maiores.append(linha)
        
    con.close()
    return maiores



cria_tabelaUsuarios()
cria_tabelaGame()
cria_tabelaEnsinamentos()
cria_tabelaConceito()
cria_tabelaConceitoUsuario()
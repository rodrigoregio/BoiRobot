import sqlite3 as sql3

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
        'CREATE TABLE IF NOT EXISTS ensinamentos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'+
        'id_usuario TEXT NOT NULL,'+
        'ensinamento TEXT NOT NULL);'
    )
    print('tabela criada com sucesso!')
    con.close()

def insere_usuario(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    #conexao=conecta()
    cursor.execute("""INSERT OR IGNORE INTO usuarios (id,display_name) VALUES (?,?)""",(user.id,user.displayName))
    con.commit()
    con.close()

def insere_ponto(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""INSERT OR IGNORE INTO pontos (id_usuario,pontuacao) VALUES (?,?)""",(user.id,0))
    con.commit()
    con.close()

def minha_pontuacao(user):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT (pontuacao) FROM pontos WHERE id_usuario LIKE ?""",(user.id))
    meu_ponto=0
    for linha in cursor.fetchall():
        meu_ponto=int(linha)
        
    con.close
    return meu_ponto

def aumenta_pontos(user, numero_gerado):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE pontos SET pontuacao=pontuacao+? WHERE id_usuario LIKE ?""",(numero_gerado,user.id))
    con.commit()
    con.close()

def zera_pontos(user):
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE pontos SET pontuacao=? WHERE id_usuario LIKE ?""",(0, user.id))
    con.commit()
    con.close()

def zera_todos_pontos():
    con= sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""UPDATE pontos SET pontuacao=?""",(str(0)))
    con.commit()
    con.close()

cria_tabela()
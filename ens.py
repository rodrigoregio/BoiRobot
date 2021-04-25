import random
import sqlite3 as sql3
from user import User
ensinamentos=[]
def pega_ensinamento():
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    cursor.execute("""SELECT ensinamento FROM ensinamentos""")

    for linha in cursor.fetchall():
        ensinamentos.append(linha)
    
    con.close()
    mystring=str(random.choice(ensinamentos))
    return mystring[2:-3]

def insere_ensinamento(user,ensinamento):
    con=sql3.connect('twitchdata.db')
    cursor=con.cursor()
    ensinamento=troca_porespaco(ensinamento)
    cursor.execute("""INSERT INTO ensinamentos (id_usuario,ensinamento) VALUES (?,?)""",(user.id,ensinamento))
    con.commit()
    con.close()
    print('Ensinamento inserido com sucesso!')

def troca_porespaco(argumento):
    texto=argumento.replace('_',' ')
    return texto
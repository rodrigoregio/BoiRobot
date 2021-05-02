import random
import sqlite3 as sql3
from user import User
ensinamentos=[]
ensinamentos.append('Mais vale um passarinho na mão do que dois voando!')
ensinamentos.append('Nem tudo o que reluz é ouro, pode ser ouro de tolo')
ensinamentos.append('Se estiver perdido, escolha sempre o caminho da direita, antes andando direito do que errado!')
ensinamentos.append('Nunca diga nunca, seu sim deve estar próximo!')
ensinamentos.append('Não faça nada de errado, alguém pode estar te filmando!')
ensinamentos.append('Acha poucos ensinamentos? manda no sussurro ao boirods para adicionar o seu!')
def pega_ensinamento():
    mystring=str(random.choice(ensinamentos))
    return mystring[2:-3]

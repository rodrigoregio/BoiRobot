import sys
import configparser
import irc.bot as ibot
import requests
from random import randint
from user import User
from banco import *
from time import sleep
from random import choice
from ens import pega_ensinamento,insere_ensinamento
class BoiRobot(ibot.SingleServerIRCBot):
    def __init__(self, user_name, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.user_name = user_name
        self.cont=0
        self.saidinha=False

        # pega o id do canal, vamos precisar disso para chamadas da api HORA_DA_VERDADE
        url = 'https://api.twitch.tv/kraken/users?login=' + self.user_name
        headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        resp = requests.get(url, headers=headers).json()
        # print(r)
        self.channel_id = resp['users'][0]['_id']

        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Conectando a ' + server + ' na porta ' + str(port) + '...')
        super().__init__([(server, port, 'oauth:' + token)], self.user_name, self.user_name)

    def on_welcome(self, c, e):
        print('Se juntando a ', self.channel)
        # Você deve pedir capacidades específicas antes de poder usa-las
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)
        c.privmsg(self.channel,"Agora o BoiRobot está on!")
        print('Me juntei...')

    def on_pubmsg(self, c, e):
        # Se uma mensagem de chat começa com ponto de esclamação, tente rodar ele como um comando
        tags={kvpair['key']:kvpair['value'] for kvpair in e.tags}
        #dados do usuario obtidos pela twitch
        user={'name':tags['display-name'], 'id':tags['user-id']}
        chamou=User(
            user['id'],
            user['name']
        )#classe
        insere_usuario(chamou)#inserir a classe
        insere_ponto(chamou)

        self.cont+=1
        if self.cont==10:
            aleatoria=["Bot helper: Tente um !ec",
                       "Bot helper: Tente um !dado",
                       "Bot helper: Tente um !agenda",
                       "Bot helper: Tente um !podium",
                       "!sh pachicodes",
                       "!sh kaduzius",
                       "!sh levxyca"]
            c.privmsg(self.channel,choice(aleatoria))
            self.cont=0
        
        if e.arguments[0][:1] == '!':
            print(e.arguments)
            comandos=e.arguments[0].split(' ')
            print('Argumentos: ', comandos)
            argumento1=''
            if len(comandos) > 1:
                argumento1=comandos[1]
                print(argumento1)
            # print(argumento1)
            print('Comando recebido: ' + argumento1)
            print('Comando recebido de: ' + user['name'])
            #chamou=user['name']
            comandos=comandos[0][1:]
            #print('Tirou ! ? ', comandos)
            self.faca_comando(e, comandos, chamou, argumento1)
        elif self.saidinha:
            c.privmsg(self.channel, 'O boirods deu uma saidinha e disse que volta logo, fique para conversar com ele!!')

        return
    
    def faca_comando(self, e, cmd, quem_chamou,argumentos):
        c=self.connection
        if cmd == 'cmds' or cmd == 'comandos':
            msgs='Veja meus comandos em https://boirobot.rregio.top!'
            c.privmsg(self.channel, msgs)
        elif cmd == 'ensinamentodocampo' or cmd == 'ensinamento' or cmd == 'ec':
            msg = pega_ensinamento()
            c.privmsg(self.channel, msg)
        elif cmd == 'insereensino' or cmd == 'iec':
            insere_ensinamento(quem_chamou,argumentos)
            mensagem='Ensinamento inserido com sucesso!'
            c.privmsg(self.channel, mensagem)
        elif cmd == 'agenda':
            msg = 'O boirods faz lives todos os finais de semana, não sei dizer os horários, mas faz... Fique de olho ;)'
            c.privmsg(self.channel, msg)
        elif cmd == 'dado':
            numero_gerado=randint(1,6)
            if numero_gerado != 1:
                msg=f'@{quem_chamou.displayName} seu numero é: '+str(numero_gerado)
                aumenta_pontos(quem_chamou, numero_gerado)
                c.privmsg(self.channel, msg)
            else:
                msg1=f'@{quem_chamou.displayName} seu numero é: 1'
                msg2='Seus pontos foram zerados, tente novamente!'
                zera_pontos(quem_chamou)
                c.privmsg(self.channel, msg1)
                c.privmsg(self.channel, msg2)
        elif cmd=='zerapontos':
            if quem_chamou.id == '548002631':
                print('Todos os pontos serão zerados!')
                zera_todos_pontos()
                c.privmsg(self.channel, 'Todos os pontos foram zerados!')
            else:
                c.privmsg(self.channel, '@'+quem_chamou.displayName+' você não tem autorização para executar este comando!')
        elif cmd == 'podium':
            maiores=pegaTresMaioresPontos()
            for maior in maiores:
                print(maior[0]+' tem '+str(maior[1])+" pontos!")
                c.privmsg(self.channel, maior[0]+' tem '+str(maior[1])+" pontos!")
        elif cmd == 'saidinha':
            if quem_chamou.id == '548002631':
                self.saidinha=True
                c.privmsg(self.channel,'Volte logo Boirods, tentarei deixar o povo em ordem!')
            else:
                c.privmsg(self.channel,'Este comando é para o streamer (se ele der uma saidinha)!')
        elif cmd == 'voltadinha':
            if quem_chamou.id == '548002631':
                self.saidinha=False
                c.privmsg(self.channel,'Que bom que voltou Boirods, não estava mais aguentando XD')
            else:
                c.privmsg(self.channel,'Não se exaltem, o Boirods ainda não voltou!!')
        else:
            print("Não entendi esse comando: " + cmd+" mas você pode me ensinar??")


def main():
    cfg=configparser.ConfigParser()
    cfg.read('data.ini')

    client_id = cfg.get('section1','CLIENT_ID')
    user_name = cfg.get('section1','BOT_NICK')
    token = cfg.get('section1','TMI_TOKEN')
    channel = cfg.get('section1','CHANNEL')
    print(f'Dados lidos:\nuser_name: {user_name}, \ncli_id: {client_id},\nToken: {token},\nCanal: {channel}')

    bot = BoiRobot(user_name, client_id, token, channel)
    bot.start()

if __name__ == '__main__':
    main()

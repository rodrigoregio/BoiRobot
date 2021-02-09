import sys
import configparser
import irc.bot as ibot
import requests
from random import randint


class BoiRobot(ibot.SingleServerIRCBot):
    def __init__(self, user_name, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.user_name = user_name

        # pega o id do canal, vamos precisar disso para chamadas da api
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        # print(r)
        self.channel_id = r['users'][0]['_id']

        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Conectando a ' + server + ' na porta ' + str(port) + '...')
        ibot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], user_name, user_name)

    def on_welcome(self, c, e):
        print('Se juntando a ', self.channel)

        # Você deve pedir capacidades específicas antes de poder usa-las
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)
        print(type(c))
        c.privmsg(self.channel,'Bom dia pessoal, sou o BoiRobot...')
        print('Me juntei...')

    def on_pubmsg(self, c, e):
        # print(type(e))
        # Se uma mensagem de chat começa com ponto de esclamação, tente rodar ele como um comando
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print('Comando recebido: ' + cmd)
            self.faca_comando(e, cmd)
        return

    def faca_comando(self, e, cmd):
        c = self.connection

        # pesquisa na api para retornar o jogo atual
        if cmd == 'game':
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitch.tv/v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, r['display_name'] + ' está jogando ' + r['game'] + ' agora!')
        elif cmd == 'title':
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitch.tv/v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, 'O canal ' + r['display_name'] + ' está com o título ' + r['status'] + ' agora!')
        elif cmd == 'mensagens':
            msg = 'Esta é uma mensagem aleatória, pode colocar para ele sortear uma mensagem aleatória!'
            c.privmsg(self.channel, msg)
        elif cmd == 'agenda':
            msg = 'O Boirods faz lives todos os dias ás 7 da manhã (horário de Brasilia)'
            c.privmsg(self.channel, msg)
        elif cmd == 'dado':
            msg='Seu numero é: '+str(randint(1,6))
            c.privmsg(self.channel,msg)
        else:
            print("Não entendi esse comando: " + cmd)


def main():
    # if len(sys.argv) != 5:
    #     print(
    #         'Para usar o bot são necessários 5 argumentos, são eles:\nusername: Nome do bot\nClient-ID: token do client id\nToken OAUTH: token recebido na twitch\nChannel: é o canal')
    #     sys.exit(1)

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

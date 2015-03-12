import re, sys, unicodedata, time, math
from twisted.internet import reactor
from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

################################################################################
########                        S e t t i n g s                         ########
################################################################################
identity = {
    'FoxBot': {
        'nickname': 'FoxBot',
        'realname': 'IRCBot',
        'username': '',
        'nickserv_pw': ''
    },
}
networks = {
    'SwiftIRC': {
        'host': '',
        'port': 6667,
        'ssl': False,
        'identity': identity['FoxBot'],
        'autojoin': (
            '',
            '',
        )
    },
}
"""  Format for Adding more networks
    'ExampleNet': {
        'host': '192.168.0.0',
        'port': 6667,
        'ssl': False,
        'identity': identity['sampleBot'],
        'autojoin': (
            'sample',
        )
    }
"""
################################################################################
log.startLogging(sys.stdout)

class TwistedBot(irc.IRCClient):

    admin = []
    start = 0

    def connectionMade(self):

        irc.IRCClient.connectionMade(self)
        print "Connection Established."

    def connectionLost(self, reason):

        irc.IRCClient.connectionLost(self, reason)
        print "Connection Lost."

    def signedOn(self):

        network = self.factory.network

        if network['identity']['nickserv_pw']:
            self.msg('NickServ', 'IDENTIFY %s' % network['identity']['nickserv_pw'])

        for channel in network['autojoin']:
            self.join(channel)

    def joined(self, channel):

        print("[I have joined %s]" %channel)

    def left(self, channel):

        print("[I have left %s]" %channel)

    def privmsg(self, user, channel, msg):

        timer = (time.time() - self.start)

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if channel == self.nickname:
            print('<%s> %s' % (usernick, msg))

            if msgParts[0].startswith(""):

                self.admin.append(host)
                msg = "You are now logged in for admin commands."
                self.msg(usernick, msg)
                msg = " "
                self.msg(usernick,msg)
                msg = "     \0034,1!join\003 \x1Fchannel\x1F   Joins channel specified"
                self.msg(usernick, msg)
                msg = "     \0034,1!leave\003            Leaves current channel"
                self.msg(usernick,msg)
                msg = "     \0034,1!logout\003           Logout of admin"
                self.msg(usernick, msg)

            else:

                msg = "Incorrect login, you fail."
                self.msg(usernick, msg)

        if (timer > 3) or host in self.admin:

            if msgParts[0].startswith("!join") and host in self.admin:

                channel = msgParts[1]
                self.join(channel)

            elif msgParts[0].startswith("!leave") and host in self.admin:

                if msg == "!leave":

                    msg = "Ok fine :("
                    self.msg(channel, msg)
                    self.part(channel)

                else:

                    channel1 = msgParts[1]
                    msg = "Leaving #" + msgParts[1]
                    self.msg(channel, msg)
                    self.part(channel1)

            elif msgParts[0].startswith("!login"):

                msg = "Password?"
                self.msg(usernick, msg)

            elif msgParts[0].startswith("!logout") and host in self.admin:

                self.admin.remove(host)
                msg = "You have been removed from admin list."
                self.msg(channel, msg)

            elif msgParts[0].startswith("!calc"):

                self.calc(user, channel, msg)

            else:

                self.commands(user, channel, msg)

        self.start = time.time()

    def commands(self, user, channel, msg):

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if msg == "!ping":

            msg = "\0038,1pong!"
            self.msg(channel, msg)
            print('<%s> %s' %(usernick, msg))

        elif msg == "!info":

            msg = "I am a bot, made by Fox. \002!info commands\002 for a list of commands."
            self.notice(usernick, msg)
            msg = "Will add more info at a later time."
            self.notice(usernick, msg)

        elif msg == "!info commands":

            msg1 = "List of user commands."
            msg2 = " "
            msg3 = "     !ping      Pong!"
            self.notice(usernick, msg1)
            self.notice(usernick, msg2)
            self.notice(usernick, msg3)

    def calc(self, user, channel, msg):

        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')



    def userJoined(self, user, channel):

        usernick = user.split('!', 1)[0]

        if usernick == 'inhaps':
            msg = "Hi, " + usernick
            self.msg(channel, msg)
            print "I said hi to inhaps!"

    def alterCollidedNick(self, nickname):

        return nickname + '^'

    def kickedFrom(self, channel, kicker, message):

        print "I was kicked. \nChannel: " + channel + "\nKicker: " + kicker + "\nReason: " + message
        self.join(channel)
        print "Attempting to rejoin " + channel

    def userRenamed(self, oldname, newname):
        """
        Called when a user changes there nick
        """
        print "%s is now %s" %(oldname, newname)

    def _get_nickname(self):
        return self.factory.network['identity']['nickname']

    def _get_realname(self):
        return self.factory.network['identity']['realname']

    def _get_username(self):
        return self.factory.network['identity']['username']

    nickname = property(_get_nickname)
    realname = property(_get_realname)
    username = property(_get_username)

class TwistedBotFactory(protocol.ClientFactory):

    protocol = TwistedBot

    def __init__(self, network_name, network):

        self.network_name = network_name
        self.network = network

    def clientConnectionLost(self, connector, reason):

        print('client connection lost')
        connector.connect()

    def clientConnectionFailed(self, connector, reason):

        print('client connection failed')
        reactor.stop()

if __name__ == '__main__':

    for name in networks.keys():

        factory = TwistedBotFactory(name, networks[name])

        host = networks[name]['host']
        port = networks[name]['port']

        if networks[name]['ssl']:
            reactor.connectSSL(host, port, factory, ssl.ClientContextFactory())
        else:
            reactor.connectTCP(host, port, factory)

    reactor.run()

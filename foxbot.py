import re,sys,unicodedata,time,math,httplib,urllib
from twisted.internet import reactor
from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc
from cmds.wolfram import Wolfram

import re
import config
#import FoxbotInterface

log.startLogging(sys.stdout)

class CmdData(object):
    def __init__(self, conn, user, channel, msg):
        self.conn = conn
        self.user = user
        self.channel = channel
        self.msg = msg
        
        self.host = user.split('!', 1)[1]
        self.usernick = user.split('!', 1)[0]
        
        self.cmd = self.getCmd()
    
    def validate(self):
        # make sure it's a valid cmd
        string = self.msg.split(' ')[0]
        return re.match(r"^([!@#$%^&*])([A-z]+)\s+(.*)$", string)
    
    def getCmd(self):
        # break the cmd into its parts
        string = self.msg.split(' ')[0] # gets the message
        regex = re.compile(r"^(?P<action>[!@#$%^&*])(?P<method>[A-z]+)\s+(?P<parameters>.*)$")
        match = regex.search(string)
        return match.groupdict()

class TwistedBot(irc.IRCClient):
    
    def __init__(self):
        
        # interface = FoxbotInterface()
        
        self.admin = []
        self.startTime = 0

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

        data = CmdData(self, user, channel, msg)
        
        timer = (time.time() - self.startTime)

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')
        print ("msgParts:", msgParts)
        
        if channel == self.nickname:

            self.adminLogin(user, channel, msg)

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

            elif msgParts[0].startswith("!logout") and host in self.admin:

                self.admin.remove(host)
                msg = "You have been removed from admin list."
                self.msg(channel, msg)

            elif msgParts[0].startswith(".google") or msgParts[0].startswith("!google"):

                if msgParts[0].startswith(".google"):
                    type = 0
                elif msgParts[0].startswith("!google"):
                    type = 1

                self.callGoog(user, channel, msg, type)
                
            elif msgParts[0].startswith(".wolf") or msgParts[0].startswith("!wolf"):
                
                if msgParts[0].startswith(".wolf"):
                    type = 0
                elif msgParts[0].startswith("!wolf"):
                    type = 1
                
                self.callWolf(user, channel, msg, type)

            else:
                self.commands(user, channel, msg)

        self.startTime = time.time()

    def commands(self, user, channel, msg):

        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if msg == "!ping":

            msg = "\0038,1pong!"
            self.msg(channel, msg)
            print('<%s> %s' %(usernick, msg))

        elif msg == "!info":

            msg = "I am a bot, made by Fox. \002!coms\002 for a list of commands."
            self.notice(usernick, msg)
            msg = "Will add more info at a later time."
            self.notice(usernick, msg)
        
        elif msg == "!coms":

            commands = "Commands: ping | goog | wolf"
            helpcom = "Use !help \002command\002 for help with a command."
            self.notice(usernick, commands)
            self.notice(usernick, helpcom)

        elif msgParts[0] == "!help":

            self.helpComs(user, channel, msg)
    
    def adminLogin(self, user, channel, msg):
        
        network = self.factory.network
        host = user.split('!', 1)[1]
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')
        
        print('<%s> %s' % (usernick, msgParts))

        if msg == ("!login %s" % network['identity']['adminPass']):

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

        elif msgParts[0].startswith("!login") and msg != ("!login %s" % network['identity']['adminPass']):
            
            msg = "Incorrect login, go away."
            self.msg(usernick, msg)

    def helpComs(self, user, channel, msg):

        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ')

        if msgParts[1] == "ping":

            msg = "Ping: Pong..."
            self.notice(usernick, msg)

        elif msgParts[1] == "google":

            msg = "Uses a google search"
            self.notice(usernick, msg)
        
        elif msgParts[1] == "wolf":
            
            msg = "Searches Wolfram Alpha... Wolfram knows all."
            self.notive(usernick, msg)
            
    def callWolf(self, user, channel, msg, type):
        
        network = self.factory.network
        usernick = user.split('!', 1)[0]
        msgParts = msg.split(' ', 1)
        appid = network['identity']['wolframID']
        query = msgParts[1]
        print('<%s> %s' % (usernick, msgParts))
        
        self.wolfram = Wolfram(appid, query)
        dataWolf = self.wolfram.search()
        
        if not dataWolf:
            print "Nothing Found"
            msg = "https://i.imgflip.com/62qwt.jpg"
            
            if type == 0:
                self.notice(usernick, msg)
            elif type == 1:
                self.msg(channel, msg)

        try: 
            msg = dataWolf['Result']
            if type == 0:
                self.notice(usernick, msg)
            elif type == 1:
                self.msg(channel, msg)
        except:
            for res in dataWolf:
                try:
                    msg = res+": "+dataWolf[res]
                    if type == 0:
                        self.notice(usernick, msg)
                    elif type == 1:
                        self.msg(channel, msg)
                except:
                    e = sys.exc_info()[0]
                    print ("Error: %s from: %s" %(e,res)) 
                
    def userJoined(self, user, channel):

        usernick = user.split('!', 1)[0]
        print "%s joined %s" %(usernick, channel)

    def alterCollidedNick(self, nickname):

        return nickname + '^'

    def kickedFrom(self, channel, kicker, message):

        print "I was kicked. \nChannel: " + channel + "\nKicker: " + kicker + "\nReason: " + message
        self.join(channel)
        print "Attempting to rejoin " + channel

    def userRenamed(self, oldname, newname):

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

    for name in config.networks.keys():

        factory = TwistedBotFactory(name, config.networks[name])

        host = config.networks[name]['host']
        port = config.networks[name]['port']

        if config.networks[name]['ssl']:
            reactor.connectSSL(host, port, factory, ssl.ClientContextFactory())
        else:
            reactor.connectTCP(host, port, factory)

    reactor.run()

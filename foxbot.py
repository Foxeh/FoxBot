import re,sys,unicodedata,time,math,httplib,urllib,traceback
from twisted.internet import reactor
from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc
from cmds.wolfram import Wolfram

import config
from foxbotinterface import FoxbotInterface

log.startLogging(sys.stdout)

class CmdData(object):
    '''
        A data object for holding the infomation to pass to plugins.
    '''
    def __init__(self, conn, user, channel, msg):
        self.msg = msg
        self.valid = self.validate()

        if(self.valid):
            self.conn = conn
            self.user = user
            self.channel = channel
            self.host = user.split('!', 1)[1]
            self.usernick = user.split('!', 1)[0]
            self.admin = ["Driste"]
            self.cmd = self.getCmd()

            self.actionEnum = {
                "!" : "bang",
                "." : "dot",
                "?" : "question",
                "/" : "slash"
            } 

            # keylookup
            self.action = self.actionEnum[self.cmd['action']]
    
    def validate(self):
        # make sure it's a valid cmd
        return re.match(r"^[\W][\w]+\s*.*$", self.msg)
    
    def getCmd(self):
        # break the cmd into its parts
        regex = re.compile(r"^(?P<action>\W)(?P<method>\w+)\s*(?P<parameters>.*)$")
        match = regex.search(self.msg)
        return match.groupdict()

class TwistedBot(irc.IRCClient):
    
    def __init__(self):
        self.interface = FoxbotInterface()
        self.interface.start(reactor)
        
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
            print "here"
            
        for channel in network['autojoin']:
            self.join(channel)
            print "herechannel"

    def joined(self, channel):
        print("[I have joined %s]" %channel)

    def left(self, channel):
        print("[I have left %s]" %channel)

    def privmsg(self, user, channel, msg):
        timer = (time.time() - self.startTime)
        #if (timer > 3):
        print ("Incoming message: ", msg)
        d = CmdData(self, user, channel, msg)
        print ("Msg Validation: ", d.valid)
        if d.valid:
            try:
                # ex. !google = bang_google
                f = self.interface.getFunc(d.action + "_" + d.cmd["method"])
                resp = f(d)
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                stackTrace = traceback.format_exception(exc_type, exc_value,exc_traceback)
                for line in stackTrace:
                    print(line)
        
        del d
        
        self.startTime = time.time()
        
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
    print config.networks
    
    for name in config.networks.keys():
        print("name %s"%name)
        
        factory = TwistedBotFactory(name, config.networks[name])

        host = config.networks[name]['host']
        port = config.networks[name]['port']

        if config.networks[name]['ssl']:
            reactor.connectSSL(host, port, factory, ssl.ClientContextFactory())
        else:
            reactor.connectTCP(host, port, factory)

    reactor.run()

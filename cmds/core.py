import re,sys,unicodedata,time,math,httplib,urllib
import config
    
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
        
def ping(self, user, channel, msg):
    # !ping
    msg = "\0038,1pong!"
    print('<%s> %s' %(usernick, msg))
    return (channel, msg)

def info(self, user, channel, msg):
    # !info
    msg = "I am a bot, made by Fox. \002!coms\002 for a list of commands."
    return self.notice(usernick, msg)
    msg = "Will add more info at a later time."
    return self.notice(usernick, msg)
        
    
    def coms(self, user, channel, msg):
        # !coms
        commands = "Commands: ping | goog | wolf"
        helpcom = "Use !help \002command\002 for help with a command."
        self.notice(usernick, commands)
        self.notice(usernick, helpcom)
    
    def help(self, user, channel, msg):
        # !help
        pass
    
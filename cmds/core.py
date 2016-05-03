import re,sys,unicodedata,time,math,httplib,urllib
import config

from interface import Interface
    
class Core(Interface):
    def commands(self, data):
    
        host = data.user.split('!', 1)[1]
        usernick = data.user.split('!', 1)[0]
        msgParts = data.msg.split(' ')
    
        if data.msg == "!ping":
    
            data.msg = "\0038,1pong!"
            self.msg(data.channel, data.msg)
            print('<%s> %s' %(usernick, data.msg))
    
        elif data.msg == "!info":
    
            msg = "I am a bot, made by Fox. \002!coms\002 for a list of commands."
            self.notice(usernick, msg)
            msg = "Will add more info at a later time."
            self.notice(usernick, msg)
        
        elif data.msg == "!coms":
    
            commands = "Commands: ping | goog | wolf"
            helpcom = "Use !help \002command\002 for help with a command."
            self.notice(usernick, commands)
            self.notice(usernick, helpcom)
    
        elif msgParts[0] == "!help":
    
            self.helpComs(data.user, data.channel, data.msg)
            
    def pingtest(self, data):
        # !ping
        msg = "\0038,1pong!"
        print('<%s> %s' %(usernick, msg))
        return (data.channel, msg)
    
    def info(self, data):
        # !info
        msg = "I am a bot, made by Fox. \002!coms\002 for a list of commands."
        return self.notice(data.usernick, msg)
        msg = "Will add more info at a later time."
        return self.notice(data.usernick, msg)
            
        
    def coms(self, data):
        # !coms
        commands = "Commands: ping | goog | wolf"
        helpcom = "Use !help \002command\002 for help with a command."
        self.notice(usernick, commands)
        self.notice(usernick, helpcom)
    
    def help(self, data):
        # !help
        pass
        
import re,sys,unicodedata,time,math,httplib,urllib
import config

from cmds.admin import requiresAdmin
from interface import Interface
    
class Core(Interface):
    
    def bang_ping(self, data):
        # !ping
        msg = "\0038,1pong!"
        print('<%s> %s' %(data.usernick, msg))
        data.conn.msg(data.channel, msg)
    
    def bang_info(self, data):
        # !info
        msg = "I am a bot, made by Fox. \002!coms\002 for a list of commands."
        data.conn.notice(data.usernick, msg)
        msg = "Will add more info at a later time."
        data.conn.notice(data.usernick, msg)
            
        
    def bang_coms(self, data):
        # !coms
        commands = "Commands: ping | goog | wolf"
        helpcom = "Use !help \002command\002 for help with a command."
        data.conn.notice(data.usernick, commands)
        data.conn.notice(data.usernick, helpcom)
    
    def bang_help(self, data):
        # !help
        if data.cmd['parameters'] == "ping":

            msg = "Ping: Pong..."
            data.conn.notice(data.usernick, msg)

        elif data.cmd['parameters'] == "google":

            msg = "Uses a google search"
            data.conn.notice(data.usernick, msg)
        
        elif data.cmd['parameters'] == "wolf":
            
            msg = "Searches Wolfram Alpha... Wolfram knows all."
            data.conn.notice(data.usernick, msg)
    
    @requiresAdmin
    def bang_join(self, data):
        print "hittttt"
        #self.join(data.cmd['parameters'])
    
    @requiresAdmin
    def bang_leave(self, data):
        #if a parameter was given
        if data.cmd['parameters']:
            msg = "Leaving #" + data.cmd['parameters']
            data.conn.msg(data.channel, msg)
            data.conn.part(data.cmd['parameters'])
        else:
            msg = "Ok fine :("
            data.conn.msg(data.channel, msg)
            data.conn.part(data.channel)
    
    @requiresAdmin
    def bang_logout(self, data):
        data.conn.admin.remove(data.host)
        msg = "You have been removed from admin list."
        data.conn.msg(data.channel, msg)

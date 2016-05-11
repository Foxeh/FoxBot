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
    
    def bang_help(self, data):
        # !help
        helpLines = [
            'FoxBot Help:',
            '    Note: Add a "?" before a command for an example.',
            '        ex. ?google',
            'Available Commands:',
            '    !ping',
            '    !info'
        ]
        
        for k in self.registry: 
                if k not in ['foxbotinterface', 'core', 'admin']:
                    helpLines.append('    '+k)

        for line in helpLines:
            data.conn.msg(data.usernick, line)
        #data.conn.notice(data.usernick, msg)
    
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

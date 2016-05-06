import re,sys,unicodedata,time,math,httplib,urllib
import config

from functools import wraps
from interface import Interface

class Admin(Interface):
    
    def admin(self, data):
        pass
    
    def _adminLogin(self, user, channel, msg):
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
        
def requiresAdmin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = args[1]
        if data.usernick in data.admin:
            print ("user is an admin")
            return f(*args, **kwargs)
        print ("user not an admin")
        return None
    return decorated
    
    
    
    
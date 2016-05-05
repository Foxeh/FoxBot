import re,sys,unicodedata,time,math,httplib,urllib
from interface import Interface

class Google(Interface):
    
    def google(self, data):
        print ("hit@@")
        '''
        usernick = data.user.split('!', 1)[0]
        msgParts = data.msg.split(' ', 1)
    
        query=urllib.urlencode({'q':msgParts[1]})
        
        start='<h2 class="r" style="display:inline;font-size:138%">'
        end='</h2>'
    
        google=httplib.HTTPConnection("www.google.com")
        google.request("GET","/search?"+query)
        search=google.getresponse()
        data=search.read()
    
        if data.find(start)==-1:
            msg = "Follow link to find your answer: www.google.com/search?"+query
            
            if data.type == 0:
                data.conn.notice(usernick, msg)
            elif data.type == 1:
                data.conn.msg(data.channel, msg)
        
        else:
            begin=data.index(start)
            result=data[begin+len(start):begin+data[begin:].index(end)]
            result = result.replace("<font size=-2> </font>",",").replace(" &#215; 10<sup>","E").replace("</sup>","").replace("\xa0",",")
            
            if data.type == 0:
                data.conn.notice(usernick, result)
            elif data.type == 1:
                data.conn.msg(data.channel, result)
        '''
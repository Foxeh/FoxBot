import re,sys,unicodedata,time,math,httplib,urllib
from interface import Interface

class Google(Interface):
    
    def google(self, foxdata):
        
        print ("Google", foxdata.cmd)
    
        query=urllib.urlencode({'q':foxdata.cmd['parameters']})
        
        start='<h2 class="r" style="display:inline;font-size:138%">'
        end='</h2>'
    
        google=httplib.HTTPConnection("www.google.com")
        google.request("GET","/search?"+query)
        search=google.getresponse()
        data=search.read()
    
        if data.find(start)==-1:
            msg = "Follow link to find your answer: www.google.com/search?"+query
            if foxdata.cmd['action'] == ".":
                print foxdata.usernick
                foxdata.conn.notice(foxdata.usernick, msg)
            elif foxdata.cmd['action'] == "!":
                foxdata.conn.msg(foxdata.channel, msg)
        
        else:
            begin=data.index(start)
            result=data[begin+len(start):begin+data[begin:].index(end)]
            result = result.replace("<font size=-2> </font>",",").replace(" &#215; 10<sup>","E").replace("</sup>","").replace("\xa0",",")
            
            if foxdata.cmd['action'] == ".":
                foxdata.conn.notice(foxdata.usernick, "test")
            elif foxdata.cmd['action'] == "!":
                foxdata.conn.msg(foxdata.channel, "test")
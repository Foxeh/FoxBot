import re,sys,unicodedata,time,math,httplib,urllib
from interface import Interface

class Google(Interface):
    
    def _google(self, foxdata):
        
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
            return (msg, 0)
        return (msg, 1)

    def dot_google(self, foxdata):
        resp, err = self._google(foxdata)
        if not err:
            foxdata.conn.notice(foxdata.usernick, resp)
        else: 
            foxdata.conn.notice(foxdata.usernick, "Error fetching result.")

    def bang_google(self, foxdata):
        resp, err = self._google(foxdata)
        if not err:
            foxdata.conn.msg(foxdata.channel, resp)
        else: 
            foxdata.conn.msg(foxdata.channel, resp)
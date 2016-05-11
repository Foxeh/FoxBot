import re,sys,unicodedata,time,math,httplib,urllib
from interface import Interface

class Google(Interface):
    
    def _google(self, data):
        
        print ("Google", data.cmd)
    
        query=urllib.urlencode({'q':data.cmd['parameters']})
        
        start='<h2 class="r" style="display:inline;font-size:138%">'
        end='</h2>'
    
        google=httplib.HTTPConnection("www.google.com")
        google.request("GET","/search?"+query)
        search=google.getresponse()
        reader=search.read()
    
        if reader.find(start)==-1:
            msg = "Follow link to find your answer: www.google.com/search?"+query
            return (msg, 0)
        return (msg, 1)

    def dot_google(self, data):
        # .google
        resp, err = self._google(data)
        if not err:
            data.conn.notice(data.usernick, resp)
        else: 
            data.conn.notice(data.usernick, "Error fetching result.")

    def bang_google(self, data):
        # !google
        resp, err = self._google(data)
        if not err:
            data.conn.msg(data.channel, resp)
        else: 
            data.conn.msg(data.channel, "Error fetching result.")
            
    def question_google(self, data):
        # ?google
        '''
            Returns help for the roll plugin.
        '''

        helpLines = (
            'Google Help:',
            '    <!|.>google <search term>',
            'Example Google: ',
            '    !google foxeh/foxbot',
            'Result:',
            '    Follow link to find your answer: www.google.com/search?q=foxeh%2Ffoxbot'
        )

        for line in helpLines:
            data.conn.msg(data.channel, line)
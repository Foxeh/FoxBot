import re,sys,unicodedata,time,math,httplib,urllib

def callGoog(self, user, channel, msg, type):

    usernick = user.split('!', 1)[0]
    msgParts = msg.split(' ', 1)

    query=urllib.urlencode({'q':msgParts[1]})
    
    start='<h2 class="r" style="display:inline;font-size:138%">'
    end='</h2>'

    google=httplib.HTTPConnection("www.google.com")
    google.request("GET","/search?"+query)
    search=google.getresponse()
    data=search.read()

    if data.find(start)==-1:
        msg = "Follow link to find your answer: www.google.com/search?"+query
        
        if type == 0:
            self.notice(usernick, msg)
        elif type == 1:
            self.msg(channel, msg)
    
    else:
        begin=data.index(start)
        result=data[begin+len(start):begin+data[begin:].index(end)]
        result = result.replace("<font size=-2> </font>",",").replace(" &#215; 10<sup>","E").replace("</sup>","").replace("\xa0",",")
        
        if type == 0:
            self.notice(usernick, result)
        elif type == 1:
            self.msg(channel, result)

    
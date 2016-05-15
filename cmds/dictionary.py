import urllib,urllib2,httplib,json,csv,re
import config

from cmds.admin import requiresAdmin
from interface import Interface
    
class Dictionary(Interface):
    def start(self, *args, **kwargs):
        self.dicUri = "http://google-dictionary.so8848.com/meaning?word="
    
    def dot_def(self,data):
        self.bang_def(data)
    def bang_def(self,data):
        """
        Gives the first definition of a provided word.
        """
        # TODO: Use api to eliminate the parsing.
        try:
            response = urllib2.urlopen(self.dicUri+data.cmd['parameters'])
            response = response.read().replace('\n','').replace('\r','').replace('\t','')
            #print response
            r = r'.*?<li style="list-style:decimal">(?P<def>.*?)<.*'
            if(re.match(r, response)):
               match = re.search(r, response).groupdict()
               print match['def']
               data.conn.msg(data.channel, match['def']);
            
        except urllib2.HTTPError as e:
            data.conn.msg(data.channel, "Unable to access dictionary. Try again later, or check your internet.")
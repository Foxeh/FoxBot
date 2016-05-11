import urllib,urllib2,httplib
from xml.etree import ElementTree as etree

from interface import Interface

class Wolfram(Interface):
    
    def dot_wolf(self, data):
        pass
    
    def bang_wolf(self, data):
        pass
    
    def _wolf(self, data):
        
        print('<%s> %s' % (data.usernick, data.cmd['parameters']))
        dataWolf = self.registry['wolfram']._search(data)
        
        if not dataWolf:
            print "Nothing Found"
            msg = "https://i.imgflip.com/62qwt.jpg"
            
            if data.cmd['action'] == ".":
                data.conn.notice(data.usernick, msg)
            elif data.cmd['action'] == "!":
                data.conn.msg(data.channel, msg)

        try: 
            msg = dataWolf['Result']
            if data.cmd['action'] == ".":
                data.conn.notice(data.usernick, msg)
            elif data.cmd['action'] == "!":
                data.conn.msg(data.channel, msg)
        except:
            for res in dataWolf:
                try:
                    msg = res+": "+dataWolf[res]
                    if data.cmd['action'] == ".":
                        data.conn.notice(data.usernick, msg)
                    elif data.cmd['action'] == "!":
                        data.conn.msg(data.channel, msg)
                except:
                    e = sys.exc_info()[0]
                    print ("Error: %s from: %s" %(e,res)) 
     
    def _search(self, data):
        xml = self.registry['wolfram']._get_xml(data.cmd['parameters'], data.conn.factory.network['identity']['wolframID'])
        result_dics = self.registry['wolfram']._xmlparser(xml)
        return result_dics
 
    def _get_xml(self, query, appid):
        url_params = {'input':query, 'appid':appid}
        data = urllib.urlencode(url_params)
        req = urllib2.Request('http://api.wolframalpha.com/v2/query?', data, {'User-Agent':None})
        xml = urllib2.urlopen(req).read()
        return xml
 
    def _xmlparser(self, xml):
        data_dics = {}
        tree = etree.fromstring(xml)
        for e in tree.findall('pod'):
            for item in [ef for ef in list(e) if ef.tag=='subpod']:
                for it in [i for i in list(item) if i.tag=='plaintext']:
                    if it.tag=='plaintext':
                        data_dics[e.get('title')] = it.text
        return data_dics
    
    
    def question_wolf(self, data):
        self.registry['wolfram'].question_wolfram(data);
    def question_wolfram(self,data):
        # ?wolf or ?wolfram
        '''
            Returns help for the Wolfram plugin.
        '''

        helpLines = (
            'Wolf Help:',
            '    <!.>wolf <equation>',
            'Example Wolf: ',
            '    !wolf 2+2',
            'Result:',
            '    2+2=4'
        )

        for line in helpLines:
            data.conn.msg(data.channel, line)
 
if __name__ == "__main__":
    w = Wolfram()
      
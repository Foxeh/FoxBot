import urllib,urllib2,httplib
from xml.etree import ElementTree as etree

from interface import Interface

class Wolfram(Interface):
        
    def wolf(self, foxdata):
        
        print('<%s> %s' % (foxdata.usernick, foxdata.cmd['parameters']))
        dataWolf = self.registry['wolfram']._search(foxdata)
        
        if not dataWolf:
            print "Nothing Found"
            msg = "https://i.imgflip.com/62qwt.jpg"
            
            if foxdata.cmd['action'] == ".":
                foxdata.conn.notice(foxdata.usernick, msg)
            elif foxdata.cmd['action'] == "!":
                foxdata.conn.msg(foxdata.channel, msg)

        try: 
            msg = dataWolf['Result']
            if foxdata.cmd['action'] == ".":
                foxdata.conn.notice(foxdata.usernick, msg)
            elif foxdata.cmd['action'] == "!":
                foxdata.conn.msg(foxdata.channel, msg)
        except:
            for res in dataWolf:
                try:
                    msg = res+": "+dataWolf[res]
                    if foxdata.cmd['action'] == ".":
                        foxdata.conn.notice(foxdata.usernick, msg)
                    elif foxdata.cmd['action'] == "!":
                        foxdata.conn.msg(foxdata.channel, msg)
                except:
                    e = sys.exc_info()[0]
                    print ("Error: %s from: %s" %(e,res)) 
     
    def _search(self, foxdata):
        xml = self.registry['wolfram']._get_xml(foxdata.cmd['parameters'], foxdata.conn.factory.network['identity']['wolframID'])
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
 
if __name__ == "__main__":
    w = Wolfram()
      
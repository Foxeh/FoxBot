import urllib,urllib2,httplib,json
from xml.etree import ElementTree as etree

from interface import Interface

class Runescape(Interface):
    def start(self, *args, **kwargs):
        self.geUri = "http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=" #4798
        self.hsUri = "http://services.runescape.com/m=hiscore/index_lite.ws?player=" #67
        self.mobUri = "http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid=" #49
        
    def bang_ge(self,data):
        data.conn.msg(data.usernick, self.geUri)
        
    def bang_hs(self,data):
        data.conn.msg(data.usernick, self.hsUri)
        
    def bang_mob(self,data):
        
        print ("result: ", urllib2.urlopen(self.mobUri+data.cmd['parameters']).read())
        response = urllib2.urlopen(self.mobUri+data.cmd['parameters']).read()
        if (response):
            result = json.loads(response)
            resp = result['name'] + " | Level " + str(result['level']) + " | Lifepoints: " + str(result['lifepoints']) + " | Weakness: " + result['weakness'] + " | XP: " + result['xp']
            data.conn.msg(data.channel, resp.encode('utf-8'))
        else:
            data.conn.msg(data.channel, "No Beast with id = "+data.cmd['parameters'])
        
    def question_mob(self,data):
        helpLines = (
            'Runescape Mob Lookup Help:',
            '    <!.>mob <item id>',
            'Example Mob Lookup: ',
            '    !mob 49',
            'Result:',
            '    Hellhound | Level: 92 | Lifepoints : 3300 | Weakness : Slashing | XP: 344.4'
        )

        for line in helpLines:
            data.conn.msg(data.usernick, line)
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
        result = json.loads(urllib2.urlopen(self.mobUri+data.cmd['parameters']).read())
        resp = result['name'] + " | " + str(result['level']) + " | " + str(result['lifepoints']) + " | " + result['weakness'] + " | " + result['xp']
        data.conn.msg(data.channel, resp.encode('utf-8'))
        
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
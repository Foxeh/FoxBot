import urllib,urllib2,httplib,json,csv

from interface import Interface

class Runescape(Interface):
    def start(self, *args, **kwargs):
        self.geUri = "http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=" #4798
        self.mobUri = "http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid=" #49
        self.hsUri = "http://services.runescape.com/m=hiscore/index_lite.ws?player=" #67
        self.skills = ("Tot", "Att", "Def", "Str", "HP", "Rng", "Pray", "Mage", "Cook", "WC", "Flch", "Fish", "FM", 
                      "Craft", "Smith", "Mine", "Herb", "Agil", "Thiev", "Slay", "Farm", "RC", "Hunt", "Con", "Sum", 
                      "Dung", "Div")
        
    def bang_ge(self,data):
        data.conn.msg(data.usernick, self.geUri)
        
    def bang_hs(self,data):
        try:
            response = urllib2.urlopen(self.hsUri+data.cmd['parameters'])
            msg = ""
            rows = response.read().splitlines()
            for i,skill in enumerate(self.skills): # enumerate adds a counter (i) to the iterable (self.skills).
                r = rows[i].split(",") # rank, lvl, xp
                if r[0] == -1:
                    continue
                msg += skill + " " + str(r[1]) + " | "
            data.conn.msg(data.channel, msg[:-1])
        except urllib2.HTTPError as e:
            data.conn.msg(data.channel, "User not found.")
        
    def bang_mob(self,data):
        f = file('../mobData.dat')
        for line in f:
            mob = line.split(' ', 1)[1].rstrip()
            if data.cmd['parameters'].lower() == mob.lower():
                num = line.split(' ', 1)[0]

        response = urllib2.urlopen(self.mobUri+num).read()
        attrs = (("","name"), (" | LVL ","level"), (" | HP ","lifepoints"), (" | XP ","xp"), (" | Weakness: ","weakness"))
        if response:
            result = json.loads(response)
            msg = ""
            for label,attr in attrs:
                if attr in result:
                    if type(result[attr]) is int:
                        result[attr] = str(result[attr])
                    msg += label + result[attr]
            data.conn.msg(data.channel, msg.encode('utf-8'))
        else:
            data.conn.msg(data.channel, "No Beast with id = "+data.cmd['parameters'])
        
    def question_mob(self,data):
        helpLines = (
            'Runescape Mob Lookup Help:',
            '    <!.>mob <mobName>',
            'Example Mob Lookup: ',
            '    !mob hellhound',
            'Result:',
            '    Hellhound | Level: 92 | Lifepoints : 3300 | Weakness : Slashing | XP: 344.4'
        )

        for line in helpLines:
            data.conn.msg(data.usernick, line)
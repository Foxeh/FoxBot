import json,urllib2
from warnings import catch_warnings

class MobUpdate(object):
    
    def __init__(self):
        self.mobUri = "http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid="
        self.f = open('mobData.dat', 'w+')
        
    def updater(self):
        x=0
        while True:
            try:
                x+=1
                print 'here ' + str(x)
                result = json.loads(urllib2.urlopen(self.mobUri+str(x)).read())
                resp = str(x) + "," + result['name']
                self.f.write(resp + '\n')
                
                if y == '10':
                    break
                y=0
                
            except ValueError:
                y+=1
                print 'error'

if __name__ == '__main__':
    m = MobUpdate()
    m.updater()
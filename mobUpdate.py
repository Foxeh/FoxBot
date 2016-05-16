import json,urllib2
from warnings import catch_warnings

class MobUpdate(object):
    
    def __init__(self):
        self.mobUri = "http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid="
        self.f = open('mobData.dat', 'w+')
        
    def updater(self):
        x=0
        y=0
        print 'Starting, this may take awhile.'
        while True:
            try:
                x+=1
                response = urllib2.urlopen(self.mobUri+str(x)).read()
                if (response):
                    result = json.loads(response)
                    resp = str(x) + "," + result['name']
                    self.f.write(resp + '\n')
                    y=0
                else:
                    y +=1
                    if y == '10':
                        break
            except ValueError:
                y+=1
                if y == '10':
                    break
                
        print 'Jobs Done'
        
if __name__ == '__main__':
    m = MobUpdate()
    m.updater()
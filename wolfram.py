import urllib,urllib2,httplib
from xml.etree import ElementTree as etree
 
class wolfram(object):
        
    def __init__(self, appid, query):
        self.appid = appid
        self.query = query
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}
     
    def search(self):
        xml = self._get_xml(self.query)
        result_dics = self._xmlparser(xml)
        return result_dics
 
    def _get_xml(self, query):
        url_params = {'input':self.query, 'appid':self.appid}
        data = urllib.urlencode(url_params)
        req = urllib2.Request(self.base_url, data, self.headers)
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
    w = wolfram()
      
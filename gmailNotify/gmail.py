from lxml import etree
import urllib2
xhtml = etree.Element('')
url = "http://192.168.0.8"
page=urllib2.urlopen(url).read()
x=etree.HTML(page)
notice=x.xpath('//td[@class="titleColumn"]/a/@href')
# r = requests.post('http://210.212.85.155',params=parameters)
print r.content
print 
print 
print 
print 
print r.status_code
f = open('result.html','w')
f.write(str(r.content))
f.close()
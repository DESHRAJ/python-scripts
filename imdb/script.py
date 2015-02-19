import requests
movieName = raw_input()
movieName = movieName+"+imdb"
# r = requests.get('https://www.google.co.in/q='+movieName.replace(' ','+'))
r = requests.get('https://www.google.co.in/#q=interstellar+imdb')
content = r.content
print content
f = open('page.html','w')
f.write(content)
f.close()
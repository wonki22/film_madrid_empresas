from urllib.request import urlopen

url = "http://www.madrid.org/filmmadrid/data/empresas.min.js"

data = urlopen(url)

js_text = ""
f = open("empresas.js", "w")

for line in data:
    js_text += line.decode('utf-8')
    
f.write(js_text)

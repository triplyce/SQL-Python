import re
import codecs

f = codecs.open('sample.html', 'r', 'utf-8')

pattern = re.compile(r'\b(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&@#/%=~_|$?!:,.]*[A-Z0-9+&@#/%=~_|$].listing',flags=re.IGNORECASE)
pattern_gps = re.compile(r'-?[0-9]{1,3}(?:\.[0-9]{1,10})?')

text = f.read()

text_link = '\n'.join(pattern.findall(text))

text_gps = '\n'.join(re.findall(r'.*gps.*',text))

text_gps = '\n'.join(pattern_gps.findall(text_gps))

text_gps = 'latitude: ' + text_gps[:11] + '\nlongitude: ' + text_gps[11:]
text_regex = text_link + '\n' + text_gps

txt_final = open('regular.txt','w')

txt_final.write(text_regex)

f.close()
txt_final.close()





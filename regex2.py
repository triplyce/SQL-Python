import re
import json

text = json.load(open('sample.json'))

f = json.dumps(text)

pattern = re.compile(r'[A-Z]{2}[0-9]{3}')

pattern2 = re.compile(r"(\Wland\W*ESP\W)")


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

ids = list(set(pattern.findall(f)))
ids_ESP = []

for key, value in recursive_items(text):
	if key in ids:
		if (pattern2.findall(json.dumps(value))):
			ids_ESP.append(key)

regular2 = 'ids: ' + str(ids) + '\nids with ESP: ' + str(ids_ESP) 
txt_final = open('regular2.txt','w')

txt_final.write(regular2)

txt_final.close()

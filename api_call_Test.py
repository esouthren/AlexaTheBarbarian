import json
import urllib.request

def get_data_from_url(url):
    # Give me a url, returns a nice JSON object of that data
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))
'''
classes_data = get_data_from_url("http://www.dnd5eapi.co/api/classes/")
classes_count = classes_data['count']

classes = []
for i in range(0, classes_count):
    classes.append(get_data_from_url(classes_data['results'][i]['url']))

for c in classes:
    print(c['name'])

print("")
barbarian = classes[0]
for key, value in barbarian.items():
    print("{} : {}".format(key, value))


print("\nhit dice of barbarian: {} ".format(classes[0]['hit_die']))
'''

races_data = get_data_from_url("http://www.dnd5eapi.co/api/races/")
races_count = races_data['count']
races = []
for i in range(0, races_count):
    races.append(get_data_from_url(races_data['results'][i]['url']))

for c in races:
    print(c['name'])

print("")
barbarian = races[0]
for key, value in barbarian.items():
    print("{} : {}".format(key, value))

import json
import urllib.request

def get_data_from_url(url):
    # Give me a url, returns a nice JSON object of that data
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))

class API():
    def __init__(self):
        self.classes = []
        self.races = []


    def get_classes(self):
        classes_data = get_data_from_url("http://www.dnd5eapi.co/api/classes/")
        classes_count = classes_data['count']
        for i in range(0, classes_count):
            self.classes.append(get_data_from_url(classes_data['results'][i]['url']))


    def get_races(self):
        races_data = get_data_from_url("http://www.dnd5eapi.co/api/races/")
        races_count = races_data['count']
        for i in range(0, races_count):
            self.races.append(get_data_from_url(races_data['results'][i]['url']))



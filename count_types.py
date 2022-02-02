
import json
import os
import sys

list_of_types = []
list_of_dictionaries = []


def extract_type(filename):
    with open(filename) as f:
        data = json.loads(f.read())
    return data['data']['type']


def read_files():
    for root, dirs, files in os.walk('temp'):
        for file in files:
            fullpath = os.path.join(root, file)
            update_values(fullpath)


def update_values(fullpath):
    if extract_type(fullpath) not in list_of_types:
        list_of_types.append(extract_type(fullpath))
        list_of_dictionaries.append(make_dictionary(extract_type(fullpath)))
    else:
        dictionary = next(item for item in list_of_dictionaries if item["type"] == extract_type(fullpath))
        dictionary['count'] += 1


def make_dictionary(key):
    return {"type": key, "count": 1}


try:
    read_files()
    file = open('type_counts.json', 'w')
    json.dump(list_of_dictionaries, file)
    file.close()

except Exception as e:
    file = open('error.txt', 'w')
    file.write("Error: %s" % e)
    file.close()

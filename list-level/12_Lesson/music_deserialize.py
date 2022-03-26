import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
    print(json.load(f))

with open('group.pickle', 'rb') as f:
    print(pickle.load(f))

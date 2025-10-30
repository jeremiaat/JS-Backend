import json

with open("data_utf8.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))
print(data[:5])

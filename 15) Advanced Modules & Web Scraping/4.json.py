""" Dictionary Yapısı """

person = {"name":"Ali", "languages":["python","C#"]}

# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

# print(result)

""" JSON Yapısı """

import json

person_string = '{"name":"Ali", "languages":["python","C#"]}'

# JSON string to Dict

# result = json.loads(person_string)
# result = result["name"]

# print(result)

# with open("person.json") as f:
#      data = json.load(f)
#      print(data)
#      print(data["name"])

person_dict = {
     "name": "Ali",
     "languages": ["Python", "Java"]
}

# Dict to JSON String

# result = json.dumps(person_dict)   

# print(result)
# print(type(result))

# with open("person.json","w")as f:
#      json.dump(person_dict,f)


person_dict = json.loads(person_string)

result = json.dumps(person_dict,indent=4,sort_keys= True)

print(person_dict)
print(result)


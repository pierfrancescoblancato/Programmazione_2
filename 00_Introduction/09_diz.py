list = ["GM",25 ,"M"]

dict = {"key": "value","name": "gm", "age": 25, "gender": "m" }

print(dict)
print(type(dict))
print(dict["name"])

print(dict.get("name","NAN"))

key = input("cosa vuoi sapere: ")
print(dict.get(key,"NAN"))

if not "citta" in dict:
    dict["citta"] = "catania"

print(dict)

gender = dict.pop("gender")
print(gender)
print(dict)

print(dict.clear)

print(len(dict))
print(sorted(dict))

for key in dict.keys():
    print(dict[key])

for value in dict.values():
    print(key,dict[key])
import json
path = "myfile.json"
try:
    file = open(path,"r")
    d = json.load(file)
    file.close()
except:
    d = {}
print(d)
newKey = input("Type in a new key")
newVal = input("Type in a new value")
d[newKey] = newVal
file = open(path,"w")
json.dump(d,file)
file.close()

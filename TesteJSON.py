import json 


#Loads

x = '{"name":"Giovanna", "age":20}'

y = json.loads(x)

##print(y["age"])
##print(y)

#Dumps 

x = {
    "name":"Giovanna",
    "age":20,
    "name":"afafa",
    "age":20,
    "name":"das",
    "age":20
}

y = json.dumps(x, indent = 3,sort_keys=True)

print(y)

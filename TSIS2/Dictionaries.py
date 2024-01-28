thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.get("model")

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)  


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
  

thisdict.update({"year": 2020})


 
thisdict.pop("model")


#Loop throug dict
for x in thisdict:
  print(x)
#or
for x in thisdict.keys():
  print(x)
 
 
  
for x in thisdict:
  print(thisdict[x]) 
#or
for x in thisdict.values():
  print(x)
  
  
for x, y in thisdict.items():
  print(x, y)
  
  
  
#Nested 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

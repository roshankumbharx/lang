from typing import TypedDict

class Person(TypedDict):
    
    name:str
    age:int
    
    
p1=Person({'name':'kaiji','age':23})

print(p1)
print(type(p1))
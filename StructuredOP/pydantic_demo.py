from pydantic import BaseModel,Field,EmailStr
from typing import Optional


class Student(BaseModel):
    name:str
    age:Optional[int] = None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,description='Cgpa of the student till date')

new_std = {'name':'roshan','email':'abc@gmail.com','cgpa':8}

student = Student(**new_std)
print(student)
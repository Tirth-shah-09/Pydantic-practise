from pydantic import BaseModel


class Address(BaseModel):
    state:str
    city:str
    pincode:int


class User(BaseModel):
    name:str
    age:int
    hometown:str
    address:Address


address_dict={
    'state':'gujarat',
    'city':'Talod',
    'pincode':383215
}
user_dict={
    'name':'Tirth',
    'age':19,
    'hometown':'Talod',
    'address':address_dict
}
user_obj=User(**user_dict)

# obj=user_obj.model_dump_json(exclude=['name'])
# print(obj)
# print(type(obj))
print(user_obj)
print(type(user_obj))

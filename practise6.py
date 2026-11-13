from pydantic import BaseModel


class Address(BaseModel):
    state:str
    city:str
    pincode:int


class Shop(BaseModel):
    name:str 
    owner:str
    address:Address


address_dict={
    'state':'Gujarat',
    'city':'Talod',
    'pincode':383215
}
shop_dict={
    'name':'Radhika Stationery',
    'owner':'Bhavin Shah',
    'address':address_dict
}

def insert_at_db(shop:Shop):
    print(shop)
    print("Insertion Done")

shop_obj= Shop(**shop_dict)
insert_at_db(shop_obj)






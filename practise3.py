from pydantic import BaseModel,field_validator


#Model for a stationery shop
class ShopModel(BaseModel):
    name:str
    owner:str
    contact_nu:int
    address:str
    sales:int

    @field_validator('sales',mode='before')
    @classmethod
    def validate_sales(cls,sales):
        if(type(sales)=='int'):
            return sales
        suffix=sales[-1]
        if(suffix=='K' or suffix=='k'):
            sales=sales[:-1]
            sales+='000'
        return int(sales)

    @field_validator('contact_nu')
    @classmethod
    def validate_contact(cls,number):
        number=str(number)
        if(len(number)!=10):
            raise TypeError('Not a valid number')
        return number
        

dictionery={
    'name':'Radhika Stationery',
    'owner':'Bhavin Shah',
    'contact_nu':989816874,
    'address':'Near Nagarpalika , main bazar Talod',
    'sales':'1000K'
}

def insertion(document):
    print(document)
    print("Insertion Done")

shop=ShopModel(**dictionery)
insertion(shop)

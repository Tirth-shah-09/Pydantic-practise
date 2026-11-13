#A Patient Model
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='give' \
    'the name of patient in less than 50 chars')]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=0,lt=80)
    weight:Annotated[float, Field(gt=0)]
    married:Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]


def insert_patient_data(patient:Patient):
    print(patient)
    print('Insertion Done')

def update_patient_data(patient:Patient):
    print(Patient)
    print('Updation done')


dict={
    'name':'patient1',
    'email':'abc@gmail.com',
    'linkedin_url':'http://localhost',
    'age':8,
    'weight':'95',
    'contact_details':{'nu':'12334455'}

}
obj=Patient(**dict)
insert_patient_data(obj)

constraint=Annotated[int, Field(...,gt=0,lt=75)]
class User(BaseModel):
    name:str
    age:constraint
    email:str=Field(...,description='its the email of the user')


user_data={
    'name':'Tirth',
    'age':60,
    'email':'shahtirth9207@gmail.com'
}
user_obj=User(**user_data)
print(user_obj)
#A Patient Model
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
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



    @model_validator(mode='after')
    def validate_age_and_contactnus(self,model):   
        print("entered model_validator with mode=after")     
        if(self.age>60):
           if('emergency' not in self.contact_details):
               raise KeyError("emergerncy conatct needed for patients with age greater than 60")
        return self



    


def insert_patient_data(patient:Patient):
    print(patient)
    print('Insertion Done')

def update_patient_data(patient:Patient):
    print(Patient)
    print('Updation done')


dict={
    'name':'patient1',
    'email':'abc@hdfc.com',
    'linkedin_url':'http://localhost',
    'age':61,
    'weight':'-1',
    'contact_details':{'emergency':'12334455'}
}
obj=Patient(**dict)
insert_patient_data(obj)

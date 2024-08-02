#install the Required Library

!pip install Faker

from faker import Faker 

fake = Faker()

#storing the values into the variable
people = []

#allcating the index of the value
for i in range(50):
    name = fake.name() 
    age = fake.random_int(min=18, max=50)
    phone = fake.phone_number()
    people.append([name, age, phone])  

for person in people:
  print(f"name: {person[0]}, age: {person[1]}, phone: {person[2]}") 

#Coverting the data into the excel format
import pandas as pd
df=pd.DataFrame(people,columns=['name','age','phone'])
df.to_excel("people.xlsx",index=False)

#Downloading the sample data into the excel file
from google.colab import files
files.download('people.xlsx')


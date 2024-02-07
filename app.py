
from PIL import Image
import requests
import os

POINT = "https://randomuser.me/api/"    
req = requests.get(POINT).json()

info = req['results'][0]['name']['title']
name = req['results'][0]['name']['first']
last = req['results'][0]['name']['last']
gender = req['results'][0]['gender']
location = req['results'][0]['location']
street = location['street']
city = location['city']
country = location['country']
state = location['state']
vaqti = location['timezone']['offset']
a = location['timezone']['description']
email = req['results'][0]['email']
phone_num = req['results'][0]['phone']
cell_num = req['results'][0]['cell']

directory = f"{name},{last}"

os.mkdir(directory)
with open(f'{directory}/info.txt', 'w') as file:
    file.write(f'foydalanuvchi ismi: {name,last}\n')
    file.write(f"foydalanuvchi jinsi: {gender}\n")
    file.write(f"Manzili: {street['name']}, {street['number']}\n")
    file.write(f"Davlati:{country},Shaxri:{city},Viloyati:{state}\n")
    file.write(f"Davlati:{country},Shaxri:{city},Viloyati:{state}\n")
    file.write(f"Vaqt mitaqasi: {vaqti},vaqti bilan:{a}\n")
    file.write(f"Vaqt mitaqasi: {vaqti},vaqti bilan:{a}\n")
    file.write(f"Foydalanuvchi emaili:{email}\n")
    file.write(f"Foydalanuvchi telefon raqami:{phone_num}\n")
    file.write(f'Foydalanuvchi uy telefoni:{cell_num}')

img_url = req['results'][0]['picture']['large']
pic = requests.get(img_url).content

with open(f'{directory}/tasvir.jpg', 'wb') as file:
    file.write(pic)
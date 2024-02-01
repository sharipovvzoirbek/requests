import requests , os
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

print("foydalanuvchi ismi: ", info,name,last)

print(f"Jinsi: {gender}")

print(f"Manzili: {street['name']}, {street['number']}")

print(f"Davlati:{country},Shaxri:{city},Viloyati:{state}")

print(f"Vaqt mitaqasi: {vaqti},vaqti bilan:{a}")

print(f"Foydalanuvchi emaili:{email}")

print(f"Foydalanuvchi telefon raqami:{phone_num}")

print(f'Foydalanuvchi uy telefoni:{cell_num}')
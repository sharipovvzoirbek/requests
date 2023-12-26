import requests 

import os

respons = requests.get('https://random-data-api.com/api/v2/users').json()

user_id_str = str(respons['id'])

try:
    
    os.mkdir('users/'+user_id_str)

except FileExistsError:
    
    print('ushbu file mavjud')



# download avatar
img = open(f'users/{user_id_str}/avatar.png', 'wb')
img.write(requests.get(respons['avatar']).content)
img.close()


print(respons)

# write information about user
file = open(f'users/{user_id_str}/info.txt','w')

file.write(f"Foydalanuvhi ID si: {respons['id']} \n")

file.write(f"Foydalanuvchi uid si: {respons['uid']} \n")

file.write(f"Foydalanuvchi paroli: {respons['password']} \n")

file.write(f"Foydalanuvchi ismi: {respons['first_name']} \n")

file.write(f"Foydalanuvchi familiyasi: {respons['last_name']} \n")

file.write(f"Foydalanuvchi username-i: {respons['username']} \n")

file.write(f"Foydalanuvchi emeil-i: {respons['email']} \n")

file.write(f"Foydalanuvchi genderi: {respons['gender']} \n")

file.write(f"Foydalanuvchi raqami: {respons['phone_number']} \n")

file.write(f"Foydalanuvchi ijtimoiy raqami: {respons['social_insurance_number']} \n")

file.write(f"Foydalanuvchi tug'ulgan sanasi: {respons['date_of_birth']} \n")

work = respons['employment']

file.write(f"Foydalanuvchi  lavozimi: {work['title']},iqtidori: {work['key_skill']}   \n")

address = respons['address']

file.write(f"Foydalanuvchi manzili: Shahri: {address['city']},ko'cahsining ismi:{address['street_name']},ko'chasining manzili:{address['street_address']} zip kodi:{address['zip_code']}, shtati: {address['state']}, davlati: {address['country']} \n")

cc = respons['credit_card']

file.write(f"Foydalanuvchi kredit karta raqami:{cc['cc_number']} \n")
           
obunalar = respons['subscription']

file.write(f"Foudalanuvchi palani: {obunalar['plan']}, Statusi: {obunalar['status']}, to'lov uslubi {obunalar['payment_method']}, \n")

#vazifa tugatildi.
import requests 
import os
respons = requests.get('https://random-data-api.com/api/v2/users').json()
try:
    os.mkdir('users')
except FileExistsError:
    print('ushbu file mavjud')


    
file = open('users/'+str(respons['id']),'w')
file.write(respons['first_name'])
file.write(respons['last_name'])
file.write(respons['username'])
file.write(respons['phone_number'])
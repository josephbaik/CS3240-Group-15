import urllib3, os, json, requests
from Decrypter import decrypt_file
from requests.auth import HTTPBasicAuth

user = input("Username: ")
password = input("Password: ")
login = requests.post('http://127.0.0.1:8000/requestlogin/', {'username':user, 'password':password})
print(login.status_code)
for key in login.cookies.keys():
    print(key)
    print(login[key])
g = requests.get('http://127.0.0.1:8000/requestgroups')
groupDict = g.json()
print(g.text)
for i in groupDict['groups']:
    print(i)

fname = input("What is the name of the file you would like to download?: ")
key = input("Please specify an AES-256 security key: ")
name = input("Please specify an output file name/location: ")
resp = urllib3.PoolManager().request('GET', ("https://github.com/josephbaik/CS3240-Group-15/raw/master/"+fname))
output = open("temp.txt", 'wb')
output.write(resp.data)
output.close()
decrypt_file(key, "temp.txt", name)
os.remove("temp.txt")

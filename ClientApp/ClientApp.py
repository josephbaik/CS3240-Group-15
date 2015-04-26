import urllib3, os, json, requests, getpass
from Decrypter import decrypt_file
from requests.auth import HTTPBasicAuth

user = input("Username: ")
password = getpass.getpass("Password: ")
login = requests.post('http://127.0.0.1:8000/requestlogin/', {'username':user, 'password':password})
r = requests.get('http://127.0.0.1:8000/requestreports', cookies=login.cookies)

reportDict = r.json()
print("You have access to the following reports:")
for i in reportDict['reports']:
    print("    %s" %i)
print("Which report would you like to download?")
title = input("What is the name of the file you would like to download?: ")

#Once you can download files, this line will do the actual acquisition to the url.
#resp = urllib3.PoolManager().request('GET', ("https://github.com/josephbaik/CS3240-Group-15/raw/master/"+fname))

output = open("temp.txt", 'wb')
output.write(resp.data)
output.close()
decrypt_file(key, "temp.txt", name)
os.remove("temp.txt")

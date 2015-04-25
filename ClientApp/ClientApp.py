import urllib3, os, json, requests, getpass
from Decrypter import decrypt_file
from requests.auth import HTTPBasicAuth

user = input("Username: ")
password = getpass.getpass("Password: ")
login = requests.post('http://127.0.0.1:8000/requestlogin/', {'username':user, 'password':password})
#g = requests.get('http://127.0.0.1:8000/requestgroups', cookies=login.cookies)
r = requests.get('http://127.0.0.1:8000/requestreports', cookies=login.cookies)
"""
groupDict = g.json()
print("You are a member of the following groups:")
for i in groupDict['groups']:
    print("    %s" %i)
print("For which groups would you like to view your reports?")
"""

reportDict = r.json()
print("You have access to the following reports:")
for i in reportDict['reports']:
    print("    %s" %i)
print("Which report would you like to download?")

fname = input("What is the name of the file you would like to download?: ")
key = input("Please specify an AES-256 security key: ")
name = input("Please specify an output file name/location: ")
resp = urllib3.PoolManager().request('GET', ("https://github.com/josephbaik/CS3240-Group-15/raw/master/"+fname))
output = open("temp.txt", 'wb')
output.write(resp.data)
output.close()
decrypt_file(key, "temp.txt", name)
os.remove("temp.txt")

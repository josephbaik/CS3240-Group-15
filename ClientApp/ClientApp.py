import urllib2, os
from Decrypter import decrypt_file

fname = raw_input("What is the name of the file you would like to download?: ")
key = raw_input("Please specify an AES-256 security key: ")
name = raw_input("Please specify an output file name/location: ")
infile = urllib2.urlopen(("https://github.com/josephbaik/CS3240-Group-15/raw/master/"+fname))
output = open("temp.txt", 'wb')
output.write(infile.read())
output.close()
decrypt_file(key, "temp.txt", name)
os.remove("temp.txt")

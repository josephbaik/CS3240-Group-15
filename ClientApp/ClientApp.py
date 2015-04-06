import urllib2
from Encrypter import encrypt_file
from Encrypter import decrypt_file

fname = input("What is the name of the file you would like to download?")
key = input("Please specify an AES-256 security key.")
name = input("Please specify an output file name/location.")
infile = urllib2.urlopen(("https://github.com/josephbaik/CS3240-Group-15"+fname))
output = open(fname, 'wb')
output.write(infile.read)
decrypt_file(key, fname, fname)

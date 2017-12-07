import hashlib
import os
from base64 import *
os.system('cls' if os.name == 'nt' else 'clear')
os.system('color a' if os.name == 'nt' else 'clear')
def main():
 print '''
 ElCryptor is a tool to encrypt a string to MD5-BASE64-SHA1-SHA512-SHA384-SHA256-SHA224
 Created BY Saber Sebri
 '''
def sha512():
 heni =raw_input("give me the string sir\n[>]")
 sexynova = heni.encode("utf-8")
 baenova = hashlib.sha512( sexynova )
 zab = baenova.hexdigest()
 print "the sha512 of ",heni,"is ",zab 
def sha384():
 nova =raw_input("give me the string sir\n[>]")
 drnova = nova.encode("utf-8")
 xnovax = hashlib.sha384( drnova )
 pornhd = xnovax.hexdigest()
 print "the sha384 of ",nova,"is ",pornhd 
def sha256():
 nigga =raw_input("give me the string sir\n[>]")
 birra = nigga.encode("utf-8")
 xvideos = hashlib.sha256( birra )
 pornhub = xvideos.hexdigest()
 print "the sha256 of ",nigga,"is ",pornhub
def sha1():
 tay =raw_input("give me the string sir\n[>]")
 yat = tay.encode("utf-8")
 hem = hashlib.sha224( yat )
 xnxx = hem.hexdigest()
 print "the sha1 of ",tay,"is ",xnxx
def sha224():
 lu =raw_input("give me the string sir\n[>]")
 oh = lu.encode("utf-8")
 no = hashlib.sha224( oh )
 efrez = no.hexdigest()
 print "the sha224 of ",lu,"is ",efrez
def nouna():
 zeb =raw_input("give me the string sir\n[>] ")
 porn = zeb.encode("utf-8")
 nika = hashlib.md5( porn )
 nik = nika.hexdigest()
 print "The MD5 Crypt of ",zeb, (nik)
 return
os.system('cls' if os.name == 'nt' else 'clear')
main()
print "hello sir please choose what you need : "
print "[1]MD5"
print "[2]BASE64"
print "[3]SHA"
ch =raw_input("\n[>]")
if ch == '1':
 nouna()
if ch == '2':
 print "[1] written text"
 print "[2] php code"
 ch2=raw_input("\n[>] ")
 if ch2 == '1' :
   print " give me a string"
   a =raw_input()
   print b64encode(a)
   text = b64encode(a)
   saveFile = open('b64elcryptor.txt','w')
   saveFile.write(text)
   saveFile.close()
   print "saved in b64elcrpyot.txt"
 if ch2 == '2':
  print " the file name"
  b =raw_input()
  f = open(b,'r')
  content = f.read()
  f.close()
  content = b64encode(content)
  print 'result is ',content
  zeb = open('b64elcryptor.php','w')
  zeb.write(content)
  zeb.close()
  print "Saved in b64elcryptor.php"
if ch == '3':
 print "[1]SH1"
 print "[2]SHA224"
 print "[3]SHA256"
 print "[4]SHA384"
 print "[5]SHA512"
 gaith =raw_input("\n[>] ")
 if gaith == '1':
  sha1()
 if gaith == '2':
  sha224()
 if gaith == '3':
  sha256()
 if gaith == '4':
  sha384()
 if gaith == '5':
  sha512()
print "[1]repeat ?"
print "[2]exit"
ch1 = raw_input("\n[>]")
if ch1 == '1':
 os.system('Cryptor.py' if os.name == 'nt' else 'python Cryptor.py')

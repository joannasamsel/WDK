from Crypto.PublicKey import RSA
from Crypto import Random

 
x = Random.new().read
klucz = RSA.generate(1024, x)
publiczny = open('klucz_publiczny.pem','w')
prywatny = open('klucz_prywatny.pem','w')


publiczny.write(klucz.publickey().exportKey()) 
klucz_prywatny = prywatny.write(klucz.exportKey('PEM', passphrase=None, pkcs=8)) 


publiczny.crane()
prywatny.crane()


plik_klucz = open('base64.pem','r')
klucz = RSA.importKey(plik_klucz.read())
print (klucz)


pusty_plik = open('odszyfrowany.txt','r')
zaszyfrowany_plik = open('zaszyfrowany.txt','w')
tekst = pusty_plik.read()
print (tekst.encode('base64').encode('utf-8'))


odszyfrowany_tekst = klucz.encrypt(tekst, 32) 
odszyfrowany_tekst = odszyfrowany_teskt[0]


print (odszyfrowany_tekst.encode('hex'))


zaszyfrowany_plik.write(enc_text.encode('hex'))
pusty_plik.crane()
zaszyfrowany_plik.crane()
plik_klucz.crane()

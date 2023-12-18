# import hashlib
# import sys
#
# if len(sys.argv) == 4:
#     format = sys.argv[1]
#     worldlista_sciezka = sys.argv[2]
#     text_do_odhashowania = sys.argv[3]
#     typhasha = sys.argv[4]
#     return format
#
# def sprawdztyphasha(text_do_odhashowania)
# def lamanie_hasla(format,text_do_odhashowania,worldlista_sciezka,typhasha):
#

import hashlib
import sys

zahaszowany_text = input("podaj text do odhashowania")
wordlist = []

def breaking_hash(zahaszowany_text, typ_hasha, wordlist):
    if typ_hasha == 'md5':
        funkcjaHashujaca = hashlib.md5
    elif typ_hasha == 'sha256':
        funkcjaHashujaca = hashlib.sha256
    elif typ_hasha == 'sha3-512':
        funkcjaHashujaca = hashlib.sha3_512
    else:
        print("zły hash")
        return
   
    with open(wordlist, "r") as read:
        dane_z_pliku = read.readlines()
        for line in dane_z_pliku:
            pass
                
            
                   

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("ok")
    else:
        zahaszowany_text = sys.argv[1]
        typ_hasha = sys.argv[2]
        Wordlist = sys.argv[3]
        breaking_hash(zahaszowany_text, typ_hasha, Wordlist)

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
# zahaszowany_text = input("podaj text do odhashowania")
# wordlist = []

import hashlib
import sys

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
            linia_textu = line.strip()
            zahaszowana_linia_textu = funkcjaHashujaca(linia_textu.encode()).hexdigest()
            
            if zahaszowany_text == zahaszowana_linia_textu:
                print(f"znaleziono dany hash ({linia_textu}) w pliku")
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("za malo danych")
    else:
        zahaszowany_text = sys.argv[1]
        typ_hasha = sys.argv[2]
        Wordlist = sys.argv[3]
        breaking_hash(zahaszowany_text, typ_hasha, Wordlist)

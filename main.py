import hashlib
import sys

if len(sys.argv) == 4:
    format = sys.argv[1]
    worldlista_sciezka = sys.argv[2]
    text_do_odhashowania = sys.argv[3]
    typhasha = sys.argv[4]

def lamanie_hasla(format,text_do_odhashowania,worldlista_sciezka,typhasha):
    
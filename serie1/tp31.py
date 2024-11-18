from serie1.CompteCourant import CompteCourant
from serie1.CompteEpargne import CompteEpargne
if __name__ == '__main__':
    cc = CompteCourant("Ali", 10000, 10000)
    print(cc)
    ce = CompteEpargne("Ali", 10000, 10)
    print(ce)
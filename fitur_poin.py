poin = 0

def getPoint(poin_baru):
    print (f"Anda mendapat {poin_baru} poin!")
    global poin_awal
    poin_awal = poin_awal + poin_baru

def tukar_poin (poin_tukar):
    if poin_awal >= poin_tukar:
        print(f"Anda menukar {poin_tukar} poin")
        poin_awal = poin_awal-poin_tukar
    else:
        print(f"Poin Anda sekarang: {poin_awal}")
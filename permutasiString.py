# Fausta Akbar W - 1301220081
def cari_permutasi(sisa, saat_ini, permutasi):
    if len(sisa) == 0:
        permutasi.append(saat_ini)
    else:
        for i in range(len(sisa)):
            sisa_baru = sisa[:i] + sisa[i+1:]
            saat_ini_baru = saat_ini + sisa[i]
            cari_permutasi(sisa_baru, saat_ini_baru, permutasi)

masukan_string = input()
hasil_permutasi = []
//msfadsofjaojaf
//comentar
cari_permutasi(masukan_string, "", hasil_permutasi)
print("hello world")
print(hasil_permutasi)

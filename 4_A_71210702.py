ib = 25000
ed = 6000
rc = 8000

print("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")

ikan = int(input("IKAN BAKAR     Rp 25.000,00   : "))
doger = int(input("ES DOGER       Rp 6.000,00    : "))
rujak = int(input("RUJAK CINGUR   Rp 8.000,00    : "))

print("=====TOTAL=====")

ib1 = int(ib)*ikan
ed1 = int(ed)*doger
rc1 = int(rc)*rujak

print("TOTAL IKAN BAKAR     : Rp ", ib1)
print("TOTAL ES DOGER       : Rp ", ed1)
print("TOTAL RUJAK CINGUR   : Rp ", rc1)

print("Jumlah total biaya yang harus dibayar adalah Rp", ib1+ed1+rc1)

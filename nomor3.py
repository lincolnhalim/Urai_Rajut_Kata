class urairajut():
    def urai(self, y):
        hasil = ''
        for i in range (len(y)):
            for j in range (i + 1):
                hasil += y[j]
                hasil += ""
        hasil += ""
        return hasil
    def rajut(self, y):
        kode = [1]
        awal = 1
        for i in range (2, len(y)):
            awal += i
            kode.append(awal)
        total = kode.index (len(y)) + 1
        total *= -1
        hasil2 = y [total: len(y)]
        return hasil2

A = urairajut()

# print(A.urai('Code'))
# print(A.rajut('CCoCodCode'))

try: 

    kata_urai = str(input("masukkan kata yang ingin diurai: "))
    print(str(A.urai(kata_urai)))
    kata_rajut = str(input("masukkan kata yang ingin dirajut: "))
    print(str(A.rajut(kata_rajut)))

except:
    print("input yang anda masukkan salah")





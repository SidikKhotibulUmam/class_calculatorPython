class Kalkulator:
    """kalkulator tambah kurang kali bagi"""
    def __init__(self, pertama, kedua):
        self.pertama = pertama
        self.kedua = kedua        
    def tambah(self): 
        return self.pertama + self.kedua
    def kurang(self):
        return self.pertama - self.kedua
    def kali(self):
        return self.pertama * self.kedua
    def bagi(self):
        return self.pertama / self.kedua

#membuat variabel untuk menyimpan nilai inputan
angka1 = int(input('Masukkan angka pertama : '))
angka2 = int(input('Masukkan angka kedua : '))
#variabel untuk  menyimpan hasil operasi
operator = input('Pilih operator  (+, -, x, :) : ')

#membuat objek dari class Kalkulator
hasilnya = Kalkulator(angka1, angka2)

#menggunakan method dari class Kalkulator
if operator  == '+':
    print (f'{angka1} + {angka2} = {hasilnya.tambah()}')
elif operator == '-':
    print (f'{angka1} - {angka2} = {hasilnya.kurang()}')
elif operator == 'x':
    print (f'{angka1} x {angka2} = {hasilnya.kali()}')
elif operator == ':':
    print (f'{angka1} : {angka2} = {hasilnya.bagi()}')
else:
    print ("Lah kocak ni bocah")


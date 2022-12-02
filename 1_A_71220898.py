print("======= Program Manipulasi String =======")
print("Pilihan Menu :")
print("1. Hitung Kata")
print("2. Ubah Kata")
a = input("Pilihan Anda :")
b = input("Masukkan sebuah kalimat/kata :")

def hitung_kata():
    c=input("Masukkan kata yang ingin dihitung :")
    d=kata.count(c)
    print("Terdapat banyak",d,"kata",c,"di dalam kalimat")

def ubah_kata():
    e=input("Masukkan yang ingin di ubah :")
    f=input ("Masukkan kata pengganti :")
    g=kata.replace(e,f)
    print("String berhasil di ubah menjadi :",g)

if a==("1"):
    hitung_kata()
elif a==("2"):
    ubah_kata()
else:
    print("pilihan yang anda input tidak terdaftar di daftar pilihan")
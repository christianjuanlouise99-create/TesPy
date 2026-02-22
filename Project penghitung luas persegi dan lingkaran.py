# penghitung jumlah luas bangunan

# Persegi

print("masukan panjang sisi persegi yang kamu inginkan")
sisi_persegi = int(input("Segi persegi : "))

luas_persegi = sisi_persegi * sisi_persegi

# Lingkaran

print("masukanlah jari-jari lingkaran yang kamu inginkan")
jari_jari_lingkaran = int(input("Jari-Jari lingkaran : "))

pi = 3.14
luas_lingkaran = pi * jari_jari_lingkaran * jari_jari_lingkaran

# Persegi Panjang

print("masukan panjang sisi persegi panjang dan lebar persegi panjang yang kamu inginkan")
panjang_persegi_panjang = int(input("panjang persegi panjang : "))
lebar_persegi_panjang = int(input("lebar persegi panjang : "))

luas_persegi_panjang = panjang_persegi_panjang * lebar_persegi_panjang

print("Jadi Luas persegi dengan sisi", sisi_persegi, "adalah:", luas_persegi)
print("Jadi luas lingkaran dengan jari jari",jari_jari_lingkaran, "adalah:", round(luas_lingkaran))
print("dan, luas persegi panjang dari sisi panjang", panjang_persegi_panjang,
       "dan lebar", lebar_persegi_panjang, "adalah:", luas_persegi_panjang,)
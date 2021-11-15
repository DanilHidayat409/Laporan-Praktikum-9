# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:49:03 2021
@judul : Menghitung nilai rata-rata
@hari/tanggal : Senin,20211115
@nim : 065002100032
@author : Muhammad Danil Hidayat 
"""

def rekursif(angka = 0, jumlah = 0 , i = 1):
    
    if jumlah <= 0 :
        return 0 
    
    else:
        angka = int(input("masukan bilangan ke " + str (i) + ":"))
        if jumlah == 1 :
            return angka
        
        else:
            i += 1
            return angka + rekursif(angka,jumlah - 1 ,i)
        
hasil = int(input("masukan jumlah nya : "))
nilai = rekursif (jumlah = hasil)
print("hasil dari penjumlahan adalah : " + str(nilai))


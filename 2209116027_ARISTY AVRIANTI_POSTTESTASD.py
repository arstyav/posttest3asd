import os #digunakan untuk menghapur=t output sebelumnya, agar tampilan terlihat rapih
from random import randint #digunakan untuk mengimport angka- anka random yang akan di sorting nanti
os.system('cls')

#yang pertama ada fungsi sorting dengan jenis merge sort
def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2 #menyatakan nilai tengah dimana dibagi 2 untuk menentukannya, apabila nilai nya angka desimal maka akan dibulatkan keba wah
        left_data = data[:mid] #menyatakan nilai kiri, dimana indeks yang diambil yaitu dari tengah  ke kiri
        right_data = data[mid:]  #menyatakan nilai kanan, dimana indeks yang diambil yaitu dari tengah  ke kanan


        mergesort(left_data) #memanggil fungsi mergesort untuk data kiri
        mergesort(right_data) #memanggil fungsi mergesort untuk data kanan
        
         
        i = j = k=0 #menyatakan bahwa indeks untuk array kiri, kanan, dan indeks untuk penggabungannya bernilai 0
        

        while i < len(left_data) and j < len (right_data):
            if left_data[i] < right_data[j]:
                data[k]= left_data[i]
                i += 1
                k += 1

            else:
                data[k] = right_data[j]
                j += 1
                k += 1

        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1

        
        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

print(65*"=")
 
data = [(randint(27,100))] #ini digunakan untuk memberi range/jangkauan angka yang akan dirandom

for i in range(10): #untuk menentukan berapa banyak angka yang akan berada dalam list
    data.append(randint(27,100)) #untuk menambahkan jangkauan angka yang diinginkan

print('data sebelum di sorting:' , data) #untuk menampilkan data sebelum di sorting
mergesort(data) #untuk memanggil fungsi mergesort di atas, agar dapat mengsorting angka yang berada dalam list
print (f"Merge Sort :  {data} ") #untuk menampilkan hasil sorting menggunakan merge sort

#Fungsi partition mengambil elemen pertama pada list sebagai pivot, menempatkannya elemen yang lebih kecil di sebelah kiri pivot, yang lebih besar di kanan pivot, 
#sekaligus me-return posisi pertama setelah pivot
def partition(l, bwh, atas):
  pivot = l[bwh]
  pos_batas = bwh+1
  for j in range(bwh+1,atas):
    if l[j] < pivot:
      l[pos_batas],l[j]=l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
  return pos_batas

def quicksort(l, bwh, atas):
  if atas <= bwh:
    return
  q = partition(l, bwh, atas)
  quicksort(l, bwh, q-1)
  quicksort(l, q, atas)
  return l

print(65*"=")
arr = [] #list kosong yang nanti akan diisi dengan angka-angka random

data = [(randint(25,100)) ]

for i in range(10): #untuk menentukan berapa banyal angka yang akan berada dalam list
    arr.append(randint(25,100)) #untuk menambahkan jangkauan angka yang diinginkan

print('dta sebelum di sorting: ',arr) #untuk menampilkan data sebelum disorting
quicksort(arr,0,len(arr))
print('Quick Sort: ',arr) #untuk menampilkan hasil sorting menggunakan quick sort

def shell(list):
    n = len (list)
    gap = n // 2 #banyak elemen nanti akan dibagi dua yang akan menjadi gap atau rentang dalam mengsorting

    while gap > 0:
        for i in range (gap, n):
            temp = list[i]
            j=i
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap

            list [j] = temp
        gap //= 2

    return list

print(65*"=")

angka = [] #list kosong yang nanti akan diisi dengan angka-angka random

data = [(randint(30,100)) ]

for i in range(10): #untuk menentukan berapa banyak angka yang akan berada dalam list
    angka.append(randint(30,100)) #untuk menambahkan jangkauan angka yang diinginkan

print("data sebelum di sorting: ", angka) #untuk menampilkan data sebelum di sorting
print ("Shell Sort : ", shell(angka)) #untuk menampilkan hasil sorting menggunakan shell sort
print(65*"=")
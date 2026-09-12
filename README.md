# MINI_PROJECT_1_Fiona Deandra Liani

Nama:Fiona Deandra Liani

NIM:2609116053

# Flowchart
<img width="551" height="436" alt="Screenshot 2026-09-12 191050" src="https://github.com/user-attachments/assets/7ab3f972-c109-4003-8970-ce680ea205c2" />


# Program
1. Input variabel yang berisi data dari tanaman. (nama tanaman, jenis indoor/outdoor, status sudah/belum disiram).
<img width="753" height="197" alt="Screenshot 2026-09-12 103443" src="https://github.com/user-attachments/assets/549ea0c0-d629-4365-9357-045dc5c5bf9b" />

2. Ketik while true untuk melakukan perulangan pada program.
   
3. Lalu print kata selamat datang dan beberapa list dari program seperti (lihat daftar tanaman,tambah data tanaman, hapus data tanaman, update status tanaman, dan pemberhentian dari perulangan jika sudah selesai).
   
4. Tambahkan variabel "pilihan" yang isinya adalah input untuk mengambil pilihan angka dari user.

<img width="756" height="142" alt="Screenshot 2026-09-12 103528" src="https://github.com/user-attachments/assets/66480c03-6a8f-430e-9be1-943b005a2e3f" />

5. Tambahkan if pilihan==1, atau jika user mengetik 1 makan akan menampilkan list dari daftar tanaman.
   
6. Lalu print "daftar tanaman" sebagai judulnya, lalu memakai no =1 untuk menampilkan variabel dalam urutan angka, contohnya:
   
   (1) Lihat daftar tanaman
   
   (2) tambah data tanaman baru
   
   (3) .....
   
7. setelah itu memakai "for tanaman in daftar_tanaman" untuk mengambil data dari daftar tanaman secara bergantian. Pakai print yang berisi f-string untuk menampilkan 3 data yang berbeda. Lalu gunakan "no = no + 1" untuk menambah nomor urut di perulangan selanjutnya.

<img width="753" height="108" alt="Screenshot 2026-09-12 113720" src="https://github.com/user-attachments/assets/c11e17fc-5e5c-4721-b23a-970f45d79cfc" />

8. Untuk elif pilihan == 2 atau saat user mengetik 2, tambahkan variabel yang berisi input dari nama, jenis, dan status tanaman untuk menambah data tanaman yang baru.
   
9. Lalu tambah variabel “tanaman_baru” yang berisi format dari tanaman yang akan diinput. Tambahkan "daftar_tanaman.append(tanaman_baru)" untuk memasukkan list tanaman baru kebagian paling akhir dari list daftar tanaman. Setelah itu print menggunakan f-string untuk menggabungkan format dari isi variabel “tanaman_baru” tadi.

<img width="756" height="174" alt="Screenshot 2026-09-12 113730" src="https://github.com/user-attachments/assets/1b7684ae-0cff-4dcd-96d2-f69296b59363" />

10. Untuk elif pilihan == 3 atau saat user mengetik tiga, tambahkan variabel bernama "nomor" yang berisi inputan int untuk memasukkan nomor dari daftar_tanaman yang ingin dihapus. Lalu untuk penggunaan variabel "index_hapus" untuk mengubah nomor pilihan pada penomoran biasa menjadi index di python (dimulai dari angka 0).
    
11.  Variabel yang berisi "daftar_tanaman.pop(index_hapus)" berguna untuk menghapus satu list data tanaman sekaligus pada posisi index tersebut. 

<img width="754" height="209" alt="Screenshot 2026-09-12 113741" src="https://github.com/user-attachments/assets/29125087-19f2-4d27-beba-d29023e3d3a4" />

12. Untuk elif pilihan == 4 atau saat user mengetik empat, berisi variabel int untuk menginput nomor dari list tanaman yang ingin diubah status siramnnya. Lalu untuk penggunaan variabel "index_update" untuk mengubah nomor pilihan pada penomoran biasa menjadi index di python (dimulai dari angka 0).
    
13. daftar_tanaman[indeks_update][2], kurung pertama [indeks_update] adalah untuk memilih tanaman ke berapa, lalu untuk kurung kedua [2] adalah untuk memilih status penyiramannya karena status penyiraman berada di indeks nomor 2.

14. Lalu if-else untuk mengecek statusnya, jika saat ini "belum disiram" maka akan berubah menjadi "sudah disiram", dan juga sebaliknya.
  
<img width="754" height="280" alt="Screenshot 2026-09-12 113755" src="https://github.com/user-attachments/assets/261b5f50-cf6c-47a0-b7d1-bed6481b5fb5" />

15. Tambahkan if pilihan == 5, lalu print "Program selesai" untuk mengakhiri perulangan pada sistem.
<img width="749" height="59" alt="Screenshot 2026-09-12 114108" src="https://github.com/user-attachments/assets/c0b53fee-64c2-4423-98f3-1900914d4806" />

16. Jika user mengetik angka selain dari 1-5, maka hasilnya program akan mengalami pengulangan
<img width="914" height="62" alt="Screenshot 2026-09-12 191429" src="https://github.com/user-attachments/assets/c58a8814-d589-424c-bd1a-7253032e7702" />






# Output
1. Daftar Tanaman
<img width="755" height="204" alt="Screenshot 2026-09-12 101340" src="https://github.com/user-attachments/assets/c64e2d10-82e7-44b3-8a29-0898e7c181ee" />

2. Tambah Daftar Tanaman
<img width="772" height="157" alt="Screenshot 2026-09-12 101406" src="https://github.com/user-attachments/assets/7006f3da-e5d0-4269-ba02-cefe04a5fc9a" />

3. Hapus Tanaman
<img width="753" height="249" alt="Screenshot 2026-09-12 101421" src="https://github.com/user-attachments/assets/ed9e8770-4457-4173-820c-2bd8f4976008" />

4. Uptade Status Tanaman
<img width="756" height="235" alt="Screenshot 2026-09-12 101440" src="https://github.com/user-attachments/assets/c1b828f3-2e61-40ab-9a00-e00d243a2449" />

5. Perulangan berhenti
<img width="755" height="136" alt="Screenshot 2026-09-12 101449" src="https://github.com/user-attachments/assets/c20d5d69-82fd-4a7f-8f39-8537fbe2f107" />

6. jika mengetik selain 1-5
<img width="959" height="237" alt="Screenshot 2026-09-12 191451" src="https://github.com/user-attachments/assets/b7a9925d-9cac-4201-9893-06205438869b" />





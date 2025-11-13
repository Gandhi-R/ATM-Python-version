#  Mini ATM Python

Proyek ini merupakan simulasi **mesin ATM sederhana** yang dibuat menggunakan bahasa pemrograman **Python**.  
Program ini dirancang dengan konsep **modularisasi**, di mana setiap fungsi utama seperti autentikasi, transaksi, dan utilitas dipisahkan ke dalam file dan folder berbeda agar kode lebih terstruktur dan mudah dikembangkan.

---

##  Fitur Utama

###  Autentikasi
- Cek nomor rekening pengguna
- Validasi PIN sebelum masuk ke menu utama

###  Transaksi
- **Cek saldo:** Menampilkan saldo terakhir dari rekening pengguna  
- **Tarik tunai:** Mengurangi saldo dan otomatis mencetak struk ke file `.txt`  
- **Transfer saldo:** Mengirim saldo ke rekening lain dalam sistem

###  Fitur Tambahan
- Pilihan bahasa (Indonesia / English)  
- Fungsi “lanjutkan transaksi” setelah tiap operasi  
- Tampilan terminal berwarna dan bersih  
- Struktur kode modular menggunakan folder `auth`, `transaksi`, dan `utils`

---

##  Struktur Folder
ATM/
│
├── Readme.md
├── main.py # Program utama, berisi alur logika ATM
├── data.py # Data rekening sementara (non-database)
├── cetak_struk.py # Fungsi untuk mencetak struk transaksi
│
├── auth.py #Fungi login dan cek PIN
│
│
├── transaksi/
│ ├── init.py
│ ├── tarik.py # Fungsi tarik saldo + cetak struk
│ ├── transfer.py # Fungsi transfer saldo antar rekening
│
└── utils/
├── init.py
├── helper.py # Fungsi umum ( tanya_lanjutkan())


## Modul yang Digunakan

Program ini hanya menggunakan modul standar bawaan Python, yaitu:

os – membersihkan terminal dan mengatur tampilan

datetime – mencetak tanggal/waktu pada struk

msvcrt – input PIN tanpa terlihat (khusus Windows)

io dan open() – untuk membaca/menulis file .txt


## Tentang Proyek

- Proyek ini dibuat sebagai latihan untuk memahami
- Dasar pemrograman Python
- Penerapan konsep modularisasi
- Penggunaan file eksternal sebagai penyimpanan sederhana
- Pembuatan sistem autentikasi dan transaksi dasar


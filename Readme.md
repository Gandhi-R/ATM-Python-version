🏧 Mini ATM Python

Mini ATM Python adalah proyek simulasi mesin ATM sederhana yang dibuat menggunakan bahasa pemrograman Python.
Proyek ini dirancang dengan konsep modularisasi, di mana setiap fitur utama dipisahkan ke dalam file dan folder yang berbeda agar kode lebih rapi, terstruktur, dan mudah dikembangkan di masa depan.

Proyek ini cocok sebagai latihan dasar Python, terutama untuk memahami alur program, validasi input, dan pengelolaan data sederhana.


✨ Fitur Utama

🔐 **Autentikasi**

Validasi nomor rekening pengguna
Verifikasi PIN sebelum masuk ke menu transaksi
Pembatasan percobaan PIN (maksimal 3 kali)


💳 **Transaksi**

Cek saldo
Menampilkan saldo terakhir dari rekening pengguna

Tarik tunai
Mengurangi saldo dan mencetak struk transaksi ke file .txt

Transfer saldo
Mengirim saldo ke rekening lain yang terdaftar dalam sistem


➕ **Fitur Tambahan**

Pilihan bahasa (Indonesia / English – English coming soon)
Konfirmasi lanjutkan transaksi setelah setiap operasi
Tampilan terminal bersih dan berwarna
Penyimpanan data menggunakan file JSON
Struktur kode modular dan mudah dipahami


📂 **Struktur Folder**
ATM/
│
├── README.md              # Dokumentasi proyek
├── main.py                # Program utama (alur ATM)
├── data.py                # Load & save data rekening (JSON)
├── data.json              # Penyimpanan data rekening
├── cetak_struk.py         # Fungsi cetak struk transaksi
├── auth.py                # Autentikasi: cek rekening & PIN
│
├── transaksi/
│   ├── __init__.py
│   ├── tarik.py           # Tarik tunai + cetak struk
│   └── transfer.py        # Transfer saldo antar rekening
│
└── utils/
    ├── __init__.py
    └── helper.py          # Fungsi umum (tanya_lanjutkan)



🛠 **Modul yang Digunakan**

Program ini hanya menggunakan modul standar bawaan Python, yaitu:
os → Membersihkan terminal & pengaturan tampilan
datetime → Mencetak tanggal dan waktu pada struk
msvcrt → Input PIN tersembunyi (khusus Windows)
json → Penyimpanan data rekening
open() → Membaca dan menulis file .txt
⚠️ Program ini berjalan optimal di Windows karena penggunaan msvcrt.



📌 **Tentang Proyek**

Proyek Mini ATM Python ini dibuat sebagai latihan dan pembelajaran, dengan tujuan memahami:
Dasar-dasar pemrograman Python
Pemisahan kode menggunakan fungsi dan modul
Validasi input dan alur logika program
Penggunaan file eksternal (JSON & TXT)
Simulasi sistem autentikasi dan transaksi sederhana

🚀 **Rencana Pengembangan**

Riwayat transaksi (transaction history)
Versi bahasa Inggris penuh
Penyimpanan data berbasis database
Mode admin untuk manajemen rekening
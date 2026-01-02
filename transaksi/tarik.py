from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_hitung_saldo


def hitung_tarik_saldo(pemilik,nominal):
    if pemilik['saldo']<nominal:

        print("\n \tMAAF, SALDO ANDA KURANG. \n ") 

    else:
        clear()
        pemilik['saldo'] -= nominal

        tambah_history(
            pemilik,
            "Tarik Tunai",
            nominal,
            f"Sisa saldo : Rp.{pemilik['saldo']}")

        print(f"\n   ANDA TELAH MENARIK UANG TUNAI SEBESAR Rp.{nominal}\n         SISA SALDO ANDA SEBESAR Rp.{pemilik['saldo']}\n\n")
        pilih=input("   APA ANDA INGIN MENCETAK STRUK TRANSAKSI ANDA ? (Y/N) : ").upper()
        if pilih=="Y":
            cetak_hitung_saldo(pemilik,nominal)
            print("\n   STRUK ANDA SEDANG DICETAK. SILAHKAN AMBIL STRUK ANDA DI NOTEPAD \n")
        enter()



def tarik_saldo(pemilik):
    print("\n\n            \tPILIH NOMINAL PENARIKAN TUNAI      \n\n\n")
    print("\t1. Rp.100.000                          4. Rp.500.000\n")
    print("\t2. Rp.200.000                          5. Rp.1.000.000\n")
    print("\t3. Rp.300.000                          6. NOMINAL LAIN\n\n\n")
    print("\t\t\tINPUT ANGKA 0\n  \t\tUNTUK MEMBANTALKAN TRANSAKSI \n\n")
    pilih=(int(input("\tMASUKKAN PENARIKAN PILIHAN PENARIKAN NOMINAL : ")))

    match pilih:
        case 1: 
            hitung_tarik_saldo(pemilik,100000)
        case 2: 
            hitung_tarik_saldo(pemilik,200000)
        case 3: 
            hitung_tarik_saldo(pemilik,300000)
        case 4: 
            hitung_tarik_saldo(pemilik,500000)
        case 5: 
            hitung_tarik_saldo(pemilik,1000000)
        case 6: 
            print("\n\n           \tNOMINAL PENARIKAN UANG TUNAI\n  \tHARUS KELIPATAN Rp.50.000 DAN MAKSIMAL Rp.2.500.000  \n")
            try:
                nominal = int(input("\t\t\t  Rp."))
            except ValueError:
                print("\t     Input tidak valid.")
                enter() 
                return

            if 50000 <= nominal <= 2500000 or nominal % 50000 == 0:
                hitung_tarik_saldo(pemilik, nominal)
            else:
                print("\t     MAAF TRANSAKSI TIDAK DAPAT DIPROSES. \n")
                enter()

        case 0:
            print("\tANDA KELUAR PROGRAM")
            enter()

        case _:
            clear()
            print("\n\tMASUKKAN ANDA TIDAK VALID!!")
            enter()


from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_transfer_saldo
   

def transfer_saldo(pemilik,data_rekening):
    
    while True:
        enter()
        clear()
        print("\n\n          TRANSFER SALDO KE REKENING LAIN\n  \t\tYANG INGIN ANDA TRANSFER\n\n")
        print("\t\t INPUT ANGKA 0 \n \t  UNTUK MEMBATALAKAN TRANSAKSI \n\n")

        norek_tujuan=input("\t MASUKKAN NOMOR REKENING TUJUAN :  ")

        if not norek_tujuan.isdigit():
            print("\t NOMOR REKENING TUJUAN HANYA BOLEH BERISI ANGKA. \n")
            enter()
            continue
        
        if norek_tujuan==pemilik['nomorRekening']:
            print("\n \t MAAF, REKENING TUJUAN TIDAK BOLEH SAMA DENGAN REKENING ANDA. \n")
            enter()
            continue

        if norek_tujuan=="0":
            print("\tANDA KELUAR PROGRAM")
            break
        

        tujuan_akun=None
        for i in data_rekening:
            if i['nomorRekening']==norek_tujuan:
                tujuan_akun=i
                break

        if tujuan_akun is None:
            print("\n\t  MAAF, NOMOR REKENING TUJUAN TIDAK DITEMUKAN.\n\t SILAHKAN ULANGI LAGI.\n")
            enter()
            continue

        clear()
        print(f"\n\n    REKNING YANG TERDAFTAR \n\n")
        print(f"    NAMA PEMILIK REKENING   : {tujuan_akun['namaPemilik']}\n\n")
        print(f"    NOMOR REKENING          : {tujuan_akun['nomorRekening']}\n\n")

        while True:
            print("\n\n   \t\tNOMINAL PENTRANSFERAN UANG TUNAI\n \t\t HARUS KELIPATAN Rp.50.000 \n\t\t DAN MAKSIMAL Rp.2.500.000  \n")
            try:
                nominal=int(input("     MASUKKAN NOMINAL YANG INGIN ANDA TRANSFER : Rp."))

            except ValueError:
                print("  INPUT TIDAK VALID. SILAHKAN ULANGI LAGI \n")
                enter()
                continue
                
    
            if 50000 <=nominal<=2500000 and nominal%50000==0:
                if pemilik['saldo']<nominal:
                    print("\n \tMAAF, SALDO ANDA KURANG \n")

                else:
                    tujuan_akun['saldo']+=nominal
                    pemilik['saldo']-=nominal

                    # History pengirim
                    tambah_history(
                        pemilik,
                        "Transfer Keluar",
                        nominal,
                        f"Ke rekening {tujuan_akun['nomorRekening']}"
                        )

                    # Histroy penerima
                    tambah_history(
                        tujuan_akun,
                        "Transfer Masuk",
                        nominal,
                        f"Dari {pemilik['namaPemilik']} ({pemilik['nomorRekening']})"
                        )



                    print(f"\n    ANDA TELAH TRANSFER SEBESAR Rp.{nominal} KE REKENING {tujuan_akun['namaPemilik']}  \n")                           
                    print(f"    SISA SALDO ANDA SAAT INI Rp.{pemilik['saldo']}   \n\n")

                    pilih=input("     APA ANDA INGIN MENCETAK STRUK TRANSAKSI ANDA ? (Y/N) : ").upper()
                    if pilih=="Y":
                        cetak_transfer_saldo(pemilik,nominal,tujuan_akun)
                        print("\n   STRUK ANDA SEDANG DICETAK. SILAHKAN AMBIL STRUK ANDA DI NOTEPAD \n")

                        enter()
                        clear()
                    clear()
                break

            else:
                print("\t     MAAF TRANSAKSI TIDAK DAPAT DIPROSES. \n")
                enter()
                break
        break
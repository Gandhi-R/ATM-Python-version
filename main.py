#ATM SEDERHANA

from auth import cek_rekening, cek_pin, ganti_pin
from data import load_data, save_data
from transaksi.tarik import tarik_saldo
from transaksi.transfer import transfer_saldo
from utils.helper import tanya_lanjutkan
from utils.console import clear, enter, warna
from utils.history import tampil_history
from utils.language import TEXT


def menu_transaksi(pemilik,data_rekening,bahasa):
    while True:
        clear()
        
        print("=============================================")
        print(f"\t\t{TEXT[bahasa]['menu_title']} ")
        print("============================================")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_1']} \n")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_2']} \n")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_3']} \n")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_4']} \n")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_5']} \n")
        print(f"\t\t\t\t{TEXT[bahasa]['menu_6']} \n")
 
        try:
            pilih_transaksi=int(input("\t\tMASUKKAN PILIHAN : "))
        except ValueError:
            print("\tINPUT TIDAK VALID. MASUKKAN ANGKA 1-5 \n")
            enter()
            continue


        match pilih_transaksi:
            case 1:
                clear()
                print(f"\n\n\t\t{TEXT[bahasa]['info_saldo']}  : Rp.{pemilik['saldo']}\n")
                print(f"\n\t {TEXT[bahasa]['press_enter']}")
                enter()
                

            case 2:
                berhasil=tarik_saldo(pemilik)
                if berhasil:
                    save_data(data_rekening)
                
                
            case 3: 
                berhasil=transfer_saldo(pemilik,data_rekening)
                if berhasil:
                    save_data(data_rekening)
                        
            case 4: 
                berhasil=ganti_pin(pemilik)
                if berhasil:
                    save_data(data_rekening)
                        
            
            case 5:
                clear()
                tampil_history(pemilik)
                enter()

            case 6:
                print("\n\n\n\t\t ANDA TELAH KELUAR PROGRAM \n TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n\n")
                break

            case _:
                        
                print("\nPILIHAN TIDAK VALID")
                enter()
        
        if not tanya_lanjutkan():
            clear()
            print("\n\t\t  ANDA TELAH KELUAR PROGRAM \n\t TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n")
            break




def main():
    warna()
    clear()

    data_rekening=load_data()
    pemilik=cek_rekening(data_rekening)
    clear()
    
    if not cek_pin(pemilik):
        return
    
    
    while True:
        clear()

        print("==============================================")
        print("               PILIH BAHASA                   ")
        print("==============================================")
        print("          LANGUAGE PREFERENCES\n\n")
        print("                                  1. INDONESIA\n")
        print("                                  2. INGGRIS\n\n")

        try:
            pilih_bahasa=int(input("         MASUKKAN PILIHAN ANDA : "))
    
        except ValueError:
            print("\t INPUT TIDAK VALID. MASUKKAN ANGKA 1 ATAU 2\n")
            continue
            

        if pilih_bahasa==1:
            bahasa="id"
            menu_transaksi(pemilik,data_rekening,bahasa)
            break
    
        elif pilih_bahasa==2:
            clear()
            bahasa="en"
            menu_transaksi(pemilik,data_rekening,bahasa)
            break
    
        else:
            print("PILIHAN TIDAK VALID")
                

if __name__=="__main__":
    main()







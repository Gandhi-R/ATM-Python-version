#ATM SEDERHANA

from auth import cek_rekening, cek_pin
from data import load_data, save_data
from transaksi.tarik import tarik_saldo
from transaksi.transfer import transfer_saldo
from utils.helper import tanya_lanjutkan
import os 

def clear():
    os.system("cls")


def menu_transaksi(pemilik,data_rekening):
    while True:
        clear()
        
        print("=============================================")
        print("\t\tPILIH TRANSAKSI      ")
        print("============================================")
        print("\t\t\t\t1. INFO SALDO \n")
        print("\t\t\t\t2. TARIK TUNAI\n ")
        print("\t\t\t\t3. TRANSFER \n")
        print("\t\t\t\t4. KELUAR\n")

                
        try:
            pilih_transkasi=int(input("\t\tMASUKKAN PILIHAN : "))
        except ValueError:
            print("\tINPUT TIDAK VALID. MASUKKAN ANGKA 1-4 \n")
            os.system("pause")
            continue


        match pilih_transkasi:
            case 1:
                print(f"\n\n\t\tSALDO ANDA SAAT INI  : Rp.{pemilik['saldo']}\n")
                os.system("pause")
                

            case 2:
                tarik_saldo(pemilik)
                save_data(data_rekening)
                
                
                
            case 3: 
                transfer_saldo(pemilik)
                save_data(data_rekening)
                        
            
            case 4:
                print("\n\n\n ANDA TELAH KELUAR PROGRAM \n TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n\n")
                break

            case _:
                        
                print("\nPILIHAN TIDAK VALID")
                os.system("pause")
        
        if not tanya_lanjutkan():
            print("\n\t  ANDA TELAH KELUAR PROGRAM \n\t TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n")
            break




def main():
    os.system("color 1F")
    clear()

    data_rekening=load_data()
    pemilik=cek_rekening(data_rekening)
    
    if not cek_pin(pemilik):
        return
    
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
        return
        

    if pilih_bahasa==1:
        menu_transaksi(pemilik,data_rekening)
    
    elif pilih_bahasa==2:
        os.system("cls")
        print("\n\n\t\tENGLISH VERSION COMING SOON")
    
    else:
        print("PILIHAN TIDAK VALID")
                

if __name__=="__main__":
    main()







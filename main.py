#ATM SEDERHANA

from auth import cek_rekening, cek_pin
from transaksi.tarik import tarik_saldo
from transaksi.transfer import transfer_saldo
from utils.helper import tanya_lanjutkan
import os 


def menu_transaksi(pemilik):
    while True:
        os.system("cls")
        cek_pin(pemilik)
        
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
                os.system("cls")
                print(f"\n\n\t\tSALDO ANDA SAAT INI  : Rp.{pemilik['saldo']}\n")
                os.system("pause")
                

            case 2:
                os.system("cls")
                tarik_saldo(pemilik)
                
                
                
            case 3:
                os.system("cls")
                transfer_saldo(pemilik)
                        
            
            case 4:
                print("\n\n\n ANDA TELAH KELUAR PROGRAM \n TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n\n")
                break

            case _:
                        
                print("\nPILIHAN TIDAK VALID")
                os.system("pause")
        

        os.system("cls")    
        if not tanya_lanjutkan():
            print("\n\t  ANDA TELAH KELUAR PROGRAM \n\t TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI \n")
            break




def main():
    os.system("color 1F")
    os.system("cls")

    pemilik=cek_rekening()
    os.system("cls")

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
        os.system("pause")
        

    if pilih_bahasa==1:
        menu_transaksi(pemilik)
    
    elif pilih_bahasa==2:
        os.system("cls")
        print("\n\n\t\tENGLISH VERSION COMING SOON")
    
    else:
        print("PILIHAN TIDAK VALID")
                

if __name__=="__main__":
    main()







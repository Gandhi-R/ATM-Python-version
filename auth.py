#otentikasi

from utils.console import clear, enter
from utils.language import TEXT
import msvcrt

def cek_rekening(data_rekening):
    while True:
        print("                    MASUKKAN  NOMOR REKENING ANDA\n ")
        print("------------------------------------------------------------------\n\n")
        print("                      ENTER YOUR NUMBER CODE\n\n")
        input_norek=(input("                                ")).strip()

        if not input_norek.isdigit():
            print("\n\n      MAAF, NOMOR REKENING HANYA BOLEH BERISI ANGKA.  \n")
            enter()
            continue

        for i in data_rekening:
            if i['nomorRekening']==input_norek:
                return i
            
        print("\n\n\n      MAAF NOMOR ANDA TIDAK TERDAFTAR , SILAHKAN ULANGI ")
        print("\n\n--------------------------------------------------------- ")
        print("\n\n       YOUR ACCOUNT NUMBER IS NOT REGISTERED. PLEASE REPEAT \n")
        input("TEKAN ENTER UNTUK MELANJUTKAN")
        clear()


def cek_pin_lemah(pin):
    pin_lemah = [
        "000000", "111111", "222222", "333333",
        "444444", "555555", "666666", "777777",
        "888888", "999999",
        "123456", "654321"
    ]

    if pin in pin_lemah:
        return True

    if pin in "0123456789":
        return True

    if len(set(pin)) == 1:
        return True

    return False


def cek_pin(pemilik):
    total_coba = 0
    pin_benar = pemilik['pin']

    while total_coba < 3:
        clear()
        print("\t\t MASUKKAN PIN ATM ANDA\n\t======================================\n\t\t     ENTER YOUR PIN\n\n\n\n", end="\t\t\t ", flush=True)
        pin_input = ""

        while True:
            ch = msvcrt.getch()
            if ch == b'\r':  # ENTER ditekan
                break
            elif ch == b'\x08':  # BACKSPACE ditekan
                if len(pin_input) > 0:
                    pin_input = pin_input[:-1]
                    print('\b \b', end="", flush=True)
            elif ch.isdigit():  # hanya angka
                pin_input += ch.decode()
                print("*", end="", flush=True)

        if len(pin_input) !=6:
            print("\n\n\n \t\t PIN HARUS 6 DIGIT. SILAHKAN ULANGI LAGI")
            print("======================================================")
            print("\n\n\n \t\t PIN MUST BE 6 DIGITS. PLEASE REPEAT AGAIN")
            enter()
            continue

        
        

        # Cek apakah PIN benar
        if pin_input == pin_benar:

            print(f"\n\n\n\n\n\t\tSELAMAT DATANG, {pemilik['namaPemilik']}.\n")
            enter()
            clear()
            return True
            
        else:
            total_coba += 1
            sisa = 3 - total_coba
            if sisa > 0:
                print(f"\n\n\n\n\t\t\tPIN SALAH.\n \t\tPERCOBAAN ANDA SISA {sisa} KALI LAGI.")
                enter()
            else:
                print("\n\n\n\n\tANDA TELAH SALAH MEMASUKKAN PIN 3 KALI.\n \t\t KARTU ANDA DIBLOKIR.\n")
                enter()
                return False
            


            
def ganti_pin(pemilik,bahasa):
    total_coba=0
    pin_benar=pemilik['pin']
    while total_coba < 3:
        clear()
        print("========================================")
        print(f"                {TEXT[bahasa]['change_pin_title']}")
        print("========================================\n")
        print(f"\t   {TEXT[bahasa]['old_pin_input']}\n\n", end="\t\t ", flush=True)
        pin_input = ""

        while True:
            ch = msvcrt.getch()
            if ch == b'\r':
                break
            elif ch == b'\x08':
                if len(pin_input) > 0:
                    pin_input = pin_input[:-1]
                    print('\b \b', end="", flush=True)
            elif ch.isdigit():
                pin_input += ch.decode()
                print("*", end="", flush=True)

        if len(pin_input) != 6:
            print(f"\n\n{TEXT[bahasa]['pin_length_error']}")
            enter()
            continue
        if pin_input!=pin_benar:
            total_coba+=1
            print(f"\t{TEXT[bahasa]['wrong_pin']} : {3-total_coba}")
            enter()
            continue

        #jika pin lama benar 
        clear()
        print(f"\t\t {TEXT[bahasa]['new_pin_input']}\n\n", end="\t\t ", flush=True)

        pin_baru = ""

        while True:
            ch = msvcrt.getch()
            if ch == b'\r':
                break
            elif ch == b'\x08':
                if len(pin_baru) > 0:
                    pin_baru = pin_baru[:-1]
                    print('\b \b', end="", flush=True)
            elif ch.isdigit():
                pin_baru += ch.decode()
                print("*", end="", flush=True)

            
        if len(pin_baru) != 6:
            print(f"\t{TEXT[bahasa]['pin_length_error']}")
            enter()
            continue

        if pin_baru == pin_benar:
            print(f"\t{TEXT[bahasa]['same_pin_error']}")
            enter()
            continue

        if cek_pin_lemah(pin_baru):
            print(f"\t{TEXT[bahasa]['weak_pin']}")
            enter()
            continue



        #konfirmasi
        clear()
        print(f"\t{TEXT[bahasa]['confirm_pin']}\n\n", end="\t\t ", flush=True)
        konfirmasi=""

        while True:
            ch=msvcrt.getch()
            if ch==b'\r':
                break
            elif ch==b'\x08':
                if len(konfirmasi)>0:
                    konfirmasi=konfirmasi[:-1]
                    print('\b \b', end="", flush=True)
            elif ch.isdigit():
                konfirmasi+=ch.decode()
                print("*",end="",flush=True)

        if konfirmasi!=pin_baru:
            print(f"\t {TEXT[bahasa]['pin_not_match']}")
            enter()
            continue

        #JIKA BERHASIL
        pemilik['pin']=pin_baru
        print(f"\n\t{TEXT[bahasa]['pin-changed']}")
        enter()
        return True  
    
    print(f"\n {TEXT[bahasa]['pin_blocked']}")
    enter()
    return False


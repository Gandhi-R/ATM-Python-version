from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_hitung_saldo
from utils.language import TEXT


def hitung_tarik_saldo(pemilik,nominal,bahasa):
    if pemilik['saldo']<nominal:

        print(f"\n\t\n{TEXT[bahasa]['min_saldo']} ") 

    else:
        clear()
        pemilik['saldo'] -= nominal

        tambah_history(
            pemilik,
            "Tarik Tunai",
            nominal,
            f"Sisa saldo : Rp.{pemilik['saldo']}")

        print(f"\n\t{TEXT[bahasa]['inpo_saldo']} Rp.{nominal}\n         {TEXT[bahasa]['sisa']} Rp.{pemilik['saldo']}\n\n")
        pilih=input(f"   {TEXT[bahasa]['struk']} (Y/N) : ").upper()
        if pilih=="Y":
            cetak_hitung_saldo(pemilik,nominal,bahasa)
            print(f"\n   {TEXT[bahasa]['valid_saldo']} \n")
        enter()



def tarik_saldo(pemilik,bahasa):
    print(f"\n\n            \t{TEXT[bahasa]['menu_tarik']}      \n\n\n")
    print("\t1. Rp.100.000                          4. Rp.500.000\n")
    print("\t2. Rp.200.000                          5. Rp.1.000.000\n")
    print("\t3. Rp.300.000                          6. NOMINAL LAIN\n\n\n")
    print(f"\t\t\t{TEXT[bahasa]['note_tarik']}\n\n")
    pilih=(int(input(TEXT[bahasa]['input_tarik'])))

    match pilih:
        case 1: 
            hitung_tarik_saldo(pemilik,100000,bahasa)
        case 2: 
            hitung_tarik_saldo(pemilik,200000,bahasa)
        case 3: 
            hitung_tarik_saldo(pemilik,300000,bahasa)
        case 4: 
            hitung_tarik_saldo(pemilik,500000,bahasa)
        case 5: 
            hitung_tarik_saldo(pemilik,1000000,bahasa)
        case 6: 
            print(f"\n\n\t\t{TEXT[bahasa]['note_tarik']} \n")
            try:
                nominal = int(input("\t\t\t  Rp."))
            except ValueError:
                print(f"\t\t{TEXT[bahasa]['invalid_input']}.")
                enter() 
                return

            if 50000 <= nominal <= 2500000 or nominal % 50000 == 0:
                hitung_tarik_saldo(pemilik, nominal,bahasa)
            else:
                print(f"\t\t{TEXT[bahasa]['nota_proses']}\n")
                enter()

        case 0:
            print(f"\t{TEXT[bahasa]['left_tarik']}")
            enter()

        case _:
            clear()
            print(F"\n\t{TEXT[bahasa]['invalid_input']}!!")
            enter()

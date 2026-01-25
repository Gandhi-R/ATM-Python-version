from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_tarik_saldo
from utils.language import TEXT


def hitung_tarik_saldo(pemilik,nominal,bahasa):
    if pemilik['saldo']<nominal:

        print(f"\n\t\n{TEXT[bahasa]['balance_not_enough']} ") 

    else:
        pemilik['saldo'] -= nominal

        tambah_history(
            pemilik,
            "Tarik Tunai",
            nominal,
            f"Sisa saldo : Rp.{pemilik['saldo']}")

        print(f"\n\t{TEXT[bahasa]['withdraw_success']} : Rp.{nominal}\n         {TEXT[bahasa]['remaining_balance']} Rp.{pemilik['saldo']}\n\n")
        pilih=input(f"   {TEXT[bahasa]['print_receipt']} (Y/N) : ").upper()
        if pilih=="Y":
            cetak_tarik_saldo(pemilik,nominal,bahasa)
            print(f"\n   {TEXT[bahasa]['receipted_printed']} \n")
        enter()



def tarik_saldo(pemilik,bahasa):
    print(f"\n\n            \t{TEXT[bahasa]['withdraw_menu']}      \n\n\n")
    print("\t1. Rp.100.000                          4. Rp.500.000\n")
    print("\t2. Rp.200.000                          5. Rp.1.000.000\n")
    print("\t3. Rp.300.000                          6. NOMINAL LAIN\n\n\n")
    print(f"\t\t\t{TEXT[bahasa]['withdraw_note']}\n")
    print(f"\t\t\t{TEXT[bahasa]['withdraw_cancel_note']}\n")
    pilih=(int(input(TEXT[bahasa]['withdraw_input'])))

    match pilih:
        case 1: 
            hitung_tarik_saldo(pemilik,100000,bahasa)
            return True
        case 2: 
            hitung_tarik_saldo(pemilik,200000,bahasa)
            return True
        case 3: 
            hitung_tarik_saldo(pemilik,300000,bahasa)
            return True
        case 4: 
            hitung_tarik_saldo(pemilik,500000,bahasa)
            return True
        case 5: 
            hitung_tarik_saldo(pemilik,1000000,bahasa)
            return True
        case 6: 
            print(f"\n\n\t\t{TEXT[bahasa]['withdraw_note']} \n")
            try:
                nominal = int(input("\t\t\t  Rp."))
            except ValueError:
                print(f"\t\t{TEXT[bahasa]['transaction_failed']}.")
                enter() 
                return

            if 50000 <= nominal <= 2500000 and nominal % 50000 == 0:
                hitung_tarik_saldo(pemilik, nominal,bahasa)
                return True
            else:
                print(f"\t\t{TEXT[bahasa]['transaction_failed']}\n")
                enter()

        case 0:
            print(f"\t{TEXT[bahasa]['transaction_left']}")
            return False
            enter()

        case _:
            clear()
            print(F"\n\t{TEXT[bahasa]['invalid_input']}!!")
            enter()

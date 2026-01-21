
from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_transfer_saldo
from utils.language import TEXT
   

def transfer_saldo(pemilik,data_rekening,bahasa):
    
    while True:
        enter()
        clear()
        print(f"\n\n          {TEXT[bahasa]['transfer_title']}\n\n")
        print(f"\t\t {TEXT[bahasa]['transfer_cancel_note']} \n\n")

        norek_tujuan=input(f"\t {TEXT[bahasa]['transfer_input_account']} :  ")

        if not norek_tujuan.isdigit():
            print(f"\t {TEXT[bahasa]['transfer_invalid_account']} \n")
            continue
        
        if norek_tujuan==pemilik['nomorRekening']:
            print(f"\n \t {TEXT[bahasa]['transfer_same_account']} \n")
            enter()
            continue

        if norek_tujuan=="0":
            print(f"\t{TEXT[bahasa]['transaction_left']}")
            break
        

        tujuan_akun=None
        for i in data_rekening:
            if i['nomorRekening']==norek_tujuan:
                tujuan_akun=i
                break

        if tujuan_akun is None:
            print(f"\n\t  {TEXT[bahasa]['transfer_account_not_found']}\n")
            enter()
            continue

        clear()
        print(f"\n\n    {TEXT[bahasa]['transfer_registered_account']} \n\n")
        print(f"    {TEXT[bahasa]['account_owner']}   : {tujuan_akun['namaPemilik']}\n\n")
        print(f"    {TEXT[bahasa]['account_number']}         : {tujuan_akun['nomorRekening']}\n\n")

        while True:
            print(f"\n\n   \t\t{TEXT[bahasa]['transfer_nominal_note']}  \n")
            try:
                nominal=int(input(f"     {TEXT[bahasa]['transfer_input_nominal']}"))

            except ValueError:
                print(f"  {TEXT[bahasa]['input_error']} \n")
                enter()
                continue
                
    
            if 50000 <=nominal<=2500000 and nominal%50000==0:
                if pemilik['saldo']<nominal:
                    print(f"\n \t{TEXT[bahasa]['balance_not_enough']}\n")

                else:
                    tujuan_akun['saldo']+=nominal
                    pemilik['saldo']-=nominal

                    # History pengirim
                    tambah_history(
                        pemilik,
                        "Transfer",
                        nominal,
                        f"Ke Rekening : {tujuan_akun['namaPemilik']}"
                        )

                    # Histroy penerima
                    tambah_history(
                        tujuan_akun,
                        "Transfer Masuk",
                        nominal,
                        f"Dari {pemilik['namaPemilik']} ({pemilik['nomorRekening']})"
                        )



                    print(f"\n    {TEXT[bahasa]['transfer_success']} \n")                           
                    print(f"    {TEXT[bahasa]['transfer_remaining_balance']}{pemilik['saldo']}   \n\n")

                    pilih=input(f"     {TEXT[bahasa]['print_receipt']} (Y/N) : ").upper()
                    if pilih=="Y":
                        cetak_transfer_saldo(pemilik,nominal,tujuan_akun)
                        print(f"\n   {TEXT[bahasa]['receipt_printed']} \n")

                        enter()
                    clear()
                break

            else:
                print(f"\t    {TEXT[bahasa]['transaction_failed']} \n")
                enter()
                break
        break
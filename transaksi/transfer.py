
from utils.console import clear, enter
from utils.history import tambah_history
from cetak_struk import cetak_transfer_saldo
from utils.language import TEXT
   

def transfer_saldo(pemilik,data_rekening,bahasa):
    
    while True:
        enter()
        clear()
        print(f"\n\n          {TEXT[bahasa]['deskrip_transfer']}\n\n")
        print(f"\t\t {TEXT[bahasa]['cancel_transfer']} \n\n")

        norek_tujuan=input(f"\t {TEXT[bahasa]['input_transfer']} :  ")

        if not norek_tujuan.isdigit():
            print(f"\t {TEXT[bahasa]['wrong_destination']} \n")
            enter()
            continue
        
        if norek_tujuan==pemilik['nomorRekening']:
            print(f"\n \t {TEXT[bahasa]['same_number']} \n")
            enter()
            continue

        if norek_tujuan=="0":
            print(f"\t{TEXT[bahasa]['out_destination']}")
            break
        

        tujuan_akun=None
        for i in data_rekening:
            if i['nomorRekening']==norek_tujuan:
                tujuan_akun=i
                break

        if tujuan_akun is None:
            print(f"\n\t  {TEXT[bahasa]['none_number']}\n")
            enter()
            continue

        clear()
        print(f"\n\n    {TEXT[bahasa]['terdaftar']} \n\n")
        print(f"    {TEXT[bahasa]['name']}   : {tujuan_akun['namaPemilik']}\n\n")
        print(f"    {TEXT[bahasa]['number']}         : {tujuan_akun['nomorRekening']}\n\n")

        while True:
            print(f"\n\n   \t\t{TEXT[bahasa]['deskrip_nominal']}  \n")
            try:
                nominal=int(input(f"     {TEXT[bahasa]['input_nominal']}"))

            except ValueError:
                print(f"  {TEXT[bahasa]['repeat_input']} \n")
                enter()
                continue
                
    
            if 50000 <=nominal<=2500000 and nominal%50000==0:
                if pemilik['saldo']<nominal:
                    print(f"\n \t{TEXT[bahasa]['low_saldo']}\n")

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



                    print(f"\n    {TEXT[bahasa]['succes1']}{nominal} {TEXT[bahasa]['succes2']} {tujuan_akun['namaPemilik']}  \n")                           
                    print(f"    {TEXT[bahasa]['remainingr']}{pemilik['saldo']}   \n\n")

                    pilih=input(f"     {TEXT[bahasa]['print_struk']} ").upper()
                    if pilih=="Y":
                        cetak_transfer_saldo(pemilik,nominal,tujuan_akun)
                        print(f"\n   {TEXT[bahasa]['print_succes']} \n")

                        enter()
                        clear()
                    clear()
                break

            else:
                print(f"\t    {TEXT[bahasa]['false_transaction']} \n")
                enter()
                break
        break
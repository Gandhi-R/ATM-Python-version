import os
import datetime
from utils.language import TEXT




def cetak_tarik_saldo(pemilik,nominal,bahasa):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA=====================\n\n")
        file.write(f"{TEXT[bahasa]['receipt_date']}    : {tanggal}                       {TEXT[bahasa]['receipt_time']}: {waktu}\n")
        file.write(f"{TEXT[bahasa]['receipt_owner']}       : {pemilik['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['receipt_account']}        : {pemilik['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['receipt_amount']}             : Rp.{nominal} \n")
        file.write(f"{TEXT[bahasa]['receipt_balance']}         : {pemilik['saldo']}\n\n")
        file.write("======================================================\n")
        file.write(f"                    {TEXT[bahasa]['receipt_note_1']} \n")
        file.write(f"                  {TEXT[bahasa]['receipt_note_2']} ")

        os.system("start /min notepad struk_saldo.txt")
    

 


def cetak_transfer_saldo(pemilik,nominal,tujuan,bahasa):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_transfer_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA====================\n\n")
        file.write(f"{TEXT[bahasa]['receipt_date']}L : {tanggal}                        {TEXT[bahasa]['receipt_time']}: {waktu}\n")
        file.write(f"{TEXT[bahasa]['receipt_owner']}           : {pemilik['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['sender_account']}   : {pemilik['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['receiver_name']}           : {tujuan['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['receiver_account']}    : {tujuan['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['receipt_amount']}                : Rp.{nominal}\n")
        file.write(f"{TEXT[bahasa]['sender_balance']}          : Rp.{pemilik['saldo']}\n")
        file.write(f"{TEXT[bahasa]['receiver_balance']}          : Rp.{tujuan['saldo']}\n")
        file.write("=====================================================\n")
        file.write(f"                 {TEXT[bahasa]['receipt_note_1']} \n")
        file.write(f"            {TEXT[bahasa]['receipt_note_2']} \n\n\n")

        os.system("start /min notepad struk_transfer_saldo.txt")

     

import os
import datetime
from utils.language import TEXT




def cetak_tarik_saldo(pemilik,nominal,bahasa):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA=====================\n\n")
        file.write(f"{TEXT[bahasa]['tanggal']}    : {tanggal}                       {TEXT[bahasa]['waktu']}: {waktu}\n")
        file.write(f"{TEXT[bahasa]['nama']}       : {pemilik['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['no_rekening']}        : {pemilik['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['tarik']}             : Rp.{nominal} \n")
        file.write(f"{TEXT[bahasa]['sisa']}         : {pemilik['saldo']}\n\n")
        file.write("======================================================\n")
        file.write(f"                    {TEXT[bahasa]['deskrip_1']} \n")
        file.write(f"                  {TEXT[bahasa]['deskrip_2']} ")

        os.system("start /min notepad struk_saldo.txt")
    

 


def cetak_transfer_saldo(pemilik,nominal,tujuan,bahasa):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_transfer_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA====================\n\n")
        file.write(f"{TEXT[bahasa]['tanggal']}L : {tanggal}                        {TEXT[bahasa]['waktu']}: {waktu}\n")
        file.write(f"{TEXT[bahasa]['pengirim']}           : {pemilik['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['no_pengirim']}   : {pemilik['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['penerima']}           : {tujuan['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['no_penerima']}    : {tujuan['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['tf']}                : Rp.{nominal}\n")
        file.write(f"{TEXT[bahasa]['saldo_pener']}          : Rp.{pemilik['saldo']}\n")
        file.write(f"{TEXT[bahasa]['saldo_pengi']}          : Rp.{tujuan['saldo']}\n")
        file.write("=====================================================\n")
        file.write(f"                 {TEXT[bahasa]['deskrip_1']} \n")
        file.write(f"            {TEXT[bahasa]['deskrip_2']} \n\n\n")

        os.system("start /min notepad struk_transfer_saldo.txt")

     

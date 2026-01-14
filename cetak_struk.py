import os
import datetime
from utils.language import TEXT




def cetak_tarik_saldo(pemilik,nominal,bahasa):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA=====================\n\n")
        file.write(f"{TEXT[bahasa]['tanggal']}    : {tanggal}                       WAKTU : {waktu}\n")
        file.write(f"{TEXT[bahasa]['nama']}       : {pemilik['namaPemilik']}\n")
        file.write(f"{TEXT[bahasa]['no_rekening']}        : {pemilik['nomorRekening']}\n")
        file.write(f"{TEXT[bahasa]['tarik']}              : Rp.{nominal} \n")
        file.write(f"{TEXT[bahasa]['sisa']}            : {pemilik['saldo']}\n\n")
        file.write("======================================================\n")
        file.write(f"                    {TEXT[bahasa]['deskrip_1']} \n")
        file.write(f"                  {TEXT[bahasa]['deskrip_2']} ")

        os.system("start /min notepad struk_saldo.txt")
    

 


def cetak_transfer_saldo(pemilik,nominal,tujuan,lang):
    sekarang=datetime.datetime.now()
    tanggal=sekarang.strftime("%d-%m-%y")
    waktu=sekarang.strftime("%H:%M:%S")
    with open("struk_transfer_saldo.txt","w") as file:
        file.write("=====================ATM BERSAMA====================\n\n")
        file.write(f"TANGGAL : {tanggal}                        WAKTU : {waktu}\n")
        file.write(f"NAMA PENGIRIM      : {pemilik['namaPemilik']}\n")
        file.write(f"NO REK PENIGIRIM   : {pemilik['nomorRekening']}\n")
        file.write(f"NAMA PENERIMA      : {tujuan['namaPemilik']}\n")
        file.write(f"NO REK PENERIMA    : {tujuan['nomorRekening']}\n")
        file.write(f"TRANSFER           : Rp.{nominal}\n")
        file.write(f"SALDO PENGIRIM     : Rp.{pemilik['saldo']}\n")
        file.write(f"SALDO PENERIMA     : Rp.{tujuan['saldo']}\n")
        file.write("=====================================================\n")
        file.write("                 SIMPAN TANDA TERIMA INI \n")
        file.write("            SEBAGAI BUKTI TRANSAKSI YANG SAH \n\n\n")

        os.system("start /min notepad struk_transfer_saldo.txt")

     

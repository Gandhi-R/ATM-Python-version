
def tanya_lanjutkan():
    while True:
        pilihan = input("\n\t APAKAH INGIN MELAKUKAN TRANSAKSI LAIN? (Y/N): ").strip().upper()
        if pilihan in ["Y", "N"]:
            return pilihan == "Y"  # return True kalau Y, False kalau N
        else:
            print("\n PILIHAN TIDAK VALID. SILAHKAN MASUKKAN Y ATAU N.")

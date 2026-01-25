from utils.language import TEXT

def tanya_lanjutkan(bahasa):
    while True:
        pilihan = input(f"\n\t {TEXT[bahasa]['continue_transaction']} ").strip().upper()
        if pilihan in ["Y", "N"]:
            return pilihan == "Y"  # return True kalau Y, False kalau N
        else:
            print(f"\n {TEXT[bahasa]['invalid_yes_no']}")

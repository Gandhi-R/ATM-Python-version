from datetime import datetime

def tambah_history(pemilik, jenis, nominal, keterangan=""):
    if "history" not in pemilik:
        pemilik["history"]=[]
        

    pemilik["history"].append(
        {
        "tanggal":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "jenis":jenis,
        "nominal":nominal,
        "keterangan":keterangan
        }
    )

    pemilik["history"]=pemilik["history"][-5:]


def tampil_history(pemilik, limit=5):
    history=pemilik.get("history",[])

    if not history:
        print("\n==============BELUM ADA RIWAYAT TRANSAKSI=========\n")
    else:
        print("\n==============RIWAYAT TRANSAKSI===============\n")
        for i,j in enumerate(history[-5:],start=1):
            print(f"{i}. {j['tanggal']}")
            print(f"   {j['jenis']} : Rp.{j['nominal']}")
            print(f"   {j['keterangan']}\n")
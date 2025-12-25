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
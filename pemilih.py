listPemilih = []

def tambah_pemilih():
    idPem = input("Masukan ID Pemilih: ")
    if any(p['ID Pemilih'] == idPem for p in listPemilih):
        print("ID sudah terdaftar.")
        return
    
    namaPem = input("Masukan Nama Pemilih: ")
    jurPem = input("Masukan Jurusan Pemilih: ")
    
    listPemilih.append({
        "ID Pemilih": idPem,
        "Nama Pemilih": namaPem,
        "Jurusan": jurPem,
        "Sudah Memilih": False
    })
    print("Pemilih berhasil didaftarkan")

def get_data():
    return listPemilih

def cari_pemilih(id):
    for p in listPemilih:
        if p['ID Pemilih'] == id:
            return p
    return Nones

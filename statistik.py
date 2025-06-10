def hasil_pemilihan():
    print("\n=== Hasil Pemilihan Sementara ===")
    if not listCalon:
        print("Belum ada data calon.")
    else:
        for c in listCalon:
            print(f"{c['Nama Calon']} ({c['ID Calon']}): {c['Jumlah Suara']} suara")

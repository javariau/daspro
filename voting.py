from .calon import listCalon, lihat_calon, pilih_calon, hasil_pemilihan
from .pemilih import listPemilih, get_data

def statistik_pemilu():
    data = get_data()
    total = len(data)
    sudah_memilih = sum(1 for p in data if p['Sudah Memilih'])
    belum_memilih = total - sudah_memilih

    print("\n=== Statistik Pemilu ===")
    print(f"Total Pemilih     : {total}")
    print(f"Sudah Memilih     : {sudah_memilih}")
    print(f"Belum Memilih     : {belum_memilih}")

def main():
    while True:
        print("\n===== SISTEM E-VOTING =====")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Statistik Pemilu")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_pemilih()
        elif pilihan == '2':
            print("\n1. Tambah Calon\n2. Lihat Calon")
            subpilih = input("Pilih: ")
            if subpilih == '1':
                tambah_calon()
            elif subpilih == '2':
                lihat_calon()
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '3':
            pilih_calon()
        elif pilihan == '4':
            hasil_pemilihan()
        elif pilihan == '5':
            statistik_pemilu()
        elif pilihan == '6':
            print("Keluar dari sistem. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()

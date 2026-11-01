class Produk:
    """
    Representasi Abstract Data Type (ADT) untuk sebuah produk.
    """
    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"ID: {self.id_produk} | Nama: {self.nama} | Harga: Rp{self.harga} | Stok: {self.stok}"


class SistemInventaris:
    """
    Sistem manajemen inventaris menggunakan Hash Table (Python Dictionary)
    untuk mencapai kompleksitas waktu rata-rata O(1).
    """
    def __init__(self):
        # Struktur data terpilih: Hash Table (dict)
        # Key: ID Produk (string), Value: Objek Produk (ADT)
        self.inventaris = {}

    def insert_produk(self, id_produk, nama, harga, stok):
        # Kompleksitas Waktu: O(1)
        if id_produk in self.inventaris:
            print(f"[GAGAL] Produk dengan ID '{id_produk}' sudah terdaftar di sistem.")
        else:
            produk_baru = Produk(id_produk, nama, harga, stok)
            self.inventaris[id_produk] = produk_baru
            print(f"[SUKSES] Produk '{nama}' berhasil didaftarkan.")

    def search_produk(self, id_produk):
        # Kompleksitas Waktu: O(1)
        if id_produk in self.inventaris:
            print("[DITEMUKAN] Detail Produk:")
            print(self.inventaris[id_produk])
        else:
            print(f"[TIDAK DITEMUKAN] Produk dengan ID '{id_produk}' tidak ada di inventaris.")

    def delete_produk(self, id_produk):
        # Kompleksitas Waktu: O(1)
        if id_produk in self.inventaris:
            produk_dihapus = self.inventaris.pop(id_produk)
            print(f"[SUKSES] Produk '{produk_dihapus.nama}' berhasil dihapus dari sistem.")
        else:
            print(f"[GAGAL] Penghapusan gagal. Produk dengan ID '{id_produk}' tidak ditemukan.")


def main():
    sistem = SistemInventaris()
    
    while True:
        print("\n" + "="*40)
        print(" SISTEM MANAJEMEN INVENTARIS PRODUK")
        print("="*40)
        print("1. Daftar Produk Baru (Insert)")
        print("2. Cari Detail Produk (Search)")
        print("3. Hapus Produk (Delete)")
        print("4. Keluar (Exit)")
        print("="*40)
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            print("\n-- Pendaftaran Produk --")
            id_produk = input("Masukkan ID Produk (contoh: PRD001): ")
            nama = input("Masukkan Nama Produk: ")
            harga = input("Masukkan Harga: ")
            stok = input("Masukkan Stok: ")
            sistem.insert_produk(id_produk, nama, harga, stok)
            
        elif pilihan == '2':
            print("\n-- Pencarian Produk --")
            id_produk = input("Masukkan ID Produk yang dicari: ")
            sistem.search_produk(id_produk)
            
        elif pilihan == '3':
            print("\n-- Penghapusan Produk --")
            id_produk = input("Masukkan ID Produk yang akan dihapus: ")
            sistem.delete_produk(id_produk)
            
        elif pilihan == '4':
            print("\nKeluar dari sistem. Terima kasih!")
            break
            
        else:
            print("\n[ERROR] Pilihan tidak valid. Silakan masukkan angka 1-4.")

if __name__ == "__main__":
    main()
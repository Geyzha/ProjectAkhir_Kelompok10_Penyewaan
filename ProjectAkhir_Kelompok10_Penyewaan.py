import datetime
import os
import re

# ---------------------------
# Data admin
# ---------------------------
admin = {
    "geyzha": "jiko332",
    "fira": "fhra128"
}

# ---------------------------
# Data alat pendakian
# Struktur: alat_pendakian[jenis][tipe][merek] = {"harga": harga_per_hari, "stok": n}
# ---------------------------
alat_pendakian = {
    "Carrier": {
        "30L": {
            "Consina": {"harga": 30000, "stok": 7},
            "Eiger": {"harga": 32000, "stok": 7},
            "Rei": {"harga": 35000, "stok": 6}
        },
        "40L": {
            "Consina": {"harga": 35000, "stok": 5},
            "Eiger": {"harga": 37000, "stok": 5},
            "Rei": {"harga": 40000, "stok": 5}
        },
        "60L": {
            "Consina": {"harga": 40000, "stok": 4},
            "Eiger": {"harga": 42000, "stok": 4},
            "Rei": {"harga": 45000, "stok": 4}
        },
        "80L": {
            "Consina": {"harga": 50000, "stok": 3},
            "Eiger": {"harga": 52000, "stok": 4},
            "Rei": {"harga": 55000, "stok": 3}
        }
    },
    "Tracking Pole": {
        "Aluminium": {
            "Consina": {"harga": 15000, "stok": 12},
            "Eiger": {"harga": 17000, "stok": 12},
            "Rei": {"harga": 18000, "stok": 11}
        },
        "Carbon": {
            "Consina": {"harga": 25000, "stok": 8},
            "Eiger": {"harga": 27000, "stok": 9},
            "Rei": {"harga": 30000, "stok": 8}
        }
    },
    "Nesting": {
        "Kecil": {
            "Consina": {"harga": 10000, "stok": 8},
            "Eiger": {"harga": 12000, "stok": 9},
            "Rei": {"harga": 13000, "stok": 8}
        },
        "Sedang": {
            "Consina": {"harga": 15000, "stok": 7},
            "Eiger": {"harga": 17000, "stok": 7},
            "Rei": {"harga": 18000, "stok": 6}
        },
        "Besar": {
            "Consina": {"harga": 20000, "stok": 3},
            "Eiger": {"harga": 22000, "stok": 4},
            "Rei": {"harga": 25000, "stok": 3}
        }
    },
    "Tenda": {
        "2P": {
            "Consina": {"harga": 40000, "stok": 4},
            "Eiger": {"harga": 42000, "stok": 4},
            "Rei": {"harga": 45000, "stok": 4}
        },
        "4P": {
            "Consina": {"harga": 60000, "stok": 3},
            "Eiger": {"harga": 62000, "stok": 4},
            "Rei": {"harga": 65000, "stok": 3}
        },
        "6P": {
            "Consina": {"harga": 80000, "stok": 3},
            "Eiger": {"harga": 82000, "stok": 4},
            "Rei": {"harga": 85000, "stok": 3}
        }
    }
}

# ---------------------------
# Global lists
# ---------------------------
daftar_penyewa = []
riwayat_pengembalian = []

# ---------------------------
# Util functions
# ---------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nTekan Enter untuk melanjutkan...")

def print_line(char="-", length=120):
    print(char * length)

def format_rupiah(amount):
    return "Rp{:,}".format(int(round(amount))).replace(",", ".")

def validasi_input_alfanumerik(prompt, error_msg="Input tidak valid! Harus diawali dengan huruf."):
    """Validasi input harus tidak kosong, tidak hanya spasi, dan diawali huruf.
       Mengizinkan spasi dan angka setelah karakter pertama."""
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("Input tidak boleh kosong atau hanya spasi!")
            continue
        if nilai[0].isalpha():
            return nilai
        else:
            print(error_msg)

def login_admin():
    clear_screen()
    print("=" * 40)
    print("LOGIN ADMIN".center(40))
    print("=" * 40)

    kesempatan = 3
    while kesempatan > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in admin and admin[username] == password:
            print("\n✓ Login berhasil! Selamat datang,", username)
            pause()
            return True
        else:
            kesempatan -= 1
            print(f"✗ Login gagal! Sisa percobaan: {kesempatan}\n")

    print("\nAkses ditolak! Program dihentikan.")
    exit()

# ---------------------------
# CRUD alat
# ---------------------------
def tambah_alat():
    print("\n=== Tambah Alat Baru ===")
    while True:
        jenis = input("Nama alat baru       : ").title().strip()
        if not jenis:
            print("✗ Nama alat tidak boleh kosong!")
            continue
        break
    while True:
        tipe = input("Tipe alat            : ").title().strip()
        if not tipe:
            print("✗ Tipe alat tidak boleh kosong!")
            continue
        break
    while True:
        merek = input("Merek alat           : ").title().strip()
        if not merek:
            print("✗ Merek alat tidak boleh kosong!")
            continue
        break
    while True:
        try:
            harga = int(input("Harga sewa per hari  : "))
            if harga <= 0:
                print("✗ Harga harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("✗ Input tidak valid! Harga harus berupa angka.")
    while True:
        try:
            stok = int(input("Stok tersedia        : "))
            if stok < 0:
                print("✗ Stok tidak boleh negatif!")
                continue
            break
        except ValueError:
            print("✗ Input tidak valid! Stok harus berupa angka.")

    if jenis not in alat_pendakian:
        alat_pendakian[jenis] = {}
    if tipe not in alat_pendakian[jenis]:
        alat_pendakian[jenis][tipe] = {}
    alat_pendakian[jenis][tipe][merek] = {"harga": harga, "stok": stok}
    print("✓ Alat berhasil ditambahkan!")

def tampilkan_alat():
    print("\n=== Daftar Alat Pendakian ===")
    if not alat_pendakian:
        print("Belum ada alat tersedia.")
        return
    for jenis, tipe_dict in alat_pendakian.items():
        print(f"\n{jenis}:")
        for tipe, merek_dict in tipe_dict.items():
            print(f"  {tipe}:")
            for merek, detail in merek_dict.items():
                print(f"    - {merek:15} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")

def update_alat():
    print("\n=== Update Data Alat ===")
    tampilkan_alat()
    if not alat_pendakian:
        return
    while True:
        jenis = input("\nMasukkan nama alat yang ingin diupdate: ").title().strip()
        if jenis not in alat_pendakian:
            print("✗ Alat tidak ditemukan! Silakan coba lagi.")
            continue
        break
    while True:
        tipe = input("Masukkan tipe alat yang ingin diupdate: ").title().strip()
        if tipe not in alat_pendakian[jenis]:
            print("✗ Tipe tidak ditemukan! Silakan coba lagi.")
            continue
        break
    while True:
        merek = input("Masukkan merek alat yang ingin diupdate: ").title().strip()
        if merek not in alat_pendakian[jenis][tipe]:
            print("✗ Merek tidak ditemukan! Silakan coba lagi.")
            continue
        break
    print("\nData saat ini:")
    print(f"Harga: {format_rupiah(alat_pendakian[jenis][tipe][merek]['harga'])}")
    print(f"Stok: {alat_pendakian[jenis][tipe][merek]['stok']}")
    while True:
        try:
            harga_baru = int(input("\nMasukkan harga baru: "))
            if harga_baru <= 0:
                print("✗ Harga harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("✗ Input tidak valid! Harga harus berupa angka.")
    while True:
        try:
            stok_baru = int(input("Masukkan stok baru: "))
            if stok_baru < 0:
                print("✗ Stok tidak boleh negatif!")
                continue
            break
        except ValueError:
            print("✗ Input tidak valid! Stok harus berupa angka.")
    alat_pendakian[jenis][tipe][merek] = {"harga": harga_baru, "stok": stok_baru}
    print("✓ Data alat berhasil diupdate!")

def hapus_alat():
    print("\n=== Hapus Alat ===")
    tampilkan_alat()
    if not alat_pendakian:
        return
    while True:
        jenis = input("\nMasukkan nama alat yang ingin dihapus: ").title().strip()
        if jenis not in alat_pendakian:
            print("✗ Alat tidak ditemukan! Silakan coba lagi.")
            continue
        break
    while True:
        tipe = input("Masukkan tipe alat yang ingin dihapus: ").title().strip()
        if tipe not in alat_pendakian[jenis]:
            print("✗ Tipe tidak ditemukan! Silakan coba lagi.")
            continue
        break
    while True:
        merek = input("Masukkan merek alat yang ingin dihapus: ").title().strip()
        if merek not in alat_pendakian[jenis][tipe]:
            print("✗ Merek tidak ditemukan! Silakan coba lagi.")
            continue
        break
    while True:
        konfirmasi = input(f"Yakin ingin menghapus {jenis} - {tipe} - {merek}? (y/n): ").lower().strip()
        if konfirmasi == 'y':
            del alat_pendakian[jenis][tipe][merek]
            if not alat_pendakian[jenis][tipe]:
                del alat_pendakian[jenis][tipe]
            if not alat_pendakian[jenis]:
                del alat_pendakian[jenis]
            print("✓ Alat berhasil dihapus!")
            break
        elif konfirmasi == 'n':
            print("Penghapusan dibatalkan.")
            break
        else:
            print("✗ Input tidak valid! Masukkan 'y' atau 'n'.")

# ---------------------------
# Pencarian
# ---------------------------
def cari_alat():
    print("\n=== Cari Alat ===")
    print("1. Cari berdasarkan Jenis")
    print("2. Cari berdasarkan Tipe")
    print("3. Cari berdasarkan Merek")
    print("4. Cari berdasarkan Range Harga")
    print("5. Cari berdasarkan Stok Tersedia")
    while True:
        pilihan = input("\nPilih kriteria pencarian (1-5): ").strip()
        if pilihan == "1":
            while True:
                jenis = input("Masukkan jenis alat: ").title().strip()
                if not jenis:
                    print("✗ Jenis tidak boleh kosong!")
                    continue
                break
            print(f"\n--- Hasil Pencarian: {jenis} ---")
            if jenis in alat_pendakian:
                for tipe, merek_dict in alat_pendakian[jenis].items():
                    for merek, detail in merek_dict.items():
                        print(f"{jenis} - {tipe} - {merek} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
            else:
                print("Tidak ditemukan!")
            break
        elif pilihan == "2":
            while True:
                tipe_cari = input("Masukkan tipe alat: ").title().strip()
                if not tipe_cari:
                    print("✗ Tipe tidak boleh kosong!")
                    continue
                break
            print(f"\n--- Hasil Pencarian: {tipe_cari} ---")
            found = False
            for jenis, tipe_dict in alat_pendakian.items():
                if tipe_cari in tipe_dict:
                    for merek, detail in tipe_dict[tipe_cari].items():
                        print(f"{jenis} - {tipe_cari} - {merek} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
                        found = True
            if not found:
                print("Tidak ditemukan!")
            break
        elif pilihan == "3":
            while True:
                merek_cari = input("Masukkan merek alat: ").title().strip()
                if not merek_cari:
                    print("✗ Merek tidak boleh kosong!")
                    continue
                break
            print(f"\n--- Hasil Pencarian: {merek_cari} ---")
            found = False
            for jenis, tipe_dict in alat_pendakian.items():
                for tipe, merek_dict in tipe_dict.items():
                    if merek_cari in merek_dict:
                        detail = merek_dict[merek_cari]
                        print(f"{jenis} - {tipe} - {merek_cari} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
                        found = True
            if not found:
                print("Tidak ditemukan!")
            break
        elif pilihan == "4":
            while True:
                try:
                    min_harga = int(input("Harga minimum: "))
                    if min_harga < 0:
                        print("✗ Harga tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("✗ Input tidak valid! Masukkan angka.")
            while True:
                try:
                    max_harga = int(input("Harga maksimum: "))
                    if max_harga < min_harga:
                        print("✗ Harga maksimum harus lebih besar dari harga minimum!")
                        continue
                    break
                except ValueError:
                    print("✗ Input tidak valid! Masukkan angka.")
            print(f"\n--- Hasil Pencarian: Rp{min_harga:,} - Rp{max_harga:,} ---")
            found = False
            for jenis, tipe_dict in alat_pendakian.items():
                for tipe, merek_dict in tipe_dict.items():
                    for merek, detail in merek_dict.items():
                        if min_harga <= detail['harga'] <= max_harga:
                            print(f"{jenis} - {tipe} - {merek} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
                            found = True
            if not found:
                print("Tidak ditemukan!")
            break
        elif pilihan == "5":
            while True:
                try:
                    min_stok = int(input("Stok minimum: "))
                    if min_stok < 0:
                        print("✗ Stok tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("✗ Input tidak valid! Masukkan angka.")
            print(f"\n--- Hasil Pencarian: Stok >= {min_stok} ---")
            found = False
            for jenis, tipe_dict in alat_pendakian.items():
                for tipe, merek_dict in tipe_dict.items():
                    for merek, detail in merek_dict.items():
                        if detail['stok'] >= min_stok:
                            print(f"{jenis} - {tipe} - {merek} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
                            found = True
            if not found:
                print("Tidak ditemukan!")
            break
        else:
            print("✗ Pilihan tidak valid! Masukkan angka 1-5.")

# ---------------------------
# Sewa alat
# ---------------------------
def sewa_alat():
    print("\n=== Menu Sewa Alat ===")
    tampilkan_alat()
    if not alat_pendakian:
        return
    nama = validasi_input_alfanumerik("\nNama penyewa: ", "Nama harus diawali dengan huruf!").title()
    while True:
        no_telp = input("Nomor telepon (11-12 digit): ").strip()
        if no_telp.isdigit() and 11 <= len(no_telp) <= 12:
            break
        else:
            print("✗ No telepon tidak valid! Harus 11-12 digit angka.")
    while True:
        print("\nJenis Jaminan:")
        print("1. KTP")
        print("2. SIM")
        pilihan_jaminan = input("Pilih jenis jaminan (1/2): ").strip()
        if pilihan_jaminan == "1":
            jenis_jaminan = "KTP"
            break
        elif pilihan_jaminan == "2":
            jenis_jaminan = "SIM"
            break
        else:
            print("✗ Pilihan jaminan tidak valid! Masukkan 1 atau 2.")
    while True:
        no_jaminan = input(f"Nomor {jenis_jaminan}: ").strip()
        if not no_jaminan:
            print(f"✗ Nomor {jenis_jaminan} tidak boleh kosong!")
            continue
        if pilihan_jaminan == "1":
            if no_jaminan.isdigit() and len(no_jaminan) <= 16:
                break
            else:
                print(f"✗ Nomor {jenis_jaminan} tidak valid! Harus berupa angka maksimal 16 digit.")
        elif pilihan_jaminan == "2":
            if no_jaminan.isalnum() and len(no_jaminan) <= 16:
                break
            else:
                print(f"✗ Nomor {jenis_jaminan} tidak valid! Harus alfanumerik maksimal 16 karakter.")
    while True:
        jenis = input("\nPilih alat yang ingin disewa: ").title().strip()
        if jenis not in alat_pendakian:
            print("✗ Alat tidak tersedia! Silakan coba lagi.")
            continue
        break
    print("\nTipe tersedia:")
    for tipe, merek_dict in alat_pendakian[jenis].items():
        total_stok = sum(detail['stok'] for detail in merek_dict.values())
        print(f"- {tipe} (Total Stok: {total_stok})")
    while True:
        tipe = input("\nPilih tipe: ").title().strip()
        if tipe not in alat_pendakian[jenis]:
            print("✗ Tipe tidak tersedia! Silakan coba lagi.")
            continue
        break
    print("\nMerek tersedia:")
    for merek, detail in alat_pendakian[jenis][tipe].items():
        print(f"- {merek} | Harga: {format_rupiah(detail['harga'])}/hari | Stok: {detail['stok']}")
    while True:
        merek = input("\nPilih merek: ").title().strip()
        if merek not in alat_pendakian[jenis][tipe]:
            print("✗ Merek tidak tersedia! Silakan coba lagi.")
            continue
        if alat_pendakian[jenis][tipe][merek]['stok'] <= 0:
            print("✗ Stok habis! Silakan pilih merek lain.")
            continue
        break
    while True:
        try:
            lama = int(input("Lama sewa (hari, max 5 hari): "))
            if 1 <= lama <= 5:
                break
            else:
                print("✗ Lama sewa harus 1-5 hari!")
        except ValueError:
            print("✗ Input tidak valid! Masukkan angka.")
    while True:
        print("\nKondisi Barang Saat Disewakan:")
        print("1. Bagus")
        print("2. Cacat")
        pilihan_kondisi = input("Pilih kondisi barang (1/2): ").strip()
        if pilihan_kondisi == "1":
            kondisi_sewa = "Bagus"
            break
        elif pilihan_kondisi == "2":
            kondisi_sewa = "Cacat"
            break
        else:
            print("✗ Pilihan kondisi tidak valid! Masukkan 1 atau 2.")
    harga = alat_pendakian[jenis][tipe][merek]['harga']
    total = harga * lama
    tanggal_sewa = datetime.datetime.now()
    tanggal_kembali = tanggal_sewa + datetime.timedelta(days=lama)
    # Kurangi stok
    alat_pendakian[jenis][tipe][merek]['stok'] -= 1
    # Pembayaran
    print("\n=== PEMBAYARAN ===")
    print(f"Total Tagihan: {format_rupiah(total)}")
    while True:
        try:
            uang_dibayar = int(input("Masukkan jumlah uang yang dibayar (Rp): "))
            if uang_dibayar < 0:
                print("✗ Nominal harus >= 0")
                continue
            break
        except ValueError:
            print("✗ Input tidak valid! Masukkan angka.")
    if uang_dibayar >= total:
        pembayaran_status = "Lunas"
        kembalian = uang_dibayar - total
        sisa_tagihan = 0
    else:
        pembayaran_status = "DP"
        sisa_tagihan = total - uang_dibayar
        kembalian = 0
    # Struk rapi
    print("\n" + "=" * 60)
    print("OUTDOOR RENTAL ADVENTURE".center(60))
    print("STRUK PENYEWAAN ALAT".center(60))
    print("=" * 60)
    print(f"Tanggal Transaksi : {tanggal_sewa.strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 60)
    print("DATA PENYEWA".center(60))
    print("-" * 60)
    print(f"Nama Penyewa      : {nama}")
    print(f"No. Telepon       : {no_telp}")
    print(f"Jaminan           : {jenis_jaminan} ({no_jaminan})")
    print("-" * 60)
    print("DETAIL PENYEWAAN".center(60))
    print("-" * 60)
    print(f"Alat              : {jenis}")
    print(f"Tipe              : {tipe}")
    print(f"Merek             : {merek}")
    print(f"Kondisi Awal      : {kondisi_sewa}")
    print(f"Harga / Hari      : {format_rupiah(harga)}")
    print(f"Lama Sewa         : {lama} hari")
    print(f"Mulai Sewa        : {tanggal_sewa.strftime('%d-%m-%Y')}")
    print(f"Jatuh Tempo       : {tanggal_kembali.strftime('%d-%m-%Y')}")
    print("-" * 60)
    print(f"TOTAL BIAYA       : {format_rupiah(total)}")
    print("=" * 60)
    print("PEMBAYARAN".center(60))
    print("-" * 60)
    print(f"Status Pembayaran : {pembayaran_status}")
    print(f"Uang Dibayar      : {format_rupiah(uang_dibayar)}")
    if sisa_tagihan > 0:
        print(f"Sisa Tagihan      : {format_rupiah(sisa_tagihan)}")
    print(f"Kembalian         : {format_rupiah(kembalian)}")
    print("-" * 60)
    print("Terima kasih telah menyewa di Outdoor Rental Adventure!".center(60))
    print("Harap kembalikan alat tepat waktu dan dalam kondisi baik.".center(60))
    print("=" * 60)
    # Simpan data penyewa
    daftar_penyewa.append({
        'nama': nama,
        'no_telp': no_telp,
        'jenis_jaminan': jenis_jaminan,
        'no_jaminan': no_jaminan,
        'jenis': jenis,
        'tipe': tipe,
        'merek': merek,
        'kondisi_sewa': kondisi_sewa,
        'tanggal_sewa': tanggal_sewa,
        'lama_hari': lama,
        'tanggal_kembali': tanggal_kembali,
        'total_biaya': total,
        'status': 'Disewa',
        'pembayaran_status': pembayaran_status,
        'uang_dibayar': uang_dibayar,
        'kembalian': kembalian,
        'sisa_tagihan': sisa_tagihan,
        # simpan harga per hari agar evaluasi denda bisa dilakukan dengan mudah
        'harga_per_hari': harga
    })

# ---------------------------
# Pengembalian
# ---------------------------
def kembalikan_alat():
    print("\n=== Pengembalian Alat ===")
    penyewa_aktif = [p for p in daftar_penyewa if p['status'] == 'Disewa']
    if not penyewa_aktif:
        print("Tidak ada penyewaan aktif.")
        return
    print("\nDaftar Penyewaan Aktif:")
    for i, data in enumerate(penyewa_aktif, 1):
        print(f"{i}. {data['nama']} ({data['no_telp']}) - {data['jenis']} {data['tipe']} {data['merek']} - Kondisi: {data['kondisi_sewa']} - Jatuh Tempo: {data['tanggal_kembali'].strftime('%d-%m-%Y')}")
    while True:
        try:
            pilihan = int(input("\nPilih nomor penyewaan untuk dikembalikan: "))
            if 1 <= pilihan <= len(penyewa_aktif):
                break
            else:
                print(f"✗ Nomor tidak valid! Masukkan angka 1-{len(penyewa_aktif)}.")
        except ValueError:
            print("✗ Input tidak valid! Masukkan angka.")
    data = penyewa_aktif[pilihan - 1]
    while True:
        print("\nKondisi Barang Saat Dikembalikan:")
        print("1. Bagus")
        print("2. Cacat")
        print("3. Hilang")
        pilihan_kondisi = input("Pilih kondisi barang (1/2/3): ").strip()
        if pilihan_kondisi == "1":
            kondisi_kembali = "Bagus"
            break
        elif pilihan_kondisi == "2":
            kondisi_kembali = "Cacat"
            break
        elif pilihan_kondisi == "3":
            kondisi_kembali = "Hilang"
            break
        else:
            print("✗ Pilihan kondisi tidak valid! Masukkan 1, 2, atau 3.")
    tanggal_pengembalian = datetime.datetime.now()
    # SELISIH HARI TERLAMBAT (positif = terlambat)
    selisih_hari = (tanggal_pengembalian.date() - data['tanggal_kembali'].date()).days
    # Harga barang = harga per hari * 20 (aturan yang dipilih)
    harga_per_hari = data.get('harga_per_hari', 0)
    harga_barang = harga_per_hari * 20
    # Denda kondisi berdasarkan aturan:
    # - Bagus -> Bagus: 0
    # - Bagus -> Cacat: 100% harga_barang
    # - Bagus -> Hilang: 200% harga_barang
    # - Cacat -> Bagus: 0
    # - Cacat -> Cacat: 0
    # - Cacat -> Hilang: 200% harga_barang
    kondisi_awal = data.get('kondisi_sewa', 'Bagus')
    denda_kondisi = 0
    if kondisi_awal == "Bagus" and kondisi_kembali == "Cacat":
        denda_kondisi = int(round(harga_barang * 1.0))
        print(f"⚠ Barang dikembalikan dalam kondisi CACAT! Denda = 100% harga barang -> {format_rupiah(denda_kondisi)}")
    elif kondisi_awal == "Bagus" and kondisi_kembali == "Hilang":
        denda_kondisi = int(round(harga_barang * 2.0))
        print(f"⚠ Barang HILANG! Denda ganti rugi = 200% harga barang -> {format_rupiah(denda_kondisi)}")
    elif kondisi_awal == "Cacat" and kondisi_kembali == "Hilang":
        denda_kondisi = int(round(harga_barang * 2.0))
        print(f"⚠ Barang HILANG (sebelumnya cacat)! Denda ganti rugi = 200% harga barang -> {format_rupiah(denda_kondisi)}")
    else:
        # semua kondisi lain dianggap tidak kena denda kondisi
        denda_kondisi = 0
        if kondisi_kembali == "Bagus":
            print("\n✓ Barang kembali dalam kondisi baik.")
        else:
            # Cacat->Cacat atau Bagus->Bagus => no charge
            if kondisi_kembali == "Cacat":
                print("\n✓ Barang dikembalikan dalam kondisi cacat (tidak ada denda tambahan yang dikenakan berdasarkan aturan saat ini).")
    # Denda keterlambatan: 10% PER HARI dari harga_barang
    denda_telat = 0
    if selisih_hari > 0:
        denda_telat = int(round(selisih_hari * harga_barang * 0.1))
        print(f"\n⚠ Terlambat {selisih_hari} hari! Denda keterlambatan = 10%/hari dari harga barang -> {format_rupiah(denda_telat)}")
    else:
        print("\n✓ Pengembalian tepat waktu atau lebih awal.")
    total_denda = denda_kondisi + denda_telat
    # Sisa tagihan awal (jika DP)
    sisa_tagihan_awal = data.get('sisa_tagihan', 0)
    # Total harus dibayar saat pengembalian = denda + sisa_tagihan_awal
    total_yang_harus_dibayar = int(round(total_denda + sisa_tagihan_awal))
    # Tampilkan rincian
    print(f"\n--- RINCIAN PEMBAYARAN ---")
    print(f"Biaya Sewa        : {format_rupiah(data.get('total_biaya', 0))}")
    if denda_telat > 0:
        print(f"Denda Keterlambatan: {format_rupiah(denda_telat)}")
    if denda_kondisi > 0:
        print(f"Denda Kondisi     : {format_rupiah(denda_kondisi)}")
    if sisa_tagihan_awal > 0:
        print(f"Sisa Tagihan (DP) : {format_rupiah(sisa_tagihan_awal)}")
    print(f"Total yang harus dibayar saat pengembalian: {format_rupiah(total_yang_harus_dibayar)}")
    print(f"\n✓ Jaminan {data['jenis_jaminan']} ({data['no_jaminan']}) dapat dikembalikan kepada {data['nama']}")
    # Jika barang tidak hilang, kembalikan stok
    if kondisi_kembali != "Hilang":
        # Pastikan struktur ada
        try:
            alat_pendakian[data['jenis']][data['tipe']][data['merek']]['stok'] += 1
        except Exception:
            # Jika terjadi kesalahan struktur, abaikan peningkatan stok (untuk menghindari crash)
            pass
    # Pembayaran pelunasan
    jumlah_bayar_pengembalian = 0
    if total_yang_harus_dibayar > 0:
        while True:
            try:
                jumlah_bayar_pengembalian = int(input("Masukkan jumlah yang dibayar saat pengembalian (Rp): "))
                if jumlah_bayar_pengembalian < 0:
                    print("✗ Nominal harus >= 0")
                    continue
                break
            except ValueError:
                print("✗ Input tidak valid! Masukkan angka.")
    else:
        print("Tidak ada tagihan tambahan pada saat pengembalian.")
    # Hitung kembalian atau sisa
    if jumlah_bayar_pengembalian >= total_yang_harus_dibayar:
        kembalian_pengembalian = jumlah_bayar_pengembalian - total_yang_harus_dibayar
        sisa_tagihan_setelah = 0
    else:
        kembalian_pengembalian = 0
        sisa_tagihan_setelah = total_yang_harus_dibayar - jumlah_bayar_pengembalian
    if sisa_tagihan_setelah == 0:
        pembayaran_status_baru = 'Lunas'
    else:
        pembayaran_status_baru = f"DP (sisa Rp{sisa_tagihan_setelah:,})"
    # Update record penyewa
    data['status'] = 'Dikembalikan'
    data['kondisi_kembali'] = kondisi_kembali
    data['denda_telat'] = denda_telat
    data['denda_kondisi'] = denda_kondisi
    data['total_denda'] = total_denda
    data['tanggal_pengembalian'] = tanggal_pengembalian
    uang_dibayar_awal = data.get('uang_dibayar', 0)
    data['uang_dibayar'] = uang_dibayar_awal + jumlah_bayar_pengembalian
    data['sisa_tagihan'] = sisa_tagihan_setelah
    data['kembalian_pengembalian'] = kembalian_pengembalian
    data['pembayaran_status'] = pembayaran_status_baru
    # Save to riwayat (lengkap)
    riwayat_pengembalian.append({
        'nama': data['nama'],
        'no_telp': data['no_telp'],
        'jenis_jaminan': data['jenis_jaminan'],
        'no_jaminan': data['no_jaminan'],
        'jenis': data['jenis'],
        'tipe': data['tipe'],
        'merek': data['merek'],
        'kondisi_sewa': kondisi_awal,
        'kondisi_kembali': kondisi_kembali,
        'tanggal_sewa': data['tanggal_sewa'],
        'tanggal_kembali': tanggal_pengembalian,
        'denda_telat': denda_telat,
        'denda_kondisi': denda_kondisi,
        'total_denda': total_denda,
        'total_bayar': data['uang_dibayar'],
        'pembayaran_status': pembayaran_status_baru,
        'sisa_tagihan': sisa_tagihan_setelah,
        'kembalian_pengembalian': kembalian_pengembalian
    })
    # Struk pelunasan pengembalian
    print("\n--- STRUK PELUNASAN PENGEMBALIAN ---")
    print("=" * 60)
    print(f"Tanggal Pengembalian : {tanggal_pengembalian.strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 60)
    print(f"Penyewa            : {data['nama']}")
    print(f"Alat               : {data['jenis']} - {data['tipe']} - {data['merek']}")
    print(f"Kondisi Saat Sewa  : {kondisi_awal}")
    print(f"Kondisi Saat Kembali: {kondisi_kembali}")
    print("-" * 60)
    print(f"Biaya Sewa         : {format_rupiah(data.get('total_biaya', 0))}")
    if total_denda > 0:
        print(f"Total Denda        : {format_rupiah(total_denda)}")
    if sisa_tagihan_awal > 0:
        print(f"Sisa Tagihan Awal  : {format_rupiah(sisa_tagihan_awal)}")
    print(f"Total Harus Bayar  : {format_rupiah(total_yang_harus_dibayar)}")
    print(f"Bayar Saat Kembali : {format_rupiah(jumlah_bayar_pengembalian)}")
    if kembalian_pengembalian > 0:
        print(f"Kembalian          : {format_rupiah(kembalian_pengembalian)}")
    if sisa_tagihan_setelah > 0:
        print(f"Sisa Tagihan       : {format_rupiah(sisa_tagihan_setelah)}")
    print(f"Status Pembayaran  : {pembayaran_status_baru}")
    print("=" * 60)
    print("✓ Pengembalian berhasil dicatat!")

# ---------------------------
# Laporan
# ---------------------------
def laporan_barang_disewa():
    print("\n" + "=" * 170)
    print("LAPORAN BARANG SEDANG DISEWA".center(170))
    print("=" * 170)
    penyewa_aktif = [p for p in daftar_penyewa if p['status'] == 'Disewa']
    if not penyewa_aktif:
        print("Tidak ada barang yang sedang disewa.".center(170))
        print("=" * 170)
        return
    print(f"{'No':<5} {'Alat':<30} {'Merek':<12} {'Kondisi':<10} {'Penyewa':<18} {'No. Telp':<15} {'Jaminan':<12} {'Tgl Sewa':<12} {'Tgl Kembali':<12} {'Pembayaran':<20} {'Biaya':<15}")
    print_line(length=170)
    for i, data in enumerate(penyewa_aktif, 1):
        alat = f"{data['jenis']} - {data['tipe']}"
        tgl_sewa = data['tanggal_sewa'].strftime('%d-%m-%Y')
        tgl_kembali = data['tanggal_kembali'].strftime('%d-%m-%Y')
        biaya = format_rupiah(data['total_biaya'])
        jaminan = data['jenis_jaminan']
        kondisi = data['kondisi_sewa']
        merek = data['merek']
        pembayaran = data.get('pembayaran_status', 'Belum Bayar')
        if pembayaran == 'DP':
            sisa = data.get('sisa_tagihan', 0)
            pembayaran = f"DP (sisa {format_rupiah(sisa)})"
        elif pembayaran == 'Lunas':
            pembayaran = "Lunas"
        print(f"{i:<5} {alat:<30} {merek:<12} {kondisi:<10} {data['nama']:<18} {data['no_telp']:<15} {jaminan:<12} {tgl_sewa:<12} {tgl_kembali:<12} {pembayaran:<20} {biaya:<15}")
    print("=" * 170)

def laporan_barang_dikembalikan():
    print("\n" + "=" * 200)
    print("LAPORAN BARANG DIKEMBALIKAN".center(200))
    print("=" * 200)
    if not riwayat_pengembalian:
        print("Belum ada pengembalian.".center(200))
        print("=" * 200)
        return
    print(f"{'No':<4} {'Alat':<25} {'Merek':<12} {'Penyewa':<18} {'No.Telp':<13} {'Kondisi Sewa':<14} {'Kembali':<10} {'Pembayaran':<20} {'Tgl Sewa':<11} {'Tgl Kembali':<11} {'Denda Telat':<13} {'Denda Kondisi':<15} {'Total Bayar':<13}")
    print_line(length=200)
    for i, data in enumerate(riwayat_pengembalian, 1):
        alat = f"{data['jenis']}-{data['tipe']}"
        tgl_sewa = data['tanggal_sewa'].strftime('%d-%m-%Y')
        tgl_kembali = data['tanggal_kembali'].strftime('%d-%m-%Y')
        denda_telat = format_rupiah(data.get('denda_telat', 0))
        denda_kondisi = format_rupiah(data.get('denda_kondisi', 0))
        total = format_rupiah(data.get('total_bayar', data.get('total_denda', 0)))
        kondisi_sewa = data['kondisi_sewa']
        kondisi_kembali = data['kondisi_kembali']
        merek = data['merek']
        pembayaran = data.get('pembayaran_status', 'Belum Bayar')
        sisa = data.get('sisa_tagihan', 0)
        if isinstance(pembayaran, str) and pembayaran.startswith('DP') and sisa > 0:
            pembayaran = f"DP (sisa {format_rupiah(sisa)})"
        print(f"{i:<4} {alat:<25} {merek:<12} {data['nama']:<18} {data['no_telp']:<13} {kondisi_sewa:<14} {kondisi_kembali:<10} {pembayaran:<20} {tgl_sewa:<11} {tgl_kembali:<11} {denda_telat:<13} {denda_kondisi:<15} {total:<13}")
    print("=" * 200)

def laporan_penyewa():
    print("\n" + "=" * 100)
    print("LAPORAN NAMA PENYEWA".center(100))
    print("=" * 100)
    if not daftar_penyewa:
        print("Belum ada penyewa.".center(100))
        print("=" * 100)
        return
    penyewa_dict = {}
    for data in daftar_penyewa:
        nama = data['nama']
        if nama not in penyewa_dict:
            penyewa_dict[nama] = {'no_telp': data['no_telp'], 'data': []}
        penyewa_dict[nama]['data'].append(data)
    print(f"{'No':<5} {'Nama Penyewa':<25} {'No. Telepon':<18} {'Total Penyewaan':<20} {'Total Pengeluaran':<25}")
    print_line(length=100)
    for i, (nama, info) in enumerate(penyewa_dict.items(), 1):
        total_biaya = sum(d.get('total_bayar', d.get('total_biaya', 0)) for d in info['data'])
        print(f"{i:<5} {nama:<25} {info['no_telp']:<18} {len(info['data']):^20} {format_rupiah(total_biaya):<25}")
    print("=" * 100)

def laporan_barang_terpopuler():
    print("\n" + "=" * 80)
    print("LAPORAN BARANG PALING SERING DISEWA".center(80))
    print("=" * 80)
    if not daftar_penyewa:
        print("Belum ada data penyewaan.".center(80))
        print("=" * 80)
        return
    barang_count = {}
    for data in daftar_penyewa:
        key = f"{data['jenis']} - {data['tipe']} - {data['merek']}"
        barang_count[key] = barang_count.get(key, 0) + 1
    sorted_barang = sorted(barang_count.items(), key=lambda x: x[1], reverse=True)
    print(f"{'Ranking':<10} {'Nama Alat':<50} {'Jumlah Disewa':<20}")
    print_line(length=80)
    for i, (barang, count) in enumerate(sorted_barang, 1):
        print(f"{i:<10} {barang:<50} {count:^20}")
    print("=" * 80)

def laporan_penyewa_terbanyak():
    print("\n" + "=" * 90)
    print("LAPORAN ORANG PALING SERING MENYEWA".center(90))
    print("=" * 90)
    if not daftar_penyewa:
        print("Belum ada data penyewa.".center(90))
        print("=" * 90)
        return
    penyewa_count = {}
    for data in daftar_penyewa:
        nama = data['nama']
        if nama not in penyewa_count:
            penyewa_count[nama] = {'no_telp': data['no_telp'], 'count': 0}
        penyewa_count[nama]['count'] += 1
    sorted_penyewa = sorted(penyewa_count.items(), key=lambda x: x[1]['count'], reverse=True)
    print(f"{'Ranking':<10} {'Nama Penyewa':<35} {'No. Telepon':<20} {'Jumlah Sewa':<20}")
    print_line(length=90)
    for i, (nama, info) in enumerate(sorted_penyewa, 1):
        print(f"{i:<10} {nama:<35} {info['no_telp']:<20} {info['count']:^20}")
    print("=" * 90)

# ---------------------------
# Cari penyewa
# ---------------------------
def cari_penyewa():
    print("\n" + "=" * 130)
    print("CARI PENYEWA".center(130))
    print("=" * 130)
    if not daftar_penyewa:
        print("Belum ada data penyewa.".center(130))
        print("=" * 130)
        return
    keyword = input("Masukkan nama penyewa atau nomor telepon: ").lower().strip()
    hasil = []
    for data in daftar_penyewa:
        nama = data['nama'].lower()
        nomor = data['no_telp'].lower()
        if keyword in nama or keyword in nomor:
            hasil.append(data)
    if not hasil:
        print("\nPenyewa tidak ditemukan.")
        print("=" * 130)
        return
    print("\nHASIL PENCARIAN:\n")
    for i, data in enumerate(hasil, 1):
        print(f"{i}. Nama            : {data['nama']}")
        print(f"   Nomor Telepon   : {data['no_telp']}")
        print(f"   Alat Disewa     : {data['jenis']} - {data['tipe']} - {data['merek']}")
        print(f"   Kondisi Sewa    : {data['kondisi_sewa']}")
        print(f"   Tanggal Sewa    : {data['tanggal_sewa'].strftime('%d-%m-%Y')}")
        pembayaran = data.get('pembayaran_status', 'Belum Bayar')
        sisa = data.get('sisa_tagihan', 0)
        if pembayaran == 'Lunas':
            print(f"   Pembayaran      : Lunas ({format_rupiah(data.get('uang_dibayar',0))})")
        elif pembayaran == 'DP':
            print(f"   Pembayaran      : DP | Bayar: {format_rupiah(data.get('uang_dibayar',0))} | Sisa: {format_rupiah(sisa)}")
        else:
            print(f"   Pembayaran      : {pembayaran}")
        if data['status'] == "Dikembalikan":
            print(f"   Tanggal Kembali : {data['tanggal_pengembalian'].strftime('%d-%m-%Y')}")
            print(f"   Total Bayar     : {format_rupiah(data.get('total_bayar', data.get('uang_dibayar',0)))}")
            print(f"   Status          : Dikembalikan")
        else:
            print(f"   Tanggal Kembali : {data['tanggal_kembali'].strftime('%d-%m-%Y')}")
            print(f"   Total Biaya     : {format_rupiah(data['total_biaya'])}")
            print(f"   Status          : Disewa")
        print("-" * 130)
    print("=" * 130)

# Function to show current penyewa (keperluan menu)
def tampilkan_penyewa():
    print("\n=== Daftar Penyewa Aktif ===")
    if not daftar_penyewa:
        print("Belum ada penyewaan aktif.")
        return
    penyewa_aktif = [p for p in daftar_penyewa if p['status'] == 'Disewa']
    if not penyewa_aktif:
        print("Belum ada penyewaan aktif.")
        return
    for i, data in enumerate(penyewa_aktif, 1):
        print(f"\n{i}. Nama: {data['nama']}")
        print(f"   No. Telepon: {data['no_telp']}")
        print(f"   Jaminan: {data['jenis_jaminan']} - {data['no_jaminan']}")
        print(f"   Alat: {data['jenis']} - {data['tipe']} - {data['merek']}")
        print(f"   Kondisi Saat Disewa: {data['kondisi_sewa']}")
        print(f"   Tanggal Sewa: {data['tanggal_sewa'].strftime('%d-%m-%Y %H:%M')}")
        print(f"   Tanggal Kembali: {data['tanggal_kembali'].strftime('%d-%m-%Y')}")
        print(f"   Total Biaya: {format_rupiah(data['total_biaya'])}")
        ps = data.get('pembayaran_status', 'Belum Bayar')
        ub = data.get('uang_dibayar', 0)
        sisa = data.get('sisa_tagihan', 0)
        if ps == 'Lunas':
            print(f"   Pembayaran: {ps} ({format_rupiah(ub)})")
        elif ps == 'DP':
            print(f"   Pembayaran: {ps} (Bayar {format_rupiah(ub)}) | Sisa: {format_rupiah(sisa)}")
        else:
            print(f"   Pembayaran: {ps}")
        print(f"   Status: {data['status']}")
        
# ---------------------------
# Menu
# ---------------------------
def menu_laporan():
    while True:
        print("\n===== MENU LAPORAN =====")
        print("1. Laporan Barang Sedang Disewa")
        print("2. Laporan Barang Dikembalikan")
        print("3. Laporan Nama Penyewa")
        print("4. Laporan Barang Paling Sering Disewa")
        print("5. Laporan Orang Paling Sering Menyewa")
        print("6. Cari Penyewa")
        print("0. Kembali")
        pilihan = input("\nPilih menu (0-6): ").strip()
        if pilihan == "1":
            laporan_barang_disewa()
        elif pilihan == "2":
            laporan_barang_dikembalikan()
        elif pilihan == "3":
            laporan_penyewa()
        elif pilihan == "4":
            laporan_barang_terpopuler()
        elif pilihan == "5":
            laporan_penyewa_terbanyak()
        elif pilihan == "6":
            cari_penyewa()
        elif pilihan == "0":
            break
        else:
            print("✗ Pilihan tidak valid! Masukkan angka 0-6.")
        pause()

def menu_crud_barang():
    while True:
        print("\n===== CRUD BARANG =====")
        print("1. Tambah Alat")
        print("2. Lihat Alat")
        print("3. Update Alat")
        print("4. Hapus Alat")
        print("5. Cari Alat")
        print("0. Kembali")
        pilihan = input("\nPilih menu (0-5): ").strip()
        if pilihan == "1":
            tambah_alat()
        elif pilihan == "2":
            tampilkan_alat()
        elif pilihan == "3":
            update_alat()
        elif pilihan == "4":
            hapus_alat()
        elif pilihan == "5":
            cari_alat()
        elif pilihan == "0":
            break
        else:
            print("✗ Pilihan tidak valid! Masukkan angka 0-5.")
        pause()

def menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("  SISTEM PENYEWAAN ALAT PENDAKIAN")
        print("=" * 40)
        print("1. CRUD Barang")
        print("2. Sewa Alat")
        print("3. Lihat Daftar Penyewa")
        print("4. Pengembalian Alat")
        print("5. Laporan")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("\nPilih menu (0-5): ").strip()
        if pilihan == "1":
            menu_crud_barang()
        elif pilihan == "2":
            sewa_alat()
            pause()
        elif pilihan == "3":
            tampilkan_penyewa()
            pause()
        elif pilihan == "4":
            kembalikan_alat()
            pause()
        elif pilihan == "5":
            menu_laporan()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan sistem!")
            break
        else:
            print("✗ Pilihan tidak valid! Masukkan angka 0-5.")
            pause()


# Jalankan program
if __name__ == "__main__":
    if login_admin():
        menu()

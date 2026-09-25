from manusia import PedagangIkanHias, KolektorIkanHias                  # Import class pedagang dan kolektor
from ikan import IkanHiasAirTawar, IkanHiasAirLaut                      # Import class ikan hias tawar dan laut
from peralatan import MediaSubstrat, AkuariumDisplay                    # Import class substrat dan akuarium
from entitas_bisnis import PeternakanIkanHias, TokoAkuarium             # Import class peternakan dan toko

def main():
    print("================================================================================")  # Cetak batas atas header
    print("                SISTEM MANAJEMEN PETERNAKAN & PERDAGANGAN IKAN HIAS             ")  # Cetak judul sistem
    print("================================================================================\n")# Cetak pembatas baris

    # 1. HARDCODE DATA IKAN HIAS 
    ikan_tawar = [  # Array of Objects Ikan Air Tawar
        IkanHiasAirTawar("IKT-01", "Ikan Discus", "Symphysodon", "Merah", "Biru", "hybrid", 150000),        # Objek 1
        IkanHiasAirTawar("IKT-02", "Ikan Louhan", "Amphilophus", "Merah", "Bintik Perak", "hybrid", 350000) # Objek 2
    ]

    ikan_laut = [   # Array of Objects Ikan Air Laut
        IkanHiasAirLaut("IKL-01", "Clownfish (Nemo)", "Amphiprion", "Oranye", "Putih", "spesies", 75000),   # Objek 1
        IkanHiasAirLaut("IKL-02", "Blue Tang (Dory)", "Paracanthurus", "Biru", "Kuning", "spesies", 200000) # Objek 2
    ]

    # 2. HARDCODE DATA PETERNAKAN 
    peternakan_list = [   # Array of Objects Peternakan
        PeternakanIkanHias("PET-01", "Maju Bersama Aquatics", "Bogor", 2012), # Objek Peternakan 1
        PeternakanIkanHias("PET-02", "Nusantara Marine Farm", "Bali", 2018)   # Objek Peternakan 2
    ]
    peternakan_list[0].tambah_ikan_hias(ikan_tawar[0])                  # Menambahkan ikan tawar 1 ke peternakan 1
    peternakan_list[0].tambah_ikan_hias(ikan_tawar[1])                  # Menambahkan ikan tawar 2 ke peternakan 1
    peternakan_list[1].tambah_ikan_hias(ikan_laut[0])                   # Menambahkan ikan laut 1 ke peternakan 2
    peternakan_list[1].tambah_ikan_hias(ikan_laut[1])                   # Menambahkan ikan laut 2 ke peternakan 2

    # 3. HARDCODE DATA AKUARIUM DISPLAY + MEDIA SUBSTRAT (Komposisi)
    akuarium_list = [  # Array of Objects Akuarium Display
        AkuariumDisplay("AKR-01", "Aquascape Forest", 120.0, "tawar"),    # Objek Akuarium 1
        AkuariumDisplay("AKR-02", "Reef Tank Display", 250.0, "laut")     # Objek Akuarium 2
    ]
    akuarium_list[0].set_media_substrat("SUB-01", "Pasir Malang", "pasir", 6.8, "Substrat ideal aquascape")         # Substrat Komposisi 1
    akuarium_list[0].tambah_ikan_hias(ikan_tawar[0])                  # Menambahkan penghuni ikan tawar 1

    akuarium_list[1].set_media_substrat("SUB-02", "Batu Karang Crushed", "batu karang", 8.2, "Menjaga pH air laut") # Substrat Komposisi 2
    akuarium_list[1].tambah_ikan_hias(ikan_laut[0])                   # Menambahkan penghuni ikan laut 1

    # 4. HARDCODE DATA TOKO AKUARIUM + PAKAN (Komposisi)
    toko_list = [  # Array of Objects Toko Akuarium
        TokoAkuarium("TKO-01", "Central Aquarium Store", "Bandung", "offline"), # Objek Toko 1
        TokoAkuarium("TKO-02", "AquaWorld Online", "Jakarta", "online")         # Objek Toko 2
    ]
    toko_list[0].tambah_pakan_ikan("FOD-01", "Hikari Micro Pellets", "buatan", ["Protein 45%", "Vitamin C"], "micro", 45000) # Pakan Komposisi 1
    toko_list[0].tambah_pakan_ikan("FOD-02", "Cacing Sutra Beku", "alami", ["Protein 50%", "Fat 10%"], "medium", 25000)      # Pakan Komposisi 2

    toko_list[1].tambah_pakan_ikan("FOD-03", "Ocean Nutrition Flakes", "buatan", ["Omega 3", "Protein 48%"], "small", 85000) # Pakan Komposisi 3
    toko_list[1].tambah_pakan_ikan("FOD-04", "TetraBits Complete", "buatan", ["Carotenoid", "Protein 47%"], "small", 60000)  # Pakan Komposisi 4

    # 5. HARDCODE DATA PEDAGANG & KOLEKTOR (Inheritance Manusia)
    pedagang_list = [  # Array of Objects Pedagang
        PedagangIkanHias("3273010101900001", "Budi Santoso", "Bandung", 2015, "distributor"), # Objek Pedagang 1
        PedagangIkanHias("3273010101900002", "Hendra Wijaya", "Jakarta", 2019, "reseller")    # Objek Pedagang 2
    ]
    pedagang_list[0].tambah_ikan_hias(ikan_tawar[0])                  # Menambahkan dagangan ikan tawar 1
    pedagang_list[0].tambah_ikan_hias(ikan_laut[0])                   # Menambahkan dagangan ikan laut 1
    pedagang_list[1].tambah_ikan_hias(ikan_tawar[1])                  # Menambahkan dagangan ikan tawar 2

    kolektor_list = [                                                     # Array of Objects Kolektor
        KolektorIkanHias("3171020202910001", "Dr. Ahmad", "Surabaya"),    # Objek Kolektor 1
        KolektorIkanHias("3171020202910002", "Kevin Pratama", "Semarang") # Objek Kolektor 2
    ]
    kolektor_list[0].tambah_ikan_favorit(ikan_tawar[0])               # Menambahkan favorit ikan tawar 1
    kolektor_list[0].tambah_pedagang_langganan(pedagang_list[0])      # Menambahkan langganan pedagang 1
    kolektor_list[0].tambah_akuarium_display(akuarium_list[0])        # Menambahkan akuarium display 1

    kolektor_list[1].tambah_ikan_favorit(ikan_laut[1])                # Menambahkan favorit ikan laut 2
    kolektor_list[1].tambah_pedagang_langganan(pedagang_list[1])      # Menambahkan langganan pedagang 2
    kolektor_list[1].tambah_akuarium_display(akuarium_list[1])        # Menambahkan akuarium display 2

    # DISPLAY DATA SIMULASI
    print("--- 1. DATA IKAN HIAS (AIR TAWAR & LAUT) ---")               # Header seksi ikan hias
    print(f"{'ID':<8} {'Nama Ikan':<22} {'Genus':<15} {'Habitat':<10} {'Warna Utama/Sekunder':<22} {'Harga':<12}") # Header tabel ikan
    print("-" * 90)                                                     # Pembatas tabel
    for t in ikan_tawar:                                                # Iterasi list ikan tawar
        print(f"{t.get_id_ikan():<8} {t.get_nama():<22} {t.get_genus():<15} {'Air Tawar':<10} {t.get_warna_utama()+'/'+t.get_warna_sekunder():<22} Rp{t.get_harga_per_ekor():<10,.0f}") # Print tawar
    for l in ikan_laut:                                                 # Iterasi list ikan laut
        print(f"{l.get_id_ikan():<8} {l.get_nama():<22} {l.get_genus():<15} {'Air Laut':<10} {l.get_warna_utama()+'/'+l.get_warna_sekunder():<22} Rp{l.get_harga_per_ekor():<10,.0f}") # Print laut
    print("\n")                                                         # Baris baru

    print("--- 2. DATA AKUARIUM DISPLAY & MEDIA SUBSTRAT (KOMPOSISI) ---")# Header seksi akuarium
    for akr in akuarium_list:                                             # Iterasi list akuarium
        sub = akr.get_media_substrat()                                    # Ambil objek substrat komposisi
        print(f"[{akr.get_kode_akuarium()}] {akr.get_nama()} | Volume: {akr.get_volume()}L | Air: {akr.get_jenis_air()}") # Print detail akuarium
        if sub:                                                           # Jika substrat ada
            print(f"   └─ Substrat (Komposisi): {sub.get_nama()} [{sub.get_jenis()}] - pH: {sub.get_ph()}") # Print detail substrat
        for ik in akr.get_list_ikan_hias():                               # Iterasi penghuni akuarium
            print(f"   └─ Penghuni: {ik.get_nama()}")                     # Print nama ikan penghuni
    print("-" * 80 + "\n")                                                # Pembatas seksi

    print("--- 3. DATA TOKO AKUARIUM & STOK PAKAN (KOMPOSISI) ---")       # Header seksi toko
    for toko in toko_list:                                                # Iterasi list toko
        print(f"[{toko.get_kode_toko()}] {toko.get_nama()} ({toko.get_jenis_toko_akuarium()}) - {toko.get_alamat()}") # Print detail toko
        print("   Stok Pakan (Komposisi):")                               # Sub-header stok pakan
        for pkn in toko.get_list_pakan_ikan():                            # Iterasi stok pakan komposisi
            print(f"    * [{pkn.get_kode_pakan()}] {pkn.get_nama()} | Kandungan: {', '.join(pkn.get_kandungan())} | Rp{pkn.get_harga_per_kemasan():,.0f}") # Print detail pakan
    print("-" * 80 + "\n")                                                # Pembatas seksi

    print("--- 4. DATA MANUSIA (PEDAGANG & KOLEKTOR IKAN HIAS) ---")      # Header seksi manusia
    print("[PEDAGANG]")                                                   # Sub-header pedagang
    for pdg in pedagang_list:                                             # Iterasi list pedagang
        print(f"KTP: {pdg.get_no_ktp()} | Nama: {pdg.get_nama()} | Jenis: {pdg.get_jenis()} | Dagang Sejak: {pdg.get_tahun_awal_dagang()}") # Print detail pedagang
        for ik in pdg.get_list_ikan_hias():                               # Iterasi dagangan ikan pedagang
            print(f"   -> Dijual: {ik.get_nama()} (Rp{ik.get_harga_per_ekor():,.0f})") # Print item dagangan

    print("\n[KOLEKTOR]")                                                 # Sub-header kolektor
    for klk in kolektor_list:                                             # Iterasi list kolektor
        print(f"KTP: {klk.get_no_ktp()} | Nama: {klk.get_nama()} | Alamat: {klk.get_alamat()}") # Print detail kolektor
        for ik in klk.get_list_ikan_favorit():                            # Iterasi ikan favorit kolektor
            print(f"   -> Ikan Favorit: {ik.get_nama()}")                 # Print item favorit
        for pdg in klk.get_list_pedagang_langganan():                     # Iterasi pedagang langganan kolektor
            print(f"   -> Langganan  : {pdg.get_nama()}")                 # Print item langganan

if __name__ == "__main__":                                                # Pengecekan eksekusi langsung
    main()                                                                # Panggil fungsi main()
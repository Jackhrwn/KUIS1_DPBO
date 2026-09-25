# KUIS1_DPBO

Tugas Kuis 1 Mata Kuliah **Desain dan Pemrograman Berorientasi Objek (DPBO)**.

Program ini mensimulasikan **sistem manajemen peternakan & perdagangan ikan hias** dengan
menerapkan empat konsep utama OOP — *Inheritance*, *Association*, *Aggregation*, dan
*Composition* — pada data ikan hias air tawar/laut, peternakan, akuarium display, toko
akuarium, pedagang, dan kolektor.

| | |
|---|---|
| Bahasa | Python 3 (tanpa dependensi eksternal) |
| Jumlah kelas | 8 |
| Jumlah atribut privat | 45 |
| Entry point | `Program/main.py` |
| Paradigma | Berorientasi Objek |

---

## Janji

> Saya **Jaka Permana Herawan** dengan NIM **2509371** mengerjakan Kuis 1 pada Mata Kuliah
> Desain dan Pemrograman Berorientasi Objek (DPBO) untuk keberkahan-Nya maka saya tidak
> melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin


Dokumendesain lengkap (janji, diagram relasi, dan screenshot output) tersedia pada
[`Desain & Dokumentasi Program.pdf`](Desain%20%26%20Dokumentasi%20Program.pdf).

---

## Struktur Folder

```
KUIS1_DPBO/
├── README.md                          # Dokumentasi proyek (file ini)
├── Desain & Dokumentasi Program.pdf   # Janji, diagram desain, & output program
└── Program/                           # Seluruh source code Python
    ├── main.py                        # Entry point + data simulasi + output
    ├── ikan.py                        # Superclass IkanHias + 2 subclass
    ├── manusia.py                     # Superclass Manusia + 2 subclass
    ├── peralatan.py                   # MediaSubstrat, PakanIkanHias, AkuariumDisplay
    └── entitas_bisnis.py              # PeternakanIkanHias, TokoAkuarium
```

**Pembagian tanggung jawab tiap file:**

| File | Kelas | Tanggung jawab |
|---|---|---|
| `ikan.py` | `IkanHias`, `IkanHiasAirTawar`, `IkanHiasAirLaut` | Model data ikan hias beserta habitatnya |
| `manusia.py` | `Manusia`, `PedagangIkanHias`, `KolektorIkanHias` | aktor/persona yang berinteraksi dengan ikan hias |
| `peralatan.py` | `MediaSubstrat`, `PakanIkanHias`, `AkuariumDisplay` | perlengkapan akuarium dan kebutuhan perawatan |
| `entitas_bisnis.py` | `PeternakanIkanHias`, `TokoAkuarium` | entitas usaha pembudi.dayakan dan perdagangan |
| `main.py` | `main()` | orkestrasi: instansiasi data, relasi, dan cetak laporan |

---

## Penjelasan Atribut

Semua atribut bersifat **privat** (prefix `_`) dan diakses melalui **getter/setter** agar
validasi serta enkapsulasi terjaga.

### 1. `ikan.py` — Hirarki Ikan Hias

#### `IkanHias` (superclass)

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_id_ikan` | `str` | `""` | Kode unik ikan, format `IKT-xx` (tawar) / `IKL-xx` (laut) |
| `_nama` | `str` | `""` | Nama dagang ikan, mis. `Ikan Discus` |
| `_genus` | `str` | `""` | Nama genus ilmiah, mis. `Symphysodon` |
| `_warna_utama` | `str` | `""` | Warna dominan tubuh ikan |
| `_warna_sekunder` | `str` | `""` | Warna pendukung/motif, mis. `Bintik Perak` |
| `_status` | `str` | `"spesies"` | Status koleksi: `spesies` atau `hybrid` |
| `_harga_per_ekor` | `float` | `0.0` | Harga jual satu ekor dalam Rupiah |

#### `IkanHiasAirTawar` & `IkanHiasAirLaut` (subclass)

Keduanya **tidak menambah atribut baru**; seluruh atribut diwarisi dari `IkanHias` dan
dikonstruktor memanggil `super().__init__(...)`. Perbedaannya hanya pada konteks habitat
yang digunakan saat pencetakan laporan.

### 2. `manusia.py` — Hirarki Manusia

#### `Manusia` (superclass)

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_no_ktp` | `str` | `""` | Nomor KTP, acting sebagai primary key |
| `_nama` | `str` | `""` | Nama lengkap |
| `_alamat` | `str` | `""` | Alamat domisili |

#### `PedagangIkanHias` (subclass)

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_tahun_awal_dagang` | `int` | `0` | Tahun mulai berdagang (experience) |
| `_jenis` | `str` | `"reseller"` | Tipe pedagang: `distributor` / `reseller` |
| `_list_ikan_hias` | `list[IkanHias]` | `[]` | Daftar ikan yang dijual (**Agregasi**) |

#### `KolektorIkanHias` (subclass)

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_list_ikan_favorit` | `list[IkanHias]` | `[]` | Ikan hias favorit (**Agregasi**) |
| `_list_pedagang_langganan` | `list[PedagangIkanHias]` | `[]` | Pedagang langganan (**Agregasi**) |
| `_list_akuarium_display` | `list[AkuariumDisplay]` | `[]` | Unit akuarium yang dimiliki (**Agregasi**) |

### 3. `peralatan.py` — Perlengkapan & Akuarium

#### `MediaSubstrat`

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_kode_media` | `str` | `""` | Kode substrat, mis. `SUB-01` |
| `_nama` | `str` | `""` | Nama substrat, mis. `Pasir Malang` |
| `_jenis` | `str` | `"pasir"` | Kategori: `pasir` / `batu karang` / `kerikil` |
| `_ph` | `float` | `7.0` | Target pH air akuarium (setter memaksa `float`) |
| `_keterangan` | `str` | `""` | Catasan fungsi substrat terhadap ekosistem |

#### `PakanIkanHias`

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_kode_pakan` | `str` | `""` | Kode pakan, mis. `FOD-01` |
| `_nama` | `str` | `""` | Nama produk pakan |
| `_jenis` | `str` | `"buatan"` | Asal pakan: ` buatan` / `alami` |
| `_kandungan` | `list[str]` | `[]` | Daftar nutrisi, mis. `["Protein 45%", "Vitamin C"]` |
| `_ukuran_butiran` | `str` | `"small"` | Ukuran butiran: `micro` / `small` / `medium` |
| `_harga_per_kemasan` | `float` | `0.0` | Harga per kemasan dalam Rupiah |

#### `AkuariumDisplay`

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_kode_akuarium` | `str` | `""` | Kode akuarium, mis. `AKR-01` |
| `_nama` | `str` | `""` | Nama tema akuarium |
| `_volume` | `float` | `0.0` | Volume air dalam liter (setter memaksa `float`) |
| `_jenis_air` | `str` | `"tawar"` | Jenis air: `tawar` / `laut` |
| `_list_ikan_hias` | `list[IkanHias]` | `[]` | Penghuni akuarium (**Asosiasi**) |
| `_media_substrat` | `MediaSubstrat` | `None` | Substrat tunggal, dibuat & dimiliki (**Komposisi**) |

> `_media_substrat` diinisialisasi `None` dan hanya diisi lewat `set_media_substrat()`, yang
> sekaligus meng-*instansiasi* objek `MediaSubstrat` — inilah pol realization Komposisi.

### 4. `entitas_bisnis.py` — Entitas Usaha

#### `PeternakanIkanHias`

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_kode_peternakan` | `str` | `""` | Kode peternakan, mis. `PET-01` |
| `_nama` | `str` | `""` | Nama perusahaan peternakan |
| `_alamat` | `str` | `""` | Lokasi peternakan |
| `_tahun_berdiri` | `int` | `0` | Tahun operasional dimulai |
| `_list_ikan_hias` | `list[IkanHias]` | `[]` | Koleksi ikan berkualitas (**Agregasi**) |

#### `TokoAkuarium`

| Atribut | Tipe | Nilai Default | Keterangan |
|---|---|---|---|
| `_kode_toko` | `str` | `""` | Kode toko, mis. `TKO-01` |
| `_nama` | `str` | `""` | Nama toko |
| `_alamat` | `str` | `""` | Alamat toko |
| `_jenis_toko_akuarium` | `str` | `"offline"` | Kanal penjualan: `offline` / `online` |
| `_list_ikan_hias` | `list[IkanHias]` | `[]` | Ikan yang dijual (**Agregasi**) |
| `_list_media_substrat` | `list[MediaSubstrat]` | `[]` | Substrat yang dijual (**Agregasi**) |
| `_list_pakan_ikan` | `list[PakanIkanHias]` | `[]` | Stok pakan, dibuat internal (**Komposisi**) |

---

## Relasi Antar Kelas

| Relasi | Pasangan | Alasan |
|---|---|---|
| **Inheritance** | `PedagangIkanHias`, `KolektorIkanHias` → `Manusia` | Keduanya adalah manusia; atribut `no_ktp`, `nama`, `alamat` ditulis sekali di superclass. |
| **Inheritance** | `IkanHiasAirTawar`, `IkanHiasAirLaut` → `IkanHias` | Tawar maupun laut adalah ikan hias; kesamaan atribut dikelompokkan di superclass. |
| **Association** | `AkuariumDisplay` → `IkanHias` | Akuarium menampung ikan yang berenang di dalamnya — hubungan tempat tinggal/ekosistem. |
| **Aggregation** | `PeternakanIkanHias` → `IkanHias` | Peternakan mengelola koleksi ikan; data ikan tetap ada meski peternakan dihapus. |
| **Aggregation** | `PedagangIkanHias` → `IkanHias` | Pedagangresser mengelola dagangan; data ikan tidak ikut hilang. |
| **Aggregation** | `KolektorIkanHias` → `IkanHias` | Kolektor menyimpan ikan favorit independently. |
| **Aggregation** | `KolektorIkanHias` → `PedagangIkanHias` | Daftar pedagang langganan tidak ikut hilang bersama kolektor. |
| **Aggregation** | `KolektorIkanHias` → `AkuariumDisplay` | Unit akuarium display tetap eksis secara logika meski data kolektor dihapus. |
| **Composition** | `AkuariumDisplay` → `MediaSubstrat` | Substrat adalah komponen fisik yang menyatu pada akuarium; ikut terhapus bila akuarium dibongkar. |
| **Composition** | `TokoAkuarium` → `PakanIkanHias` | Pakan adalah inventaris resmi toko; ikut terhapus bila toko tutup. |

**Perbedaan kunci antara Agregasi dan Komposisi pada kode:**

```python
# AGREGASI -> objek anak dibuat di luar, lalu disalin ke list
peternakan.tambah_ikan_hias(ikan)          # ikan sudah ada sebelum relasi ini

# KOMPOSISI -> objek anak dibuat DI DALAM kelas induk
def set_media_substrat(self, kode_media, nama, jenis, ph, keterangan):
    self._media_substrat = MediaSubstrat(kode_media, nama, jenis, ph, keterangan)  # dibuat di dalam
```

---

## Alur Program

```
python Program/main.py
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 0. if __name__ == "__main__"  →  panggil main()                 │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 1. Cetak HEADER sistem (garis batas + judul)                     │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 2. HARDCODE DATA IKAN HIAS                                        │
│    4 objek: 2 IkanHiasAirTawar + 2 IkanHiasAirLaut              │
│    → disimpan pada list ikan_tawar[] dan ikan_laut[]             │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 3. HARDCODE DATA PETERNAKAN (Agregasi)                            │
│    2 objek PeternakanIkanHias                                    │
│    → PET-01 diberi 2 ikan tawar, PET-02 diberi 2 ikan laut       │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 4. HARDCODE DATA AKUARIUM (Komposisi + Asosiasi)                  │
│    2 objek AkuariumDisplay                                       │
│    → set_media_substrat() membuat objek MediaSubstrat sendiri     │
│    → tambah_ikan_hias() mengisi penghuni                          │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 5. HARDCODE DATA TOKO + PAKAN (Komposisi)                         │
│    2 objek TokoAkuarium                                          │
│    → tambah_pakan_ikan() membuat 4 objek PakanIkanHias            │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 6. HARDCODE DATA PEDAGANG & KOLEKTOR (Inheritance + Agregasi)     │
│    2 PedagangIkanHias + 2 KolektorIkanHias                       │
│    → diisi dagangan, favorit, langganan, dan akuarium display     │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│ 7. CETAK LAPORAN — 4 seksi                                       │
│    1) Data Ikan Hias (Air Tawar & Laut) → tabel format           │
│    2) Data Akuarium Display & Media Substrat (Komposisi)         │
│    3) Data Toko Akuarium & Stok Pakan (Komposisi)                │
│    4) Data Manusia (Pedagang & Kolektor)                          │
└───────────────────────────────────────────────────────────────────┘
        │
        ▼
   [ Program Selesai ]
```

> Semua data bersifat *hardcode* (tanpa basis data atau input pengguna) sesuai tujuan kuis:
> murni mendemonstrasikan struktur kelas dan relasi OOP. Pengambilan data selalu melalui
> **getter** (`get_*`), bukan akses langsung ke atribut privat.

---

## Dokumentasi

### Cara Menjalankan

Program hanya membutuhkan **Python 3** — tidak ada `requirements.txt` maupun dependensi
eksternal.

```bash
# Opsi 1: jalankan dari dalam folder Program
cd Program
python main.py

# Opsi 2: jalankan dari root repository
python Program/main.py
```

> **Catatan 1 — direktori kerja:** karena `main.py` melakukan `from ikan import ...` (import
> relatif tanpa package), eksekusi harus dijalankan dengan direktori kerja `Program/` —
> opsi 1 adalah cara yang paling aman.

> **Catatan 2 — Windows `UnicodeEncodeError`:** output memakai karakter garis dekoratif
> (`└─`) yang tidak tersedia di konsol `cp1252` bawaan Windows. Program akan berhenti
> dengan `UnicodeEncodeError` bila dijalankan lewat CMD/PowerShell tanpa pengaturan
> tambahan. Solusinya (pilih salah satu):
>
> ```bash
> # PowerShell
> $env:PYTHONIOENCODING="utf-8"; python main.py
>
> # CMD
> set PYTHONIOENCODING=utf-8 && python main.py
>
> # Alternatif permanen (Windows)
> chcp 65001
> ```
>
> Di Linux/macOS serta terminal modern program berjalan normal tanpa pengaturan ini.

### Contoh Output Lengkap

```text
================================================================================
                SISTEM MANAJEMEN PETERNAKAN & PERDAGANGAN IKAN HIAS
================================================================================

--- 1. DATA IKAN HIAS (AIR TAWAR & LAUT) ---
ID       Nama Ikan              Genus           Habitat    Warna Utama/Sekunder   Harga
------------------------------------------------------------------------------------------
IKT-01   Ikan Discus            Symphysodon     Air Tawar  Merah/Biru             Rp150,000
IKT-02   Ikan Louhan            Amphilophus     Air Tawar  Merah/Bintik Perak     Rp350,000
IKL-01   Clownfish (Nemo)       Amphiprion      Air Laut   Oranye/Putih           Rp75,000
IKL-02   Blue Tang (Dory)       Paracanthurus   Air Laut   Biru/Kuning            Rp200,000


--- 2. DATA AKUARIUM DISPLAY & MEDIA SUBSTRAT (KOMPOSISI) ---
[AKR-01] Aquascape Forest | Volume: 120.0L | Air: tawar
   └─ Substrat (Komposisi): Pasir Malang [pasir] - pH: 6.8
   └─ Penghuni: Ikan Discus
[AKR-02] Reef Tank Display | Volume: 250.0L | Air: laut
   └─ Substrat (Komposisi): Batu Karang Crushed [batu karang] - pH: 8.2
   └─ Penghuni: Clownfish (Nemo)
--------------------------------------------------------------------------------

--- 3. DATA TOKO AKUARIUM & STOK PAKAN (KOMPOSISI) ---
[TKO-01] Central Aquarium Store (offline) - Bandung
   Stok Pakan (Komposisi):
    * [FOD-01] Hikari Micro Pellets | Kandungan: Protein 45%, Vitamin C | Rp45,000
    * [FOD-02] Cacing Sutra Beku | Kandungan: Protein 50%, Fat 10% | Rp25,000
[TKO-02] AquaWorld Online (online) - Jakarta
   Stok Pakan (Komposisi):
    * [FOD-03] Ocean Nutrition Flakes | Kandungan: Omega 3, Protein 48% | Rp85,000
    * [FOD-04] TetraBits Complete | Kandungan: Carotenoid, Protein 47% | Rp60,000
--------------------------------------------------------------------------------

--- 4. DATA MANUSIA (PEDAGANG & KOLEKTOR IKAN HIAS) ---
[PEDAGANG]
KTP: 3273010101900001 | Nama: Budi Santoso | Jenis: distributor | Dagang Sejak: 2015
   -> Dijual: Ikan Discus (Rp150,000)
   -> Dijual: Clownfish (Nemo) (Rp75,000)
KTP: 3273010101900002 | Nama: Hendra Wijaya | Jenis: reseller | Dagang Sejak: 2019
   -> Dijual: Ikan Louhan (Rp350,000)

[KOLEKTOR]
KTP: 3171020202910001 | Nama: Dr. Ahmad | Alamat: Surabaya
   -> Ikan Favorit: Ikan Discus
   -> Langganan  : Budi Santoso
KTP: 3171020202910002 | Nama: Kevin Pratama | Alamat: Semarang
   -> Ikan Favorit: Blue Tang (Dory)
   -> Langganan  : Hendra Wijaya
```

### Ringkasan Data Simulasi

| Kategori | Jumlah Objek | Kode |
|---|---|---|
| Ikan hias air tawar | 2 | `IKT-01`, `IKT-02` |
| Ikan hias air laut | 2 | `IKL-01`, `IKL-02` |
| Peternakan | 2 | `PET-01`, `PET-02` |
| Akuarium display | 2 | `AKR-01`, `AKR-02` |
| Media substrat | 2 | `SUB-01`, `SUB-02` |
| Toko akuarium | 2 | `TKO-01`, `TKO-02` |
| Pakan ikan | 4 | `FOD-01` … `FOD-04` |
| Pedagang | 2 | — |
| Kolektor | 2 | — |
| **Total objek** | **18** | |

---

## Ringkasan API Kelas

| Kelas | Metode Utama |
|---|---|
| `IkanHias` | `get/set_id_ikan`, `get/set_nama`, `get/set_genus`, `get/set_warna_utama`, `get/set_warna_sekunder`, `get/set_status`, `get/set_harga_per_ekor` |
| `IkanHiasAirTawar`, `IkanHiasAirLaut` | mewarisi seluruh API `IkanHias` |
| `Manusia` | `get/set_no_ktp`, `get/set_nama`, `get/set_alamat` |
| `PedagangIkanHias` | mewarisi `Manusia` + `get/set_tahun_awal_dagang`, `get/set_jenis`, `get_list_ikan_hias`, `tambah_ikan_hias` |
| `KolektorIkanHias` | mewarisi `Manusia` + `get_list_ikan_favorit`/`tambah_ikan_favorit`, `get_list_pedagang_langganan`/`tambah_pedagang_langganan`, `get_list_akuarium_display`/`tambah_akuarium_display` |
| `MediaSubstrat` | `get/set_kode_media`, `get/set_nama`, `get/set_jenis`, `get/set_ph`, `get/set_keterangan` |
| `PakanIkanHias` | `get/set_kode_pakan`, `get/set_nama`, `get/set_jenis`, `get/set_kandungan`, `get/set_ukuran_butiran`, `get/set_harga_per_kemasan` |
| `AkuariumDisplay` | `get/set_kode_akuarium`, `get/set_nama`, `get/set_volume`, `get/set_jenis_air`, `get_list_ikan_hias`/`tambah_ikan_hias`, `get_media_substrat`/`set_media_substrat` |
| `PeternakanIkanHias` | `get/set_kode_peternakan`, `get/set_nama`, `get/set_alamat`, `get/set_tahun_berdiri`, `get_list_ikan_hias`/`tambah_ikan_hias` |
| `TokoAkuarium` | `get/set_kode_toko`, `get/set_nama`, `get/set_alamat`, `get/set_jenis_toko_akuarium`, `get/tambah_ikan_hias`, `get/tambah_media_substrat`, `get_list_pakan_ikan`/`tambah_pakan_ikan` |

### Catatan Desain

1. **Enkapsulasi penuh** — seluruh atribut privat, diakses hanya lewat `get_*`/`set_*`.
2. **Setter numerik** — `harga_per_ekor`, `ph`, `volume`, dan `harga_per_kemasan` melakukan
   konversi `float(val)` sehingga data konsisten meski diisi nilai numerik apa pun.
3. **Default value aman** — `kandungan` dan seluruh list diinisialisasi sebagai objek list
   baru (`[]`) per instance, mencegah mutable-default-argument pada tiap instance.
4. **Method komposisi** — `set_media_substrat()` dan `tambah_pakan_ikan()` menerima
   *atribut* (bukan objek), lalu meng-*instansiasi* kelas di dalamnya. Ini menjaga relasi
   Komposisi tetap terenkapsulasi di dalam kelas induk.
5. **Konsistensi nama** — `tambah_ikan_hias()` memakai nama yang sama di `AkuariumDisplay`,
   `PeternakanIkanHias`, `PedagangIkanHias`, dan `TokoAkuarium`, sehingga pemakaiannya
   seragam di seluruh program.

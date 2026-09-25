from peralatan import PakanIkanHias                                     # Import class PakanIkanHias

class PeternakanIkanHias:
    def __init__(self, kode_peternakan="", nama="", alamat="", tahun_berdiri=0):
        self._kode_peternakan = kode_peternakan                         # Inisialisasi atribut kode_peternakan
        self._nama = nama                                               # Inisialisasi atribut nama
        self._alamat = alamat                                           # Inisialisasi atribut alamat
        self._tahun_berdiri = tahun_berdiri                             # Inisialisasi atribut tahun_berdiri
        self._list_ikan_hias = []                                       # Daftar ikan budidaya (Agregasi)

    def get_kode_peternakan(self): return self._kode_peternakan         # Mengembalikan kode_peternakan
    def set_kode_peternakan(self, val): self._kode_peternakan = val     # Mengubah kode_peternakan

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_alamat(self): return self._alamat                           # Mengembalikan nilai alamat
    def set_alamat(self, val): self._alamat = val                       # Mengubah nilai alamat

    def get_tahun_berdiri(self): return self._tahun_berdiri             # Mengembalikan tahun_berdiri
    def set_tahun_berdiri(self, val): self._tahun_berdiri = val         # Mengubah tahun_berdiri

    def get_list_ikan_hias(self): return self._list_ikan_hias           # Mengembalikan daftar ikan hias
    def tambah_ikan_hias(self, ikan): self._list_ikan_hias.append(ikan) # Menambahkan ikan budidaya


class TokoAkuarium:
    def __init__(self, kode_toko="", nama="", alamat="", jenis_toko_akuarium="offline"):
        self._kode_toko = kode_toko                                     # Inisialisasi atribut kode_toko
        self._nama = nama                                               # Inisialisasi atribut nama
        self._alamat = alamat                                           # Inisialisasi atribut alamat
        self._jenis_toko_akuarium = jenis_toko_akuarium                 # Inisialisasi jenis_toko_akuarium
        self._list_ikan_hias = []                                       # Daftar ikan dijual (Agregasi)
        self._list_media_substrat = []                                  # Daftar substrat (Agregasi)
        self._list_pakan_ikan = []                                      # Daftar pakan ikan (Komposisi)

    def get_kode_toko(self): return self._kode_toko                     # Mengembalikan kode_toko
    def set_kode_toko(self, val): self._kode_toko = val                 # Mengubah kode_toko

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_alamat(self): return self._alamat                           # Mengembalikan nilai alamat
    def set_alamat(self, val): self._alamat = val                       # Mengubah nilai alamat

    def get_jenis_toko_akuarium(self): return self._jenis_toko_akuarium # Mengembalikan jenis_toko_akuarium
    def set_jenis_toko_akuarium(self, val): self._jenis_toko_akuarium = val # Mengubah jenis_toko_akuarium

    def get_list_ikan_hias(self): return self._list_ikan_hias           # Mengembalikan daftar ikan
    def tambah_ikan_hias(self, ikan): self._list_ikan_hias.append(ikan) # Menambahkan ikan hias

    def get_list_media_substrat(self): return self._list_media_substrat # Mengembalikan daftar substrat
    def tambah_media_substrat(self, substrat): self._list_media_substrat.append(substrat) # Menambah substrat

    def get_list_pakan_ikan(self): return self._list_pakan_ikan         # Mengembalikan daftar pakan

    def tambah_pakan_ikan(self, kode_pakan, nama, jenis, kandungan, ukuran_butiran, harga_per_kemasan):
        pakan = PakanIkanHias(kode_pakan, nama, jenis, kandungan, ukuran_butiran, harga_per_kemasan) # Instansiasi Komposisi
        self._list_pakan_ikan.append(pakan)                             # Menambahkan objek pakan ke list
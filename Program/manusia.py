class Manusia:
    def __init__(self, no_ktp="", nama="", alamat=""):
        self._no_ktp = no_ktp                                           # Inisialisasi atribut privat no_ktp
        self._nama = nama                                               # Inisialisasi atribut privat nama
        self._alamat = alamat                                           # Inisialisasi atribut privat alamat

    # Getter & Setter
    def get_no_ktp(self): return self._no_ktp                           # Mengembalikan nilai no_ktp
    def set_no_ktp(self, val): self._no_ktp = val                       # Mengubah nilai no_ktp

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_alamat(self): return self._alamat                           # Mengembalikan nilai alamat
    def set_alamat(self, val): self._alamat = val                       # Mengubah nilai alamat


class PedagangIkanHias(Manusia):
    def __init__(self, no_ktp="", nama="", alamat="", tahun_awal_dagang=0, jenis="reseller"):
        super().__init__(no_ktp, nama, alamat)                           # Memanggil konstruktor superclass Manusia
        self._tahun_awal_dagang = tahun_awal_dagang                     # Inisialisasi atribut tahun_awal_dagang
        self._jenis = jenis                                             # Inisialisasi atribut jenis pedagang
        self._list_ikan_hias = []                                       # Inisialisasi daftar ikan hias (Agregasi)

    def get_tahun_awal_dagang(self): return self._tahun_awal_dagang     # Mengembalikan tahun_awal_dagang
    def set_tahun_awal_dagang(self, val): self._tahun_awal_dagang = val # Mengubah tahun_awal_dagang

    def get_jenis(self): return self._jenis                             # Mengembalikan jenis pedagang
    def set_jenis(self, val): self._jenis = val                         # Mengubah jenis pedagang

    def get_list_ikan_hias(self): return self._list_ikan_hias           # Mengembalikan daftar ikan hias
    def tambah_ikan_hias(self, ikan): self._list_ikan_hias.append(ikan) # Menambahkan objek ikan hias ke daftar


class KolektorIkanHias(Manusia):
    def __init__(self, no_ktp="", nama="", alamat=""):
        super().__init__(no_ktp, nama, alamat)                          # Memanggil konstruktor superclass Manusia
        self._list_ikan_favorit = []                                    # Daftar ikan hias favorit (Agregasi)
        self._list_pedagang_langganan = []                              # Daftar pedagang langganan (Agregasi)
        self._list_akuarium_display = []                                # Daftar akuarium display (Agregasi)

    def get_list_ikan_favorit(self): return self._list_ikan_favorit                                 # Mengembalikan daftar ikan favorit
    def tambah_ikan_favorit(self, ikan): self._list_ikan_favorit.append(ikan)                       # Menambah ikan favorit

    def get_list_pedagang_langganan(self): return self._list_pedagang_langganan                     # Mengembalikan daftar pedagang
    def tambah_pedagang_langganan(self, pedagang): self._list_pedagang_langganan.append(pedagang)   # Menambah pedagang

    def get_list_akuarium_display(self): return self._list_akuarium_display                         # Mengembalikan daftar akuarium
    def tambah_akuarium_display(self, akuarium): self._list_akuarium_display.append(akuarium)       # Menambah akuarium
class MediaSubstrat:
    def __init__(self, kode_media="", nama="", jenis="pasir", ph=7.0, keterangan=""):
        self._kode_media = kode_media                                   # Inisialisasi atribut kode_media
        self._nama = nama                                               # Inisialisasi atribut nama
        self._jenis = jenis                                             # Inisialisasi atribut jenis
        self._ph = ph                                                   # Inisialisasi atribut pH
        self._keterangan = keterangan                                   # Inisialisasi atribut keterangan

    def get_kode_media(self): return self._kode_media                   # Mengembalikan nilai kode_media
    def set_kode_media(self, val): self._kode_media = val               # Mengubah nilai kode_media

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_jenis(self): return self._jenis                             # Mengembalikan nilai jenis
    def set_jenis(self, val): self._jenis = val                         # Mengubah nilai jenis

    def get_ph(self): return self._ph                                   # Mengembalikan nilai pH
    def set_ph(self, val): self._ph = float(val)                        # Mengubah nilai pH

    def get_keterangan(self): return self._keterangan                   # Mengembalikan nilai keterangan
    def set_keterangan(self, val): self._keterangan = val               # Mengubah nilai keterangan


class PakanIkanHias:
    def __init__(self, kode_pakan="", nama="", jenis="buatan", kandungan=None, ukuran_butiran="small", harga_per_kemasan=0.0):
        self._kode_pakan = kode_pakan                                   # Inisialisasi atribut kode_pakan
        self._nama = nama                                               # Inisialisasi atribut nama
        self._jenis = jenis                                             # Inisialisasi atribut jenis
        self._kandungan = kandungan if kandungan is not None else []    # Inisialisasi list kandungan nutrisi
        self._ukuran_butiran = ukuran_butiran                           # Inisialisasi atribut ukuran_butiran
        self._harga_per_kemasan = harga_per_kemasan                     # Inisialisasi atribut harga_per_kemasan

    def get_kode_pakan(self): return self._kode_pakan                   # Mengembalikan nilai kode_pakan
    def set_kode_pakan(self, val): self._kode_pakan = val               # Mengubah nilai kode_pakan

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_jenis(self): return self._jenis                             # Mengembalikan nilai jenis
    def set_jenis(self, val): self._jenis = val                         # Mengubah nilai jenis

    def get_kandungan(self): return self._kandungan                     # Mengembalikan list kandungan
    def set_kandungan(self, val): self._kandungan = val                 # Mengubah list kandungan

    def get_ukuran_butiran(self): return self._ukuran_butiran           # Mengembalikan ukuran_butiran
    def set_ukuran_butiran(self, val): self._ukuran_butiran = val       # Mengubah ukuran_butiran

    def get_harga_per_kemasan(self): return self._harga_per_kemasan     # Mengembalikan harga_per_kemasan
    def set_harga_per_kemasan(self, val): self._harga_per_kemasan = float(val) # Mengubah harga_per_kemasan


class AkuariumDisplay:
    def __init__(self, kode_akuarium="", nama="", volume=0.0, jenis_air="tawar"):
        self._kode_akuarium = kode_akuarium                             # Inisialisasi atribut kode_akuarium
        self._nama = nama                                               # Inisialisasi atribut nama
        self._volume = volume                                           # Inisialisasi atribut volume
        self._jenis_air = jenis_air                                     # Inisialisasi atribut jenis_air
        self._list_ikan_hias = []                                       # Daftar ikan hias (Asosiasi)
        self._media_substrat = None                                     # Media substrat tunggal (Komposisi)

    def get_kode_akuarium(self): return self._kode_akuarium             # Mengembalikan kode_akuarium
    def set_kode_akuarium(self, val): self._kode_akuarium = val         # Mengubah kode_akuarium

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_volume(self): return self._volume                           # Mengembalikan nilai volume
    def set_volume(self, val): self._volume = float(val)                # Mengubah nilai volume

    def get_jenis_air(self): return self._jenis_air                     # Mengembalikan jenis_air
    def set_jenis_air(self, val): self._jenis_air = val                 # Mengubah jenis_air

    def get_list_ikan_hias(self): return self._list_ikan_hias           # Mengembalikan daftar ikan hias
    def tambah_ikan_hias(self, ikan): self._list_ikan_hias.append(ikan) # Menambahkan ikan ke akuarium

    def get_media_substrat(self): return self._media_substrat           # Mengembalikan objek media_substrat

    def set_media_substrat(self, kode_media, nama, jenis, ph, keterangan):
        self._media_substrat = MediaSubstrat(kode_media, nama, jenis, ph, keterangan) # Instansiasi Komposisi
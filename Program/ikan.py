class IkanHias:
    def __init__(self, id_ikan="", nama="", genus="", warna_utama="", warna_sekunder="", status="spesies", harga_per_ekor=0.0):
        self._id_ikan = id_ikan                                         # Inisialisasi atribut privat id_ikan
        self._nama = nama                                               # Inisialisasi atribut privat nama
        self._genus = genus                                             # Inisialisasi atribut privat genus
        self._warna_utama = warna_utama                                 # Inisialisasi atribut privat warna_utama
        self._warna_sekunder = warna_sekunder                           # Inisialisasi atribut privat warna_sekunder
        self._status = status                                           # Inisialisasi atribut privat status
        self._harga_per_ekor = harga_per_ekor                           # Inisialisasi atribut harga_per_ekor

    # Getter & Setter
    def get_id_ikan(self): return self._id_ikan                         # Mengembalikan nilai id_ikan
    def set_id_ikan(self, val): self._id_ikan = val                     # Mengubah nilai id_ikan

    def get_nama(self): return self._nama                               # Mengembalikan nilai nama
    def set_nama(self, val): self._nama = val                           # Mengubah nilai nama

    def get_genus(self): return self._genus                             # Mengembalikan nilai genus
    def set_genus(self, val): self._genus = val                         # Mengubah nilai genus

    def get_warna_utama(self): return self._warna_utama                 # Mengembalikan nilai warna_utama
    def set_warna_utama(self, val): self._warna_utama = val             # Mengubah nilai warna_utama

    def get_warna_sekunder(self): return self._warna_sekunder           # Mengembalikan nilai warna_sekunder
    def set_warna_sekunder(self, val): self._warna_sekunder = val       # Mengubah nilai warna_sekunder

    def get_status(self): return self._status                           # Mengembalikan nilai status
    def set_status(self, val): self._status = val                       # Mengubah nilai status

    def get_harga_per_ekor(self): return self._harga_per_ekor           # Mengembalikan nilai harga_per_ekor
    def set_harga_per_ekor(self, val): self._harga_per_ekor = float(val)# Mengubah nilai harga_per_ekor


class IkanHiasAirTawar(IkanHias):
    def __init__(self, id_ikan="", nama="", genus="", warna_utama="", warna_sekunder="", status="spesies", harga_per_ekor=0.0):
        super().__init__(id_ikan, nama, genus, warna_utama, warna_sekunder, status, harga_per_ekor) # Konstruktor IkanHias


class IkanHiasAirLaut(IkanHias):
    def __init__(self, id_ikan="", nama="", genus="", warna_utama="", warna_sekunder="", status="spesies", harga_per_ekor=0.0):
        super().__init__(id_ikan, nama, genus, warna_utama, warna_sekunder, status, harga_per_ekor) # Konstruktor IkanHias
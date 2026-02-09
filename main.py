import random
import time

class MysteryAdventureBot:
    def __init__(self):
        self.nama = ""
        self.stamina = 100
        self.posisi = "Pintu Masuk Hutan"
        self.clues_terkumpul = []
        self.health = 100
        self.resep_ditemukan = False
        
    def tampilkan_status(self):
        """Menampilkan status pemain"""
        print(f"\n{'='*50}")
        print(f"Nama: {self.nama}")
        print(f"Lokasi: {self.posisi}")
        print(f"Stamina: {self.stamina}% {'█' * (self.stamina//10)} {['░' * (10-self.stamina//10)]}")
        print(f"Nyawa: {self.health}%")
        print(f"Clue Terkumpul: {len(self.clues_terkumpul)}/4")
        print(f"{'='*50}\n")
    
    def pengenalan(self):
        """Intro game"""
        print("\n" + "="*60)
        print("╔════════════════════════════════════════════════════════╗")
        print("║       MYSTERY ADVENTURE BOT: RESEP RAHASIA HUTAN      ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("="*60)
        print("\nSuatu hari, kamu menemukan peta tua yang menunjukkan")
        print("lokasi harta karun luar biasa di dalam hutan belantara:")
        print("RESEP MAKANAN TERNIKMAT DI SELURUH DUNIA!")
        print("\nResep ini konon katanya milik seorang master chef legendaris")
        print("yang hilang bertahun-tahun lalu. Perjalananmu dimulai sekarang...")
        print("="*60 + "\n")
        
        self.nama = input("Siapa nama petualangmu? ").strip()
        if not self.nama:
            self.nama = "Pemberani"
        
        print(f"\nSalam, {self.nama}! Mari kita mulai petualangan ini!\n")
        time.sleep(2)

    def lokasi_pintu_masuk(self):
        """Lokasi pertama - Pintu Masuk Hutan"""
        self.posisi = "Pintu Masuk Hutan"
        print("\n" + "="*50)
        print("📍 PINTU MASUK HUTAN")
        print("="*50)
        print("Kamu berdiri di depan hutan yang gelap dan misterius.")
        print("Pohon-pohon besar melingkupi area ini dengan akar yang")
        print("melilit di tanah. Udara terasa lembab dan penuh misteri.")
        print("\nDi samping pohon tua, kamu melihat sebuah papan kayu:")
        print('"Selamat datang, pencari resep... Jawabu teka-teki untuk')
        print('mendapat petunjuk pertama:\n')
        print("TEKA-TEKI: Aku memiliki tangan tapi tidak bisa menepuk,")
        print("           Aku bergerak tapi tidak memiliki kaki.")
        print('           Makanan yang aku masak selalu hangat. Siapa aku?"')
        print("\n(A) Jam dinding  (B) Jam tangan  (C) Panci masak  (D) Ombak\n")
        
        return self.tanya_jawab_pertama()

    def tanya_jawab_pertama(self):
        """Puzzle pertama"""
        jawaban_benar = "C"
        while True:
            jawab = input("Jawaban mu (A/B/C/D): ").strip().upper()
            if jawab in ['A', 'B', 'C', 'D']:
                if jawab == jawaban_benar:
                    print("\n✓ BENAR! Papan kayu bersinar dan kamu membaca:")
                    print('"Selamat! Petunjuk pertama: Cari POHON KEMBAR BESAR')
                    print('di arah UTARA hutan. Di sana ada clue menunggu!"')
                    self.clues_terkumpul.append("Pohon Kembar Besar")
                    print("\n🗝️ CLUE 1 DITEMUKAN!\n")
                    return True
                else:
                    print("\n✗ Jawaban salah! Coba lagi...")
                    if jawab == "D":
                        print("Petunjuk: Ombak? Itu di laut, bukan di dapur!")
            else:
                print("Input tidak valid! Gunakan A, B, C, atau D")

    def lokasi_pohon_kembar(self):
        """Lokasi kedua - Pohon Kembar Besar"""
        self.posisi = "Pohon Kembar Besar"
        self.stamina -= 10
        print("\n" + "="*50)
        print("📍 POHON KEMBAR BESAR")
        print("="*50)
        print("Kamu berjalan ke arah utara melalui semak-semak yang lebat.")
        print("Setelah beberapa menit, kamu menemukan dua pohon raksasa")
        print("yang tumbuh berdampingan, cabang-cabangnya saling berkaitan.")
        print("\nTiba-tiba... GROARRR!!!")
        print("\n⚠️  SERANGAN HEWAN BUAS! 🐻")
        print("Seekor BERUANG BESAR muncul dari balik semak!")
        print("Beruang itu langsung mengejarmu! Kamu harus cepat!\n")
        
        return self.mekanisme_serangan_hewan()

    def mekanisme_serangan_hewan(self):
        """Mekanik serangan hewan"""
        while True:
            print("Apa yang akan kamu lakukan?")
            print("(1) BERLARI dengan cepat  (2) Bersembunyi di balik pohon\n")
            pilihan = input("Pilihan (1 atau 2): ").strip()
            
            if pilihan == "1":
                print("\n🏃‍♂️ Kamu berlari sekencang-kencangnya!")
                self.stamina -= 25
                print(f"Stamina berkurang 25%! Sekarang: {self.stamina}%")
                
                if self.stamina < 0:
                    self.stamina = 0
                    print("\n☠️  KAMU TERLALU LELAH! Beruang mengejarmu!")
                    self.health -= 50
                    print(f"Beruang mencengkerammu! Nyawa berkurang! ({self.health}%)")
                    if self.health <= 0:
                        return False
                else:
                    print("Kamu berhasil melarikan diri! Beruang itu tertinggal.")
                    break
            
            elif pilihan == "2":
                print("\n🫨 Kamu bersembunyi dengan diam-diam di balik pohon besar!")
                print("Beruang itu mencium-cium area disekitarmu...")
                print("Jantungmu berdebar-debar... tapi kamu tetap diam...")
                time.sleep(2)
                print("\nBeruang itu kehilangan jejakmu dan pergi mencari mangsanya.")
                print("Kamu berhasil selamat tanpa kehilangan stamina!")
                break
            else:
                print("Input tidak valid!")
        
        print("\n💙 Setelah beberapa saat, kamu keluar dari persembunyian.")
        print("Ternyata... ada catatan di pohon kembar itu!")
        print('"Bagus sekali! Kamu sudah lolos dari Beruang.\n')
        print("TEKA-TEKI KEDUA:\n")
        print("Aku dibuat dari biji-bijian dan dedak,")
        print("Banyak orang suka makan aku saat pagi hari.")
        print("Sebagian dari kami goreng sampai cokelat. Kami siapa?"')
        print("\n(A) Sereal  (B) Roti  (C) Pasta  (D) Kue\n")
        
        return self.tanya_jawab_kedua()

    def tanya_jawab_kedua(self):
        """Puzzle kedua"""
        jawaban_benar = "A"
        while True:
            jawab = input("Jawaban mu (A/B/C/D): ").strip().upper()
            if jawab in ['A', 'B', 'C', 'D']:
                if jawab == jawaban_benar:
                    print("\n✓ BENAR! Catatan bersinar dan terungkap pesan baru:")
                    print('"Pintar! Petunjuk kedua: Cari SUNGAI BERBATU DI TIMUR')
                    print('di sana ada clue tertanam di bawah batu besar!"')
                    self.clues_terkumpul.append("Sungai Berbatu")
                    print("\n🗝️ CLUE 2 DITEMUKAN!\n")
                    return True
                else:
                    print("\n✗ Jawaban salah! Coba lagi...")
                    if jawab == "B":
                        print("Petunjuk: Roti? Tidak dibuat dari dedak saja...")
            else:
                print("Input tidak valid!")

    def lokasi_sungai_berbatu(self):
        """Lokasi ketiga - Sungai Berbatu"""
        self.posisi = "Sungai Berbatu"
        self.stamina -= 15
        print("\n" + "="*50)
        print("📍 SUNGAI BERBATU")
        print("="*50)
        print("Kamu berjalan ke arah timur dan menemukan sebuah sungai")
        print("yang mengalir deras dengan batu-batu besar yang menghiasi")
        print("alur air. Suara air yang mengalir sangat menenangkan.\n")
        print("Di tengah sungai, kamu melihat batu besar yang mengkilap.")
        print("Kamu melompati batu-batu untuk sampai ke tengah sungai.")
        
        print("\nTiba-tiba... PSSSSTT!!! HISSSS!!!")
        print("\n⚠️  SERANGAN HEWAN BUAS! 🐍")
        print("Sepasang ULAR PITON RAKSASA muncul dari semak sungai!")
        print("Pertahanannya tidak lama lagi! Harus segera bertindak!\n")
        
        return self.mekanisme_serangan_ular()

    def mekanisme_serangan_ular(self):
        """Mekanik serangan ular"""
        while True:
            print("Apa yang akan kamu lakukan?")
            print("(1) BERLARI dari area ini  (2) Bersembunyi di bawah air")
            print("(3) Melempar batu ke arah ular\n")
            pilihan = input("Pilihan (1/2/3): ").strip()
            
            if pilihan == "1":
                print("\n🏃‍♂️ Kamu berlari meninggalkan sungai!")
                self.stamina -= 20
                print(f"Stamina berkurang 20%! Sekarang: {self.stamina}%")
                if self.stamina < 0:
                    self.stamina = 0
                    print("\nUlar itu mengejarmu dan mengigit!")
                    self.health -= 40
                    print(f"Venom ular! Nyawa berkurang! ({self.health}%)")
                    if self.health <= 0:
                        return False
                else:
                    print("Kamu berhasil lolos dengan selamat!")
                    break
                    
            elif pilihan == "2":
                print("\n💧 Kamu menyelam di bawah air dengan cepat!")
                print("Ular tidak bisa mengejarmu di bawah sana.")
                print("Kamu tetap diam sampai ular pergi.")
                print("Mirip tapi sangat berbahaya!")
                time.sleep(2)
                print("Setelah beberapa saat, kamu naik ke permukaan.")
                print("Ularnya sudah hilang!")
                break
                
            elif pilihan == "3":
                print("\n🪨 Kamu mengambil batu dan melemparnya ke arah ular!")
                print("Ular itu terkejut dan bergerak pergi!")
                print("Strategi sederhana tapi efektif!")
                break
            else:
                print("Input tidak valid!")
        
        print("\n💙 Kamu kembali ke batu besar di tengah sungai.")
        print("Karena batu itu mengkilap, kamu gerakkan sedikit...")
        print("BRAK! Batunya terbuka dan menunjukkan kotak besi tua!\n")
        print("Kamu buka kotak itu dan menemukan catatan:\n")
        print('"Hebat! Kamu berhasil mengatasi dua rintangan.\n')
        print("TEKA-TEKI KETIGA:\n")
        print("Aku kuning dan premium, orang bayar mahal untuk aku.")
        print("Aku berasal dari bunga dan dibuat oleh serangga kecil.")
        print('Rasa manismu sempurna untuk masakan apapun. Siapa aku?"')
        print("\n(A) Gula pasir  (B) Madu  (C) Sirup jagung  (D) Aspartame\n")
        
        return self.tanya_jawab_ketiga()

    def tanya_jawab_ketiga(self):
        """Puzzle ketiga"""
        jawaban_benar = "B"
        while True:
            jawab = input("Jawaban mu (A/B/C/D): ").strip().upper()
            if jawab in ['A', 'B', 'C', 'D']:
                if jawab == jawaban_benar:
                    print("\n✓ BENAR! Kotak itu bersinar terang!")
                    print('"Sempurna! Petunjuk ketiga: Cari GUNDUKAN BERBATU BARAT')
                    print('di sana tersembunyi petunjuk akhir!"')
                    self.clues_terkumpul.append("Gundukan Berbatu")
                    print("\n🗝️ CLUE 3 DITEMUKAN!\n")
                    return True
                else:
                    print("\n✗ Jawaban salah! Coba lagi...")
                    if jawab == "A":
                        print("Petunjuk: Gula pasir dibuat dari tebu, bukan bunga!")
            else:
                print("Input tidak valid!")

    def lokasi_gundukan_berbatu(self):
        """Lokasi keempat - Gundukan Berbatu"""
        self.posisi = "Gundukan Berbatu"
        self.stamina -= 12
        print("\n" + "="*50)
        print("📍 GUNDUKAN BERBATU BARAT")
        print("="*50)
        print("Kamu berjalan ke arah barat melalui hutan yang semakin lebat.")
        print("Akhirnya, kamu menemukan gundukan batu yang aneh,")
        print("berbentuk seperti pyramid miniatur. Sangat unik dan misterius.\n")
        print("Kamu mulai menggali-gali batu itu, mencari sesuatu...")
        
        print("\nHUUUU! ROAAARRR!!!")
        print("\n⚠️  SERANGAN HEWAN BUAS! 🐅")
        print("Seekor MACAN TUTUL BESAR muncul dari balik pohon!")
        print("Matanya menatapmu dengan tajam dan lapar!\n")
        
        return self.mekanisme_serangan_macan()

    def mekanisme_serangan_macan(self):
        """Mekanik serangan macan"""
        while True:
            print("Apa yang akan kamu lakukan?")
            print("(1) BERLARI ke arah terdekat  (2) Bersembunyi di balik batu")
            print("(3) Menggunakan taktik distraksi\n")
            pilihan = input("Pilihan (1/2/3): ").strip()
            
            if pilihan == "1":
                print("\n🏃‍♂️ Kamu berlari dengan sekuat tenaga!")
                self.stamina -= 30
                print(f"Stamina berkurang 30%! Sekarang: {self.stamina}%")
                if self.stamina < 0:
                    self.stamina = 0
                    print("\nMacan yang cepat mengejarmu dan menggoresku!")
                    self.health -= 60
                    print(f"Cakarnya sangat tajam! Nyawa berkurang! ({self.health}%)")
                    if self.health <= 0:
                        return False
                else:
                    print("Macan tidak bisa menangkapmu!")
                    break
                    
            elif pilihan == "2":
                print("\n🪨 Kamu cepat bersembunyi di balik batu besar!")
                print("Macan itu mencium-cium tempat persembunyianmu...")
                print("Tapi batunya terlalu besar untuk dilompati...")
                time.sleep(2)
                print("Macan itu pergi mencari mangsa lain.")
                print("Kamu selamat tanpa kehilangan banyak stamina!")
                break
                
            elif pilihan == "3":
                print("\n💡 Kamu mengambil batu dan melemparkannya jauh!")
                print("Macan itu terdistraksi dan mengejar batu itu!")
                print("Saat itu, kamu bisa lolos dengan aman!")
                break
            else:
                print("Input tidak valid!")
        
        print("\n💙 Setelah macan itu hilang, kamu lanjut menggali.")
        print("Dan TADA! Kamu menemukan sebuah peti emas tua!\n")
        print("Peti itu berisi catatan terakhir:\n")
        print('"Luar biasa! Kamu sudah mengatasi semua rintangan!!\n')
        print("TEKA-TEKI TERAKHIR (FINAL):\n")
        print("Aku raja bumbu, aku hangat dan pedas,")
        print("Orang gunakan aku untuk segala masakan tradisional.")
        print("Dari batang/umbi aku diambil dan dibuat bubuk. Siapa aku?"')
        print("\n(A) Lada hitam  (B) Kunyit  (C) Merica  (D) Paprika\n")
        
        return self.tanya_jawab_final()

    def tanya_jawab_final(self):
        """Puzzle final"""
        jawaban_benar = "B"
        while True:
            jawab = input("Jawaban mu (A/B/C/D): ").strip().upper()
            if jawab in ['A', 'B', 'C', 'D']:
                if jawab == jawaban_benar:
                    print("\n" + "="*50)
                    print("✓ BENAR! PETI EMAS BERSINAR SANGAT TERANG!")
                    print("="*50)
                    print("\nPeti terbuka dengan sempurna...")
                    print("Di dalamnya ada sebuah gulungan kertas berumur ratusan tahun!")
                    print("\nDengan tangan yang bergetar, kamu membukanya perlahan...")
                    print("\n🌟 RESEP RAHASIA TERUNGKAP! 🌟\n")
                    
                    print("RESEP \"MAKANAN MASTER CHEF LEGENDARIS\"")
                    print("-" * 50)
                    print("BAHAN UTAMA:")
                    print("• 500g daging premium dipilih dengan hati-hati")
                    print("• 2 sendok makan madu alami dari lebah hutan")
                    print("• 3 sendok teh kunyit terbaik yang digiling halus")
                    print("• 100ml minyak zaitun kualitas tinggi")
                    print("• Garam dan merica secukupnya")
                    print("• 5 cengkeh, 3 buah cinnamon untuk aroma")
                    print("• Kemangi segar dari kebun pribadi\n")
                    
                    print("CARA MEMASAK:")
                    print("1. Potong daging menjadi potongan sempurna")
                    print("2. Lumuri dengan madu dan kunyit, biarkan 30 menit")
                    print("3. Panaskan minyak zaitun hingga berasap tipis")
                    print("4. Goreng daging dengan api sedang-besar")
                    print("5. Tambahkan bumbu cengkeh dan cinnamon")
                    print("6. Masak hingga daging empuk (±45 menit)")
                    print("7. Tambahkan kemangi di akhir\n")
                    print("RAHASIA SPESIAL: Masak dengan penuh kasih sayang")
                    print("maka makanan akan terasa lebih nikmat!\n")
                    
                    print("-" * 50)
                    self.clues_terkumpul.append("Resep Rahasia")
                    self.resep_ditemukan = True
                    print("\n🗝️ CLUE 4 DAN RESEP TERAKHIR DITEMUKAN!\n")
                    return True
                else:
                    print("\n✗ Jawaban salah! Coba lagi...")
                    if jawab == "C":
                        print("Petunjuk: Merica sama saja dengan lada hitam!")
            else:
                print("Input tidak valid!")

    def memasak_makanan(self):
        """Mini-game memasak"""
        print("\n" + "="*50)
        print("🍳 SAATNYA MEMASAK MAKANAN RAHASIA!")
        print("="*50)
        
        print(f"\nKamu kembali ke rumah dengan resep di genggaman.")
        print(f"Sekarang saatnya untuk memasak makanan legendaris itu!\n")
        
        bahan_dipilih = []
        bahan_tersedia = [
            ("Daging premium", "Bahan utama yang sempurna"),
            ("Madu alami", "Memberikan rasa manis alami"),
            ("Kunyit halus", "Bumbu emas untuk masakan"),
            ("Minyak zaitun", "Untuk menggoreng dengan sempurna"),
            ("Cengkeh dan cinnamon", "Aroma yang menggugah selera"),
            ("Kemangi segar", "Untuk aroma akhir yang sempurna")
        ]
        
        print("TAHAP MEMASAK - Pilih bahan dalam urutan yang benar:\n")
        
        for i, (bahan, deskripsi) in enumerate(bahan_tersedia, 1):
            print(f"{i}. {bahan} - {deskripsi}")
        
        print("\nUrutannya adalah: Daging → Madu & Kunyit → Minyak → Bumbu → Kemangi")
        print("Masukkan nomor urutan sesuai instruksi di atas!\n")
        
        urutan_benar = [1, 2, 3, 4, 5, 6]
        langkah = 0
        
        while langkah < len(urutan_benar):
            prompt = f"Langkah {langkah + 1}: Pilih bahan (1-6): "
            pilihan = input(prompt).strip()
            
            try:
                nomor = int(pilihan)
                if nomor in urutan_benar:
                    if nomor == urutan_benar[langkah]:
                        bahan, deskripsi = bahan_tersedia[nomor - 1]
                        print(f"✓ {bahan} ditambahkan dengan sempurna!")
                        bahan_dipilih.append(bahan)
                        langkah += 1
                    else:
                        print(f"✗ Urutan salah! Coba bahan yang sesuai urutan.")
                else:
                    print("Bahan tidak valid!")
            except ValueError:
                print("Input harus berupa nomor!")
        
        print("\n" + "="*50)
        print("🎉 MAKANAN BERHASIL DIMASAK!")
        print("="*50)
        print("\nAromatisnya wangi ke seluruh dapur...")
        print("Warna kecokelatan yang sempurna menarik perhatian...")
        print("Teksturnya lembut tapi tidak remuk...")
        print("\nInilah... MAKANAN MASTER CHEF LEGENDARIS!")
        print("\nTada... sempurna! Benar-benar layak disebut harta karun!")

    def ending(self):
        """Ending game"""
        print("\n" + "="*60)
        print("╔════════════════════════════════════════════════════════╗")
        print("║                    🎊 SELAMAT! 🎊                     ║")
        print("║                                                        ║")
        print(f"║  Petualangan luar biasa milikmu telah mencapai puncak! ║")
        print("║                                                        ║")
        print(f"║  {self.nama}, kamu adalah PEMENANG SEJATI!              ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("="*60)
        
        print("\n📊 STATISTIK AKHIR:")
        print(f"  • Clue yang dikumpulkan: {len(self.clues_terkumpul)}/4")
        print(f"  • Stamina sisa: {self.stamina}%")
        print(f"  • Nyawa sisa: {self.health}%")
        
        print(f"\n💌 KISAH SINGKAT:")
        print(f"  {self.nama} memulai perjalanan dengan keberanian penuh.")
        print(f"  Menghadapi beruang, ular, dan macan dengan strategi cemerlang.")
        print(f"  Memecahkan semua teka-teki dan menemukan resep legendaris.")
        print(f"  Berhasil memasak makanan istimewa yang akan dikenang selamanya.")
        
        print("\n🏆 PENGHARGAAN SPESIAL:")
        print("  ✦ Master Petualang Hutan")
        print("  ✦ Pemecah Teka-Teki Cerdas")
        print("  ✦ Pemberani Menghadapi Hewan Buas")
        print("  ✦ Chef Legendaris Sejati")
        
        print("\n" + "="*60)
        print("Terima kasih telah memainkan MYSTERY ADVENTURE BOT!")
        print("Semoga petualanganmu penuh kenangan indah!")
        print("="*60 + "\n")

    def jalankan_game(self):
        """Fungsi utama untuk menjalankan game"""
        self.pengenalan()
        
        # Lokasi 1
        self.tampilkan_status()
        if not self.lokasi_pintu_masuk():
            self.game_over()
            return
        
        # Lokasi 2
        input("\nTekan ENTER untuk lanjut ke lokasi berikutnya...")
        self.tampilkan_status()
        if not self.lokasi_pohon_kembar():
            self.game_over()
            return
        
        # Lokasi 3
        input("\nTekan ENTER untuk lanjut ke lokasi berikutnya...")
        self.tampilkan_status()
        if not self.lokasi_sungai_berbatu():
            self.game_over()
            return
        
        # Lokasi 4
        input("\nTekan ENTER untuk lanjut ke lokasi berikutnya...")
        self.tampilkan_status()
        if not self.lokasi_gundukan_berbatu():
            self.game_over()
            return
        
        # Memasak
        input("\nTekan ENTER untuk mulai memasak...")
        self.tampilkan_status()
        self.memasak_makanan()
        
        # Ending
        input("\nTekan ENTER untuk melihat ending...")
        self.ending()

    def game_over(self):
        """Game Over screen"""
        print("\n" + "="*60)
        print("╔════════════════════════════════════════════════════════╗")
        print("║                      GAME OVER                        ║")
        print("║                                                        ║")
        print("║  Petualanganmu harus berakhir di sini, sayang...       ║")
        print("║                                                        ║")
        print("║  Tapi tidak apa-apa, kamu bisa coba lagi!              ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("="*60)
        print(f"\nStamina: {self.stamina}%")
        print(f"Nyawa: {self.health}%")
        print("Clue terkumpul: " + ", ".join(self.clues_terkumpul) if self.clues_terkumpul else "Tidak ada")
        print("\n" + "="*60 + "\n")

def main():
    """Fungsi main"""
    while True:
        game = MysteryAdventureBot()
        game.jalankan_game()
        
        lagi = input("\nMain lagi? (Ya/Tidak): ").strip().lower()
        if lagi != "ya" and lagi != "y":
            print("\nTerima kasih telah bermain! Sampai jumpa lagi! 👋\n")
            break

if __name__ == "__main__":
    main()

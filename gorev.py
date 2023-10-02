# gorev_yoneticisi.py

class GorevYoneticisi:
    def __init__(self):
        self.gorevler = []

    def gorev_ekle(self, gorev, son_tarih):
        self.gorevler.append({"gorev": gorev, "son_tarih": son_tarih})

    def gorev_sil(self, index):
        if index >= 0 and index < len(self.gorevler):
            del self.gorevler[index]

    def gorevleri_goruntule(self):
        if not self.gorevler:
            print("Görev yok.")
        else:
            print("Görevler:")
            for i, gorev in enumerate(self.gorevler, start=1):
                print(f"{i}. Görev: {gorev['gorev']}, Son Tarih: {gorev['son_tarih']}")

def main():
    gorev_yoneticisi = GorevYoneticisi()

    while True:
        print("\nGörev Yöneticisi Uygulaması")
        print("1. Görev Ekle")
        print("2. Görev Sil")
        print("3. Görevleri Görüntüle")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            gorev = input("Eklemek istediğiniz görevi girin: ")
            son_tarih = input("Son tarih (gg/aa/yyyy) girin: ")
            gorev_yoneticisi.gorev_ekle(gorev, son_tarih)
            print("Görev eklendi.")
        elif secim == "2":
            index = int(input("Silmek istediğiniz görevin numarasını girin: ")) - 1
            gorev_yoneticisi.gorev_sil(index)
            print("Görev silindi.")
        elif secim == "3":
            gorev_yoneticisi.gorevleri_goruntule()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

# not_defteri.py

class NotDefteri:
    def __init__(self):
        self.notlar = {}

    def not_ekle(self, baslik, icerik):
        self.notlar[baslik] = icerik

    def not_sil(self, baslik):
        if baslik in self.notlar:
            del self.notlar[baslik]

    def not_goruntule(self):
        if not self.notlar:
            print("Not defteri boş.")
        else:
            print("Notlar:")
            for baslik, icerik in self.notlar.items():
                print(f"{baslik}: {icerik}")

def main():
    not_defteri = NotDefteri()

    while True:
        print("\nNot Defteri Uygulaması")
        print("1. Not Ekle")
        print("2. Not Sil")
        print("3. Notları Görüntüle")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            baslik = input("Not başlığını girin: ")
            icerik = input("Not içeriğini girin: ")
            not_defteri.not_ekle(baslik, icerik)
            print("Not eklendi.")
        elif secim == "2":
            baslik = input("Silmek istediğiniz notun başlığını girin: ")
            not_defteri.not_sil(baslik)
            print("Not silindi.")
        elif secim == "3":
            not_defteri.not_goruntule()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

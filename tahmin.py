# kelime_tahmin_oyunu.py
import random

kelimeler = ["elma", "armut", "çilek", "muz", "portakal", "karpuz", "kiraz"]

def kelime_sec():
    return random.choice(kelimeler)

def kelime_tahmin_oyunu():
    kelime = kelime_sec()
    tahmin_edilen = ["_" for _ in kelime]
    tahminler = []
    hak = 6

    print("Kelime Tahmin Oyununa Hoş Geldiniz!")

    while hak > 0:
        print(" ".join(tahmin_edilen))
        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Geçersiz tahmin. Lütfen bir harf girin.")
            continue

        if tahmin in tahminler:
            print("Bu harfi daha önce tahmin ettiniz.")
            continue

        tahminler.append(tahmin)

        if tahmin in kelime:
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            hak -= 1
            print(f"Yanlış tahmin. {hak} hakkınız kaldı.")

        if "_" not in tahmin_edilen:
            print("Tebrikler, kelimeyi buldunuz!")
            break

    if "_" in tahmin_edilen:
        print(f"Maalesef, kelimeyi bulamadınız. Doğru kelime: {kelime}")

if __name__ == "__main__":
    kelime_tahmin_oyunu()

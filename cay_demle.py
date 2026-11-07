#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra Yavaş Çay Demleyici
Dünyanın en yavaş çay demleme protokolü.
Çay içmek için sabır gerekir. Çok sabır.
"""

import time
import random
import sys

# Gizli not: bazen en yavaş demlenen çay, en özgür düşünceleri getirir. (saklı mesaj)
OZELLIKLER = [
    "Su kaynamaya başlıyor... ama acele etmiyor.",
    "Çay yaprakları düşüncelere daldı.",
    "Zamanın kendisi bile çayı bekliyor.",
    "Bir yudum için üç ömür geçti.",
    "Felsefe yaparken çay demlenir, demlenirken felsefe yapılır."
]

def yavas_ilerleme(mesaj, saniye=5):
    print(mesaj)
    for i in range(10):
        sys.stdout.write("\r" + "█" * i + " " * (10 - i) + f" %{i*10}")
        sys.stdout.flush()
        time.sleep(saniye / 10)
    print()

def cay_demle():
    print("=" * 50)
    print("ULTRA YAVAŞ ÇAY DEMLEME PROTOKOLÜ BAŞLATILDI")
    print("=" * 50)
    print("Bu işlem gerçekten uzun sürebilir. Çay içmeye karar verdiyseniz, kahve içmeyi düşünün.")
    print()

    yavas_ilerleme("Su ısıtılıyor... (gerçek hayatta bu 3 dakika sürer, burada 10 saniye)", 10)
    time.sleep(2)

    yavas_ilerleme("Çay yaprakları ekleniyor... her yaprak kendi hikayesini anlatıyor", 8)
    time.sleep(3)

    for _ in range(3):
        soz = random.choice(OZELLIKLER)
        print(f"\n🍵 Felsefi ara: {soz}")
        time.sleep(4)

    yavas_ilerleme("Demleme süresi... çay kendine geliyor", 15)
    time.sleep(5)

    print("\n" + "=" * 50)
    print("ÇAY HAZIR! ...ama içmek için bir 5 dakika daha bekleyin, soğusun.")
    print("Afiyet olsun. Eğer hâlâ buradaysanız, tebrikler, sabırlısınız.")
    print("=" * 50)

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\nÇay demleme iptal edildi. Belki de kahve daha hızlıdır.")

def harf(s):
    buyuk= sum(1 for char in s if char.isupper())
    kucuk=sum(1 for char in s if char.islower())
    return buyuk,kucuk

def main():
    metin=input("Metin girin:")
    upper,lower = harf(metin)
    print(f"Büyük harf sayısı: {upper}")
    print(f"Küçük harf sayısı: {lower}")

if __name__ == "__main__":
    main()
    
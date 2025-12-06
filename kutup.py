class Kutup:
    
    def __init__(self, kitapNo, kitapIsim, sayfaNo):
        self.kitapNo = kitapNo
        self.kitapIsim = kitapIsim
        self.sayfaNo = sayfaNo 

    def yazdir(self): 
        print(f"Kitapinizin numarası {self.kitapNo} kitabinizin ismi {self.kitapIsim} sayfa sayisi {self.sayfaNo}")
kutuphane=[]
sec='a'
while sec!='q' :
    try:
        no = int(input("Kitap numarasını giriniz "))
        isim= input("ismini girin ")
        sayfa=int(input("Sayfa sayısı girin "))
        kutuphane.append(Kutup(no,isim,sayfa))
        yaz=str(no) +" "+isim +" "+str(sayfa)+"\n"
        with open("kutup.txt","a",encoding="utf-8")as dosya:
            dosya.write(yaz)
    except ValueError:
        print("Lütfen rakam gereken yerlere rakamları giriniz")
        continue
    sec=input("cikmak icin q ya devam etmek için q hariç basın ")
for kitap in kutuphane:
    kitap.yazdir()

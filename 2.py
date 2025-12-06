class Kullanici:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email
    def bilgi(self):
        return self.isim + " " + self.email

class Ders:
    def __init__(self, ad, ogretmen):
        self.ad = ad
        self.ogretmen = ogretmen
        self.__notlar = {}
    def not_ekle(self, nott):
        self.__notlar.append(nott)
    def not_yazdir(self):
        for nota in self.__notlar:
            print(nota)
    def ort(self):
        if len(self.__notlar) == 0:
            return 0
        top = sum(self.__notlar)
        return top / len(self.__notlar.keys())

class Ogrenci(Kullanici):
    def __init__(self, isim, email, ogrenci_no):
        super().__init__(isim, email)
        self.ogrenci_no = ogrenci_no
    def bilgi(self):
        return super().bilgi() + " " + str(self.ogrenci_no)

class Ogretmen(Kullanici):
    def __init__(self, isim, email, brans):
        super().__init__(isim, email)
        self.brans = brans
    def bilgi(self):
        return super().bilgi() + " " + self.brans

class Platform:
    def __init__(self):
        self.kullanicilar = []
        self.dersler = []
    def ogrenci_ekle(self, isim, email, no):
        yeni_ogrenci = Ogrenci(isim, email, no)
        self.kullanicilar.append(yeni_ogrenci)
    def ders_ekle(self, ad, ogretmen):
        yeni_ders = Ders(ad, ogretmen)
        self.dersler.append(yeni_ders)
    def yazdir(self):
        for k in self.kullanicilar:
            print(k)
        for i in self.dersler:
            print (i)
if __name__ =="__main__":
    t1 = Ogretmen("beytullah","beytullah@btk.com.tr","ucus egitimi")
    s1 = Ogrenci("mehmet","kaan@gmail.cm","100")
    s2 = Ogrenci("me213","kaawqdas@gmail.cm","200")
    p = Platform()
    btk_python = Ders("btk ileri egiim",t1)
#şimdi selammmm
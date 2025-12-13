from dataclasses import dataclass

@dataclass
class MesajBilgi:
    mesaj: str
    kisi: str

class MesajDondurucu:
    def mesajDondur(self, bilgi: MesajBilgi):
        return f"{bilgi.kisi} kişisinden mesaj: {bilgi.mesaj}"

class Gonderici():
    def send(self, bilgiNesnesi: MesajBilgi):
        pass

class Email(Gonderici):
    def send(self, bilgiNesnesi: MesajBilgi):
        dondurucu = MesajDondurucu()
        icerik = dondurucu.mesajDondur(bilgiNesnesi)
        print(f"Email Gönderildi: {icerik}")

class Sms(Gonderici):
    def send(self, bilgiNesnesi: MesajBilgi):
        dondurucu = MesajDondurucu()
        icerik = dondurucu.mesajDondur(bilgiNesnesi)
        print(f"SMS Gönderildi: {icerik}")


benimMesajim = MesajBilgi(mesaj="Selam", kisi="Mahmut")

mailServisi = Email()
smsServisi = Sms()

mailServisi.send(benimMesajim)
smsServisi.send(benimMesajim)

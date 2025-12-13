from dataclasses import dataclass
from typing import Protocol
@dataclass
class MesajBilgi:
    mesaj: str
    kisi: str

class MesajDondurucu:
    def mesajDondur(self, bilgi: MesajBilgi)-> str:
        return f"{bilgi.kisi} kişisinden mesaj: {bilgi.mesaj}"

class Gonderici(Protocol):
    def send(self, bilgiNesnesi: MesajBilgi)->None:
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

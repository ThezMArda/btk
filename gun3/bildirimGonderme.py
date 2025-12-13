from dataclasses import dataclass

@dataclass
class MesajBilgi:
    mesaj: str

    def mesajDondur(self) -> str:
        return self.mesaj

class Email:
    def send(self, bilgi_nesnesi: MesajBilgi):
        icerik = bilgi_nesnesi.mesajDondur()
        print(f"Email : {icerik}")

class Sms:
    def send(self, bilgi_nesnesi: MesajBilgi):
        icerik = bilgi_nesnesi.mesajDondur()
        print(f"SMS : {icerik}")


benimMesajim = MesajBilgi(mesaj="email")
benimMesajim2= MesajBilgi(mesaj="sms")
mailServisi = Email()
mailServisi.send(benimMesajim2)
mailServisi.send(benimMesajim)

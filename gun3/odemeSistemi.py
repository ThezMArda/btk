from abc import abstractmethod
from dataclasses import dataclass
from typing import ParamSpec, Protocol

class fiyat(Protocol):
    @staticmethod
    def fiyat(para:float)->float:
        ...
class normalFiyat(fiyat):
    @staticmethod
    def fiyat(para):
        return para
class ogrFiyat(fiyat):
    @staticmethod
    def fiyat(para:float):
        return (para*0.9)
class blckFiyat(fiyat):
    @staticmethod
    def fiyat(para:float):
        return (para*0.8)
class odeme(Protocol):
    @staticmethod
    def ode(fiyat):
        pass

@dataclass
class ccOdeme(odeme):
    @staticmethod
    def ode(fiyat):
        print(f"kredi kartıyla ödendi {fiyat}")
@dataclass
class paypalOdeme(odeme):
    @staticmethod
    def ode(fiyat):
        print(f"paypal ile ödendi")
class factory:



    @staticmethod
    def create(channel:str,indirim : str,para:float,son):

        if(indirim=="o"):
            son =ogrFiyat.fiyat(para)
        elif(indirim =="n"):
            son =normalFiyat.fiyat(para)
        elif(indirim=="b"):
            son =blckFiyat.fiyat(para)
        if(channel=="cc"):
            return ccOdeme.ode(son)
        elif channel=="paypal":
            return paypalOdeme.ode(son)
        else :
            return "duzgun girilmedi"


@dataclass
class Logger:

    def __init__(self,para,channel,indirim) -> None:
        self.para = para
        self.channel=channel
        self.indirim=indirim
        factory.create(channel,indirim,para,0)

    _instance = None
    def __new__(cls) :
        if cls._instance is None:
            cls._instance=super().__new__(cls)

        return cls._instance
logger =Logger(100.0,"cc","o")

class Penalty_strategy:
    def calculate(self,days_late:int)->float:
        ...



class NoPenalty(Penalty_strategy):
    def NoPenalty(self,days_late:int)->float:
        print("ceza yok")
        return days_late*0.0

class StandartPenalty(Penalty_strategy):
    def standartPenalty(self,days_late:int)->float:
        return days_late*5.0

class StrictPenalty(Penalty_strategy):
    def strictPenalty(self,days_late:int)->float:
        
        return days_late*10.0
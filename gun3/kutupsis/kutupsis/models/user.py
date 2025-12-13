from dataclasses import dataclass
@dataclass
class User:
    user_name:str
    user_id:int

class StudentUser(User):
    can_lend =True
    can_get_penaltie=True
class TeacherUser(User):
    can_lend = True
    can_get_penaltie=False
class GuestUser(User):
    can_lend =False
    can_get_penaltie=True

class Factory_pattern:
    def create(self,channel):
        if(channel=="s"):
            return StudentUser("a",2)
        if(channel=="t"):
            return StudentUser("das",3)
        if(channel=="g"):
            return StudentUser("asda",4)

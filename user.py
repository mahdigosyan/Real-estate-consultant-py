from base import BaseClass

class User(BaseClass):
    def __init__(self,firstname,lastname,phone,*args,**kwargs):
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        super().__init__(*args,**kwargs)
    
    
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
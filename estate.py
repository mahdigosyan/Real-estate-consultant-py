from base import BaseClass

class EsatateAbastract(BaseClass):
    def __init__(self,user,area,rooms_count,built_year,region,address, *args, **kwargs):
        self,user=user
        self.area=area
        self.rooms_count=rooms_count
        self.built_year=built_year
        self.region=region
        self.address=address
        super().__init__(*args, **kwargs)

class Apartment(EsatateAbastract):
    pass

class House(EsatateAbastract):
    pass

class Store(EsatateAbastract):
    pass
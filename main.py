from random import choice
from user import User
from estate import Apartment , House ,Store
from region import Region
FIRST_NAME = ['mahdi','reza','ahmd']
LAST_NAME = ['kameli','rezasds','ahmdi']
PHONE = ['091245678','0918767654','09332657898']
if __name__=="__main__":
    for phone in PHONE:
        User(choice(FIRST_NAME),choice(LAST_NAME),phone)

    for user in User.object_list:
        print(f"{user.id}\t {user.fullname}")

    reg1= Region(name='R1')
    apt1 = Apartment(has_elevator=True,has_parking=True,floor=2,user=User.object_list[0],built_year=1396,region=reg1,area=80,rooms_count=2,address='meydan emam')
    apt1.show_description()


    house = House(
        has_yard=True, floor_count=1 , user=User.object_list[2], area=400,
        rooms_count=6 , built_year=1380 , region=reg1, address='na koja abad'
    )


    house.show_description()

    store = Store(
        user=User.object_list[-1],area=30,rooms_count=0,built_year=1390,
        region=reg1,address='hminja'
    )

    store.show_description()


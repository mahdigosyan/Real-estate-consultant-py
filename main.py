from random import choice
from user import User
FIRST_NAME = ['mahdi','reza','ahmd']
LAST_NAME = ['kameli','rezasds','ahmdi']
PHONE = ['091245678','0918767654','09332657898']
if __name__=="__main__":
    for phone in PHONE:
        User(choice(FIRST_NAME),choice(LAST_NAME),phone)

    for user in User.object_list:
        print(f"{user.id}\t {user.fullname}")
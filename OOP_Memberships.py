import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Users:
    def __init__(self, first_name, last_name, memberShip_id, memberShipStatus= 'inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.memberShip_id = memberShip_id
        self.memberShipStatus = memberShipStatus

    def display_members(self):
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'MemberShip id: {self.memberShip_id}')
        print(f'MemberShipstatus: {self.memberShipStatus}')
        print('_' * 20)

def create_users():
    first_name = input('enter your first name: ')
    last_name = input('enter your last name: ')
    memberShip_id = input('membership id: ')
    memberShipStatus = input('enter membership status, or click enter: ')
    if not memberShipStatus:
        memberShipStatus = 'inactive'
    return Users(first_name, last_name, memberShip_id, memberShipStatus)
# بداية دالة البحث

def search_member(members):
    clear_screen()
    print('\nSearch by: \n')
    print('1. Membership ID')
    print('2. First Name')
    print('3. Membership Status\n')

    search_choice = int(input('Enter your choice: '))
    
    found_members = []

    if search_choice == 1:
        search_id = input('Enter membership ID to search: ')
        for x in members:
            if x.memberShip_id == search_id:
                found_members.append(x)  
                break  
    
    elif search_choice == 2:
        search_name = input('Enter membership name to search: ')
        for x in members:
            if x.first_name == search_name:
                found_members.append(x)

    elif search_choice == 3:
        search_status = input('Enter member status: ')
        for x in members:
            if x.memberShipStatus == search_status:
                found_members.append(x)
    else:
        print('invalid choice')

    if found_members:
        clear_screen()
        print('Members found: ')
        for x in members:
            x.display_members()
    else:
        print('Member not found!')
    time.sleep(2)

# نهاية دالة البحث
members = []
while True:
    print('''welcome to membership managment 
          choose an action:
          1. add new member
          2. display all member
          3. search for a member
          4. exit''')
    
    choice = int(input('enter your choice: '))
    if choice == 1:
        members.append(create_users())
        print('member added seccusfly') 
        print('wait')
        time.sleep(1)
    
    elif choice == 2:
        clear_screen()
        if members:
            print('diplaying all new members ..')
            time.sleep(1)
            for i in members:
                i.display_members()
                time.sleep(1)
        else:
            print('sorry no one to display')
            time.sleep(1)

    elif choice == 3:
        if members:
            search_member(members)
        else:
            print('no members to display')
            time.sleep(2)

    
    elif choice == 4:
        print('exiting...')
        break

    else:
        print('invalid move')
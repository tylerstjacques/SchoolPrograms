class Contact:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.phone = 0
        self.address = ''


me = Contact()
me.name = 'Tyler'
me.email = 'tyler@gmail.com'
me.phone = 1112223333
me.address = '123 abc street'
your_contact = [me.name, me.email, me.phone, me.address]
print('Your contact: ', your_contact)


friend = Contact()
friend.name = 'Kyle'
friend.email = 'kyle@gmail.com'
friend.phone = '3332221111'
friend.address = '321 abc street'
friend_contact = [friend.name, friend.email, friend.phone, me.address]
print("Friends Contact: ", friend_contact)
print(your_contact, friend_contact)

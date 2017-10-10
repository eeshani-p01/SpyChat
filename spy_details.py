from datetime import datetime
# # spy = {
#     'name' : 'Bond',
#     'salu' : 'Dr.',
#     'age' : 23,
#     'rating' : 4.7,
#     'is_online' : True
# }
class Chat:

    def __init__(self, name, message, sent_by_me):
        self.name = name
        self.message = message
        self.time = datetime.now().strftime("%b %d %Y %H:%M:%S")
        self.sent_by_me = sent_by_me

# chats = []
# chat_details = Chat("Hey","ME")
# chats.append(chat_details)
# print chats

class Spy:

    def __init__(self, name, salu, age, rating):
        self.name = name
        self.salu = salu
        self.age = age
        self.rating =rating
        self.is_online = True
        self.chats = []
        self.current_status = None
#
# friends = []
# spy = Spy('Bond', 'Mr.', 23, 5)
# # friends.append(list(spy))
# print list(spy)
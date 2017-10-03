from datetime import datetime
# # spy = {
#     'name' : 'Bond',
#     'salu' : 'Dr.',
#     'age' : 23,
#     'rating' : 4.7,
#     'is_online' : True
# }
class Chat:

    def __init__(self, message, time, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


class Spy:

    def __init__(self, name, salu, age, rating):
        self.name = name
        self.salu = salu
        self.age = age
        self.rating =rating
        self.is_online = True
        self.chats = []
        self.current_status = None
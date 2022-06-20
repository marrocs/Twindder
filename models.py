from datetime import datetime

user_counter = 1
chat_counter = 1
message_counter = 1

class Chat:
    
    global chat_counter

    def __init__(self, user1, user2) -> None:
        self.chat_id = str(666) + str(chat_counter)
        self.datetime_init = datetime.now()
        self.user1 = user1
        self.user2 = user2
        self.user1_messages = []
        self.user2_messages = []

        user1.chats.append(self)
        user2.chats.append(self)

        chat_counter += 1  

class Message:

    global message_counter

    def __init__(self, sender, receiver, chat_id, content) ->  None:
        self.message_id = str(999) + str(message_counter)
        self.sender = sender
        self.receiver = receiver
        self.chat_id = chat_id
        self.datetime = datetime.now()
        self.content = content

class User:

    def __init__(self, name, password):
        
        global user_counter

        self.registry = user_counter
        self.name = name
        self.password = password
        self.liked = []
        self.matchs = []
        self.chats = []

        user_counter += 1

    def __str__(self) -> str:
        return f'Registry: {self.registry}, Name: {self.name}, Password: {self.password}, Liked_list: {self.liked}, matchs: {self.matchs}'

    def __dict__(self) -> dict:
        return {'Registry': {self.registry}, 'Name': {self.name}, 'password': {self.password}, 'Liked list': {self.liked}, 'matchs': {self.matchs}}

    def __repr__(self):
        return self.name

    @property
    def call_name(self) -> None:
        return self.name
    
    @property
    def call_password(self) -> None:
        return self.password

    @property
    def call_liked_list(self) -> None:
        return self.liked

    @call_liked_list.setter
    def model_like_profile(self, liked_user) -> None:
        self.liked.append(liked_user)
        return f'{liked_user.name} got liked'

    def unmatch_profile(self, unmatched_user) -> None:
        pass

    def see_matchs(self) -> None:

        for m in self.matchs:
            return m

    def send_message(self, receiver) -> None:

        message = input('Say something: ')
        
        for cht in self.matchs:
            if cht.user1 == self and cht.user2 == receiver: # saber se há um objeto Chat que tenha self e receiver como user1 e user2 (checar em ambos 'self.matchs')
                mssg = Message(self, receiver, cht.chat_id, message)  # Se existente, criar Message com message como message, self como sender e receiver como receiver
                cht.user1_messages.append(mssg) # Adiciona mssg a uma lista de mensagens de Chat
            else:   # Se não existe, criar um Chat com self como user1 e receiver como user2
                chat = Chat(self, receiver)
                self.chats.append(chat)
                
                mssg = Message(self, receiver, chat.chat_id, message)  # Se existente, criar Message com message como message, self como sender e receiver como receiver
                cht.user1_messages.append(mssg) # Adiciona mssg a uma lista de mensagens de Chat
        
    

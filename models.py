from atexit import register
from random import randint
import main

cont = 1

class User:

    def __init__(self, name, password):
        global cont

        self.registry = cont
        self.name = name
        self.password = password
        self.liked = []
        self.matches = []

        cont += 1
    
    def __str__(self) -> str:
        return f'Registry: {self.registry}, Name: {self.name}, Password: {self.password}, Liked_list: {self.liked}, matches: {self.matches}'

    def __dict__(self) -> dict:
        return {'Registry': {self.registry}, 'Name': {self.name}, 'password': {self.password}, 'Liked list': {self.liked}, 'matches': {self.matches}}

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
    def like_person(self, displayed_user) -> None:
        self.liked.append(displayed_user)
        return f'{displayed_user.name} got liked'

    def see_matches(self) -> None:
        return self.matches

from random import randint
import main

class User:

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__liked = []

    @property
    def nome(self) -> None:

        return self.__nome
    
    @property
    def senha(self) -> None:
        return self.__senha

    @property
    def liked_list(self):
        return print(self.__liked)

    def see_profiles():

        if main.show_profiles == True:
            perfil = main.profiles_catalog[randint(0, len(main.profiles_catalog)-1)].nome

            print(perfil)

            acao2 = input('O que achou da pessoa acima? (s/n)')

            pass

    def like_person(self, perfil):

            User.likes.append(perfil)
            print(f'Você deu like em {perfil.nome}')

class User:

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__liked = []

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self) -> None:
        return self.__senha

    @property
    def liked_list(self):
        return print(self.__liked)

    def like_person(self, perfil):
        self.__liked.append(perfil)
        print(f'Você deu like em {perfil.nome}')

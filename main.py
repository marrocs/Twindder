from operators_functions import *

profiles_catalog = []


def main():
    # Recebe ação (cria user / login)
    action1 = int(input('Digite 1 para criar usuario, ou 2 para fazer login: '))
    # Cria usuario
    while action1 == 1:
        create_user()
        action1 = int(input('Digite 1 para criar usuario, ou 2 para fazer login: '))

    #  Login
    if action1 == 2:
        check_email(input('Digite seu email: '))

    list_profiles()
    #  Listagem perfis
    #  acao (move p/ lista liked ou listagem()
    #  Checagem match


if __name__ == '__main__':
    main()

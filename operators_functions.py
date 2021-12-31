from class_user import *
from main import *
from random import randint


def create_user():
    nome = input('Insira seu nome: ')
    senha = input('Insira a senha desejada: ')

    user = User(nome, senha)
    profiles_catalog.append(user)


def check_email(email):
    for user in profiles_catalog:
        if user.nome == email:
            check_senha(input('Digite sua senha: '))
        else:
            print('Usuário inexistente.')
            return False


def check_senha(senha):
    for user in profiles_catalog:
        if user.senha == senha:
            return print('Login feito com sucesso!')
        else:
            print('Senha incorreta.')
            return False


def list_profiles():
    perfil = profiles_catalog[randint(0, len(profiles_catalog)-1)].nome
    print(perfil)

    acao2 = input('O que achou da pessoa acima? (s/n)')

    if acao2 == 's':
        User.like_person(perfil)
        list_profiles()
    else:
        list_profiles()

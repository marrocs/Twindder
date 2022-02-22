from operators_functions import *
from class_user import *

profiles_catalog = []
show_profiles = False
user_in_command = ""

def main():

    def create_user(nome, senha) -> str:

        user = User(nome, senha)
        print(f'TESTE: perfil criado com o nome de {nome} e senha {senha}.')
        profiles_catalog.append(user)

        print("perfil criado com sucesso!")
        print(f'TESTE: total de usuarios na lista: {len(profiles_catalog)} usuarios')
    
    def login(nome, senha):
        
        print(f'TESTE: função iniciada. Total: {len(profiles_catalog)} usuarios cadastrados')

        for usuario in range(len(profiles_catalog)):
            if profiles_catalog[usuario].nome == nome:
                print('Usuario encontrado')
                if profiles_catalog[usuario].senha == senha:
                    main.show_profiles = True
                    main.user_in_command = usuario
                    print('Login autorizado')
                    User.see_profiles()
                    action1 == 4

                else:
                    print('Acesso negado')
                    main.action1 = int(input('Digite 1 para criar usuario, 2 para fazer login ou 3 para sair: ')) 
            else:
                print('Nome de usuario incorreto')
                main.action1 = int(input('Digite 1 para criar usuario, 2 para fazer login ou 3 para sair: '))
        
        # Recebe ação (cria user / login)
    action1 = int(input('Digite 1 para criar usuario, 2 para fazer login ou 3 para sair: '))

        #  Cria usuario
    while action1 == 1:

        nome, senha = input('Insira seu nome: '), input('Insira a senha desejada: ')
        create_user(nome, senha)
        action1 = int(input('Digite 1 para criar usuario, ou 2 para fazer login: '))
        #  Login
    while action1 == 2:
        nome, senha = input('Digite seu nome: '), input('Digite sua senha: ')
        login(nome, senha)
        #  Exit
    if action1 == 3:
        exit()
        #  See_profiles
    while action1 == 4:
        User.see_profiles()

if __name__ == '__main__':
    main()

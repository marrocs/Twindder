from models import *
import json

# --- to do: change 'profiles_catalog' data set from list to dict? --- 
profiles_catalog = []
show_profiles = False

def main():

    def create_user(name, password) -> str:

        user = User(name, password)
        print(f'(l.11) TESTE: perfil número {user.registry} criado com o nome de {user.name} e password {user.password}.')
        profiles_catalog.append(user)

        print("perfil criado com sucesso!")
        print(f'(l.15) TESTE: total de usuarios na lista: {len(profiles_catalog)} usuarios')

        return user
    
    def login(name, password):
        
        print(f'(l;19) TESTE: função iniciada. Total: {len(profiles_catalog)} usuarios cadastrados')

        for profile in profiles_catalog:
            if profile.name == name:
                print('Usuario encontrado')
                if profile.password == password:
                    main.show_profiles = True
                    print('Login autorizado')
                    act1 == 4

                else:
                    print('Acesso negado')
                    main.act1 = int(input('Type\n1 to create user\n2 to login\n3 to exit ')) 
            else:
                print('Nome de usuario incorreto')
                main.act1 = int(input('Type\n1 to create user\n2 to login\n3 to exit '))
        
    def show_profiles(control_user):

        displayed_user = profiles_catalog[randint(0, len(profiles_catalog))]
        
        user_like_answer = input(f'{displayed_user} \n\nDo you like user above? Y/N ').lower()

        if user_like_answer == 'y':
            like_profile(control_user, displayed_user)
        
        else:
            show_profiles(control_user)

    def like_profile(control_user, displayed_user):
        
        liking_user = control_user
        liked_user = displayed_user
        
        liking_user.like_profile(liked_user)
        print('User liked!')

    def check_match(control_user, displayed_user):
        
        if control_user in displayed_user.liked:
            if displayed_user in control_user.liked:
                displayed_user.matches.append(control_user)
                control_user.matches.append(displayed_user)
                print(f'You and {displayed_user.name} like each other. Go talk (: ')
    
    def see_matches(control_user):
        print(control_user.see_matches())

    
    act1 = int(input('Type: \n1 to create user\n2 to login\n3 to exit \nYour answer: '))

    # --- Create user ---
    while act1 == 1:

        alpha = input('is this test?')

        if alpha == 'y':
            
            # --- for tests ---
            with open('C:\\Users\\Lucas\\Documents\\LUCAS\programacao\\python\\meus_projetos\\FreteDatingApp\\tests\\data.json', 'r', encoding='utf-8') as data:
                dt = json.load(data)
                
                for x in dt:
                    print('\n', x, '\n')

                    username = x['nome']
                    user_password = x['cpf']

                    print(username, user_password)

                    user = create_user(str(username), str(user_password))

                    print(f"Perfil número {user.registry} criado: {user.name}")
            
            act1 = int(input('Type: \n1 to create user\n2 to login\n3 to exit '))
        
        else:
            # --- for production ---
            name, password = input('What is your name: '), input('type your password: ')
            create_user(name, password)
            act1 = int(input('Type: \n1 to create user\n2 to login\n3 to exit'))

    # --- Login ---
    while act1 == 2:
        
        control_user = input('Enter your name: ').lower()
        control_user_password = input('Your password: ')

        for x in profiles_catalog:
            if x.name == control_user:
                if x.password == control_user_password:
                    print('Login succed')
                    act1 = 3

                else:
                    print('Wrong password.')
                    act1 == 2
            else:
                print("User doesn't exist")
                act1 == 2
    
    # --- Show profiles ---
    while act1 == 3:
        
        for x in profiles_catalog:
            print(str(x))

            act2 = input(f'Did you like {x.name}? Y/N').lower()

            if act2 == 'y':
                like_profile(control_user, x)
                show_profiles(control_user)
            else:
                show_profiles(control_user)
        
    # --- Exit ---
    while act1 == 4:
        exit()

if __name__ == '__main__':
    main()

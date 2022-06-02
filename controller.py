from models import *
import json

# --- to do: change 'profiles_catalog' data set from list to dict? --- 
profiles_catalog = []

def main():

    def create_user(name, password) -> str:

        user = User(name, password)
        print(f'(l.11) TEST: perfil número {user.registry} criado com o nome de {user.name} e password {user.password}.')
        profiles_catalog.append(user)

        print("perfil criado com sucesso!")
        print(f'(l.15) TEST: total de usuarios na lista: {len(profiles_catalog)} usuarios')

        return user
    
    def login(name, password):
        pass
        
    def show_random_profile():

        displayed_user = profiles_catalog[randint(0, len(profiles_catalog) - 1)]
            
        return displayed_user
    
    def main_like_profile(control_user, displayed_user):
        
        liking_user = control_user
        liked_user = displayed_user
        
        liking_user.model_like_profile = liked_user  # That line of code was breaking. Dude 'Oli' at StackO solved it
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
            with open('C:\\Users\\Lucas\\Documents\\LUCAS\programacao\\python\\meus_projetos\\twindder\\tests\\data.json', 'r', encoding='utf-8') as data:
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

                    control_user = x
                    print('Login succeeded')
                    act1 = 3
                else:
                    print('Information doesnt match.')
    
    # --- Show profiles ---
    while act1 == 3:

        displayed_user = show_random_profile()

        user_like_answer = input(f'{displayed_user} \n\nDo you like user above? Y/N \n\nYour answer: ' ).lower()

        if user_like_answer == 'y':

            main_like_profile(control_user, displayed_user)
            
            print(f'You liked: {displayed_user.name}')

            check_match(control_user, displayed_user)

        elif user_like_answer == 'n':
            act1 = 3
        
        else:
            act2 = input('1 - See matches\n2 - Settings\n3 - to EXIT \nYour answer: ')

            if act2 == '1':
                see_matches(control_user)

            elif act2 == '2':
                pass

            elif act2 == '3':
                print('Goodbye, cruel world')
                exit()

            else:
                pass
            
    # --- Exit ---
    while act1 == 4:
        exit()

if __name__ == '__main__':
    main()

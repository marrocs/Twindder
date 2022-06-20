'''
Functionalities:
    1) Login - OK
    2) See Users - OK
    3) Like User - OK
    4) Check for match - OK
    5) Send messages - TODO
    6) Retrieve data from Twitter - TODO
'''

from random import randint
from models import *
import json

# --- to do: change 'profiles_catalog' data set from list to dict? --- 
profiles_catalog = []

def main():

    # --- 'create user' function. Take no argument and get from user 'username' and 'password' to instantiate a User object, than append it to 'profiles_catalog'
    def create_user(name, password) -> str:

        user = User(name, password)

        profiles_catalog.append(user)

        print("perfil criado com sucesso!")

        return user
    
    # --- 'login' function. Takes 'username' and 'password' and check it is the same as in 'profile_catalog' TO BE implemented
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
                displayed_user.matchs.append(control_user)
                control_user.matchs.append(displayed_user)
                print(f'You and {displayed_user.name} like each other. Go talk (: ')
    
    def see_matchs(control_user):
        print(control_user.see_matchs())

    
    act1 = int(input('Press: \n1 to create user\n2 to login\n3 to exit \nYour answer: '))

    # --- Create user ---
    while act1 == 1:

        alpha = input('is this test?')

        # --- uncomment for tests ---
        if alpha == 'y':
            
            with open('C:\\Users\\Lucas\\Documents\\LUCAS\programacao\\python\\meus_projetos\\twindder\\tests\\data.json', 'r', encoding='utf-8') as data:
                dt = json.load(data)
                
                for x in dt:
                    username = x['nome']
                    user_password = x['cpf']

                    user = create_user(str(username).lower(), str(user_password))

                    print(f"Perfil número {user.registry} criado: {user.name}")
            
            act1 = int(input('Press: \n1 to create user\n2 to login\n3 to exit \nYour answer: '))
        
        # --- for production ---
        else:
            name, password = input('What is your name: '), input('type your password: ')
            create_user(name, password)
            act1 = int(input('Press: \n1 to create user\n2 to login\n3 to exit \nYour answer: '))

    # --- Login ---
    while act1 == 2:
        
        control_user = input('Enter your name: ').lower().strip()
        control_user_password = input('Your password: ')

        for profile in profiles_catalog:

            if profile.name == control_user:

                if profile.password == control_user_password:

                    control_user = profile
                    print('Login succeeded')
                    act1 = 3
                else:
                    print('password doesnt match.')
            else:
                print('user not found')
    
    # --- Show profiles ---
    while act1 == 3:

        displayed_user = show_random_profile()

        # --- prevent user to see itself ---
        if displayed_user == control_user:
            act1 = 3
        
        # --- prevent user to see others users already liked --- 
        elif displayed_user in control_user.liked:
            act1 = 3
        
        # --- show all others --- 
        else:
            user_like_answer = input(f'{displayed_user} \n\nDo you like user above? Yes / No / Else \n\nYour answer: ' ).lower()

            if user_like_answer == 'y' or user_like_answer == 'yes':

                main_like_profile(control_user, displayed_user)
                
                print(f'You liked: {displayed_user.name}')  # remove line for production

                check_match(control_user, displayed_user)

            elif user_like_answer == 'n' or user_like_answer == 'no':
                act1 = 3
            
            else:
                act2 = input('1 - See matchs\n2 - Show profiles\n3 - Settings\n4 - to exit to main\nYour answer: ')

                if act2 == '1':
                    see_matchs(control_user)

                    act3 = input('Type the id of user you want to talk, or "no" to return: ')
                    
                    # --- problems in section below. Script doesnt find user by it registry
                    if act3 == 'no' or act3 == 'n':
                        act2 = input('1 - See matchs\n2 - Show profiles\n3 - Settings\n4 - to exit to main\nYour answer: ')
                    else:
                        for num, lkd in enumerate(control_user.liked):
                            if (num + 1) == int(act3):
                                control_user.send_message(control_user, control_user.liked[int(act3)])
                            else:
                                print('User nor found!')
                                act3 = input('Type the id of user you want to talk, or "no" to return: ')
                    
                elif act2 == '2':
                    show_random_profile()

                elif act2 == '4':
                    main()

                else:
                    pass

    # --- Exit ---
    while act1 == 4:
        exit()

if __name__ == '__main__':
    main()

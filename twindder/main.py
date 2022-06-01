import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root_breno',
    passwd='projeto_breno'
)

mycursor = db.cursor()

def main():

    action1 = input('Digite para acessar: ')   # Receceber o usuario (login/'clique para acessar a ferramenta')
    
    if action1:
        pass    # receber o usuario // conectar  api

    def checa_user(user):    # Se existente, exibir um perfil (função)
        if user in db:
            mostra_perfis()

    def mostra_perfis():    # exibir perfis (função)
        pass
    
    # Apresentar o perfil e receber o que o usuario acha
    
    def checa_match():    # Verificar se os perfis se curtem (função)
        pass

if __name__ == '__name__':
    main()
"""
Discipline: PROGRAMMING LANGUAGE APPLIED TO AUTOMATION. - LPAA
Teacher: João Fausto Lorenzato de Oliveira
Students: Guilherme Barros, Lukas Ponciano

Project of a system that performs registration, rent or sale to a car rental company in python.

initiation of the program...
"""

# Tags

tag = True

# Variaveis globais

lst_clientes = [['ID', 'Nome', 'Login', 'Senha', 'CPF', 'idade', 'datanasc', 'divida_com_a_empresa']]
lst_perfispendentes = [['ID', 'Nome', 'Login', 'Senha', 'CPF', 'idade', 'datanasc']]
lst_funcionarios = [['ID', 'Nome', 'Login', 'Senha', 'CPF', 'idade', 'datanasc']]
lst_gerentes = [['ID', 'Nome', 'Login', 'Senha', 'CPF', 'idade', 'datanasc']]
lst_usuarios = [lst_gerentes ,lst_clientes, lst_funcionarios]
lst_tarifasdiarias = [1,2,3]

# Funcoes e resto do codigo

def main():
    print('Iniciando sistema ...\n')
    print('Locadora de Vans Localiza, bem-vindo!\n')
    
    inicia_sistema()

def inicia_sistema():
    x = 0 # variavel provisoria, apenas para nao estourar o while
    while(tag):
        print('colocar coisas primarias aqui')
        x += 1
        
        if x == 7:
            break
        
main()

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

lst_clientes = [['ID', 'Nome','CPF', 'idade', 'datanasc', 'Login', 'Senha', 'divida_com_a_empresa']]
lst_perfispendentes = [['ID', 'Nome','CPF', 'idade', 'datanasc']]
lst_funcionarios = [['ID', 'Nome','CPF', 'idade', 'datanasc', 'Login', 'Senha']]
lst_gerentes = [['ID', 'Nome','CPF', 'idade', 'datanasc', 'Login', 'Senha']]
lst_usuarios = [lst_gerentes ,lst_clientes, lst_funcionarios]
lst_tarifasdiarias = [1,2,3]

# Funcoes e resto do codigo

def main():
    print('Iniciando sistema ...\n')
    print('Locadora de Vans Localiza, bem-vindo(a)!\n')
    
    inicia_sistema()

def inicia_sistema():
    x = 0 # variavel provisoria, apenas para nao estourar o while
    while(tag):
        opcoes_iniciais()
        x += 1
        if x==1:
            break

def opcoes_iniciais():
    entrada_inicial = 0
    tp_entrada = ('1','2')
    
    while(entrada_inicial not in tp_entrada):
        entrada_inicial = raw_input('Opcoes do sistema. Digite: 1 para logar ou 2 para realizar cadastro\n')
    
    if entrada_inicial=='1':
        print('o sport ta na final')
    else:
        realizar_cadastro()
        
    return 0

def realizar_cadastro():
    lst_perguntas = ['\nNome: ', '\nCPF: ', '\nIdade: ', '\nData de nascimento: ', '\nLogin desejado: ', '\nSenha escolhida: ']
    lst_dados = []
    x = 0
    
    print('\nEntrada de dados para cadastro. Responda conforme o que for pedido:')
    while(x<6):
        entrada_dados = raw_input('%s' %(lst_perguntas[x]))
        lst_dados.append(entrada_dados)
        x+=1
    print(lst_dados)
    
    return
    
##    lst_perfispendente.append(lst_dados) aparentemente só funciona com a lista passando como parâmetro
        
main()

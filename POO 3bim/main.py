# Trabalho de POO do IFRO calama
# Grupo: Geovana Garcia, Theo Henrique, Ítalo Silva
# Porfessora: Camila Serrão
# Turma: 2º M Informática

# ==============================================================================================

import classe
import funcoes
from funcoes import ForaDeAlcance

# aluno1= classes.Aluno('italo', 'idad', '123', 'dsada', '213213','dsad', 'dsad', '123')
# aluno1.cadastrar()
# composição
# Adicionando os alunos à lista de almoços grátis do primeiro aluno


tipo_user = funcoes.loop_Pergunta('login', 'Tipo de usuário: ',
                                  ['Aluno', 'Visitante', 'Dono do restaurante', 'Funcionário do DEPAE'],
                                  'Usuário inexistente! TENTE NOVAMENTE!')

while True:
        try:
                tipo_user = funcoes.loop_Pergunta('login', 'Tipo de usuário: ', ['Aluno', 'Visitante', 'Dono do restaurante', 'Funcionário do DEPAE'], 'Usuário inexistente! TENTE NOVAMENTE!')

                break
        except Exception:
                print("ERRO!!, coloque um número.")


if tipo_user == 1:
       
        login_ou_cadastro = funcoes.loop_Pergunta('Cadastro ou login', 'Você deseja fazer login ou se cadastrar? ',
                                                ['Login', 'Cadastro'], 'OPÇÃO INEXISTENTE! TENTE NOVAMENTE!')
        
      
        while True:
                if login_ou_cadastro == 1:
                        while True:
                                print('=' * 50)
                                print('LOGIN'.center(50))
                                print('=' * 50)
                                login_aluno_matric = input('Qual o nº da matrícula? ')
                                login_aluno_senha = input('Qual a senha? ')

                                aluno_objeto = classe.Aluno('', '', login_aluno_senha, '', '', '', '', login_aluno_matric, '')

                                if aluno_objeto.logar():
                                        lista_almoc_hj = classe.AlmocoGratis(aluno_objeto)
                                        print('Os alunos que têm direito a almoço grátis hoje são: ')
                                        print(lista_almoc_hj.exibir_almoco())
                                        exit()

                                else:
                                        print('\n\033[31mUsuário inexistente!\033[m\n')
                                        print('=' * 50)
                                        ir_pro_cadastro = input('Você deseja fazer o cadastro? (S/N) \n-> ').upper()
                                        if ir_pro_cadastro == 'S':
                                                login_ou_cadastro = 2
                                                break

                if login_ou_cadastro == 2:
                        print('=' * 50)
                        print('CADASTRO'.center(50))
                        print('=' * 50)
                        while True:
                                try:
                                        aluno_nome = input("Nome: ")

                                        if aluno_nome.isalpha():
                                                break
                                        else:
                                                print("Digite apenas letras")
                                                raise ValueError
                                except ValueError:
                                        print('\033[31mTente novamente!\033[m')

                        aluno_email = input("Email: ")
                        aluno_senha = input("Senha: ")

                        while True:
                                try:
                                        aluno_n_telefone = input("Número de telefone: ")
                                        if aluno_n_telefone.isnumeric():
                                                break
                                        else:
                                                print('Digite apenas números!')
                                                raise ValueError
                                except ValueError:
                                        print('\033[31mTente novamente!\033[m')

                        aluno_curso = input("Curso: ")

                        aluno_turma = input("Turma: ")

                        while True:
                                try:
                                        aluno_cpf = input("CPF: ")
                                        if aluno_cpf.isnumeric():
                                                break
                                        else:
                                                print('Digite apenas números!')
                                                raise ValueError
                                except ValueError:
                                        print('\033[31mTente novamente!\033[m')

                        while True:
                                try:
                                        aluno_matricula = input("Matrícula: ")

                                        if aluno_matricula.isnumeric():
                                                break
                                        else:
                                                print('Digite apenas números!')
                                                raise ValueError

                                except ValueError:
                                        print('\033[31mTente novamente!\033[m')

                        while True:
                                try:
                                        aluno_dias_contraturno = input('Dias de contraturno (Digite 2 para Segunda, 3 para Terça, etc...): ')

                                        if aluno_dias_contraturno.isalpha():
                                                raise ValueError

                                        if int(aluno_dias_contraturno) < 1 or int(aluno_dias_contraturno) > 5:
                                                raise ForaDeAlcance()
                                        else:
                                                break

                                except ValueError:
                                        print("Por favor, insira um número inteiro válido.")
                                except ForaDeAlcance:
                                        print("Digite apenas número de 1 a 5.")


                        aluno_objeto = classe.Aluno(aluno_nome, aluno_email, aluno_senha, aluno_n_telefone, aluno_cpf, aluno_curso,
                                                        aluno_turma, aluno_matricula, aluno_dias_contraturno)
                        aluno_objeto.cadastrar()

                        login_ou_cadastro = 1

if tipo_user == 2:
        login_ou_cadastro = funcoes.loop_Pergunta('Cadastro ou login', 'Você deseja fazer login ou se cadastrar? ',
                                                ['Login', 'Cadastro'], 'OPÇÃO INEXISTENTE! TENTE NOVAMENTE!')
        while True:
                if login_ou_cadastro == 1:
                        while True:
                                print('=' * 50)
                                print('LOGIN'.center(50))
                                print('=' * 50)
                                login_visitante_cpf = input('Qual o seu CPF? ')
                                login_visitante_senha = input('Qual a sua senha? ')

                                visitante_objeto = classe.Visitantes('', '', login_visitante_senha, '', login_visitante_cpf)

                                if not visitante_objeto.logar():
                                        print('\n\033[31mUsuário inexistente!\033[m\n')
                                        print('=' * 50)

                                        ir_pro_cadastro = input('Você deseja fazer o cadastro? (S/N) \n-> ').upper()
                                if ir_pro_cadastro == 'S':
                                        login_ou_cadastro = 2
                                        break

                                else:
                                        visitante_objeto.logar()
                                        exit()

                        if login_ou_cadastro == 2:
                                print('=' * 50)
                                print('CADASTRO'.center(50))
                                print('=' * 50)
                                while True:
                                        try:
                                                visitante_nome = input("Nome: ")
                                                if visitante_nome.isalpha():
                                                        break
                                                else:
                                                        raise ValueError
                                        except ValueError :
                                                print("\033[31mDigite apenas letras!\033[m")
                                        visitante_email = input("Email: ")
                                        visitante_senha = input("Senha: ")
                                while True:
                                        try:
                                                visitante_n_telefone = input("Número de telefone: ")
                                                if visitante_n_telefone.isnumeric() and visitante_n_telefone.isspace()==False:
                                                        break
                                                else:
                                                        raise ValueError
                                        except ValueError:
                                                print("\033[31mDigite apenas números!\033[m")

                                visitante_cpf = input("CPF: ")

                                visitante_objeto = classe.Visitantes(visitante_nome, visitante_email, visitante_senha, visitante_n_telefone,
                                                                        visitante_cpf)
                                visitante_objeto.cadastrar()
                                login_ou_cadastro = 1

if tipo_user == 3:

        login_ou_cadastro = funcoes.loop_Pergunta('Cadastro ou login', 'Você deseja fazer login ou se cadastrar? ',
                                                ['Login', 'Cadastro'], 'OPÇÃO INEXISTENTE! TENTE NOVAMENTE!')
        while True:
                if login_ou_cadastro == 1:
                        while True:
                                print('=' * 50)
                                print('LOGIN'.center(50))
                                print('=' * 50)
                                login_restaurante_cnpj = input('Qual o CPNJ? ')
                                login_restaurante_senha = input('Qual a senha? ')

                                restaurante_objeto = classe.Restaurante('', '', login_restaurante_senha, "", "", login_restaurante_cnpj,
                                                                        '')

                                if not restaurante_objeto.logar():
                                        print('\n\033[31mUsuário inexistente!\033[m\n')
                                        print('=' * 50)
                                        ir_pro_cadastro = input('Você deseja fazer o cadastro? (S/N) \n-> ').upper()
                                if ir_pro_cadastro == 'S':
                                        login_ou_cadastro = 2
                                        break

                                else:
                                        restaurante_objeto.logar()
                                        exit()

                if login_ou_cadastro == 2:
                        print('=' * 50)
                        print('CADASTRO'.center(50))
                        print('=' * 50)
                        restaurante_nome = input("Nome do titular: ")
                        restaurante_email = input("Email: ")
                        restaurante_senha = input("Senha: ")
                        restaurante_n_telefone = input("Número de telefone: ")
                        restaurante_cpf = input("CPF: ")
                        restaurante_cnpj = input("CNPJ: ")
                        restaurante_nomeEmpresa = input("Nome do restaurante: ")

                        restaurante_objeto = classe.Restaurante(restaurante_nome, restaurante_email, restaurante_senha,
                                                                restaurante_n_telefone, restaurante_cpf, restaurante_cnpj,
                                                                restaurante_nomeEmpresa)
                        restaurante_objeto.cadastrar()
                        login_ou_cadastro = 1

if tipo_user == 4:

        login_ou_cadastro = funcoes.loop_Pergunta('Cadastro ou login', 'Você deseja fazer login ou se cadastrar? ',
                                                ['Login', 'Cadastro'], 'OPÇÃO INEXISTENTE! TENTE NOVAMENTE!')
        while True:
                if login_ou_cadastro == 1:
                        while True:
                                print('=' * 50)
                                print('LOGIN'.center(50))
                                print('=' * 50)
                                login_depae_siape = input('Qual o nº do SIAPE? ')
                                login_depae_senha = input('Qual a sua senha? ')

                                depae_objeto = classe.Func_Depae('', '', login_depae_senha, '', '', login_depae_siape)

                                if not depae_objeto.logar():
                                        print('\n\033[31mUsuário inexistente!\033[m\n')
                                        print('=' * 50)
                                        ir_pro_cadastro = input('Você deseja fazer o cadastro? (S/N) \n-> ').upper()
                                        if ir_pro_cadastro == 'S':
                                                login_ou_cadastro = 2
                                                break

                                else:
                                        depae_objeto.logar()
                                        exit()

                        if login_ou_cadastro == 2:
                                print('=' * 50)
                                print('CADASTRO'.center(50))
                                print('=' * 50)
                                depae_nome = input("Nome: ")
                                depae_email = input("Email: ")
                                depae_senha = input("Senha: ")
                                depae_n_telefone = input("Número de telefone: ")
                                depae_cpf = input("CPF: ")
                                depae_siape = input('Siape: ')

                                depae_objeto = classe.Func_Depae(depae_nome, depae_email, depae_senha, depae_n_telefone, depae_cpf,
                                                                depae_siape)
                                depae_objeto.cadastrar()
                                login_ou_cadastro = 1
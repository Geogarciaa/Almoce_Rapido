from abc import ABC, abstractmethod
import time
import datetime
from googletrans import Translator

banco_dados = {'Alunos': {},
               'Visitantes': {},
               'Restaurantes': {},
               'Funcionario_Depae': {}}


class Usuario(ABC):
    def __init__(self, nome, email, senha, n_telefone, cpf):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__n_telefone = n_telefone
        self.__cpf = cpf

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def logar(self):
        pass

    # get
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_n_telefone(self):
        return self.__n_telefone

    def get_cpf(self):
        return self.__cpf

    # set
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        self.__senha = senha

    def set_n_telefone(self, n_telefone):
        self.__n_telefone = n_telefone

    def set_cpf(self, cpf):
        self.__cpf = cpf


# Aluno-----------------------------------------------------------------------------------------
class Aluno(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, curso, turma, matricula, dias_contraturno):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__curso = curso
        self.__turma = turma
        self.__matricula = matricula
        self.__ficha = None  # Ficha associada ao Aluno
        self.__dias_contraturno = dias_contraturno.split(" ")
        self.dias_nome_week = []

    # associação
    def associar_ficha(self, ficha):
        if isinstance(ficha, Ficha):
            self.__ficha = ficha
            print(f'Ficha número {ficha.get_numero()} associada ao aluno {self.get_nome()}.')
    # get

    def get_ficha(self):
        return self.__ficha

    def get_curso(self):
        return self.__curso

    def get_turma(self):
        return self.__turma

    def get_matricula(self):
        return self.__matricula

    def get_dias_contraturno(self):
        return self.__dias_contraturno

    # set
    def set_curso(self, curso):
        self.__curso = curso

    def set_turma(self, turma):
        self.__turma = turma

    def set_matricula(self, matricula):
        self.__matricula = matricula


    # cadastro
    def cadastrar(self):
        if self.__matricula in banco_dados["Alunos"]:
            print('Aluno já cadastrado.')

        else:
            banco_dados['Alunos'][self.__matricula] = self
            print(f'\033[32mAluno {banco_dados["Alunos"][self.__matricula].get_nome()} cadastrado com sucesso.\033[m')

    # login
    def logar(self):

        if self.get_matricula() in banco_dados['Alunos'] and self.get_senha() == banco_dados['Alunos'][self.__matricula].get_senha():
            print(f'\033[32mAluno {banco_dados["Alunos"][self.__matricula].get_nome()} logado com sucesso!\033[m\n')
            objeto = banco_dados["Alunos"][self.__matricula]
            objeto.almoco_gratis()
            return True
        else:
            return False


    def dias_semana(self):

        for q in self.__dias_contraturno:

            if q == "2":
                self.dias_nome_week.append('Segunda-feira')
            if q == "3":
                self.dias_nome_week.append('Terça-feira')
            if q == "4":
                self.dias_nome_week.append('Quarta-feira')
            if q == "5":
                self.dias_nome_week.append('Quinta-feira')
            if q == "6":
                self.dias_nome_week.append('Sexta-feira')

    def almoco_gratis(self):
       
    
        eu_almoco_hj = False
        self.dias_semana()
        data_atual = datetime.datetime.now()
        data_semana_numero = int(data_atual.weekday())+2
        dia_semana = data_atual.strftime('%A')

        tradutor = Translator()
        dia_semana_traduzido = tradutor.translate(dia_semana, dest='pt', src='en')

        if str(data_semana_numero) in self.__dias_contraturno:
            eu_almoco_hj = True
            print(f"Seus dias de almoço são: {self.dias_nome_week}. Hoje é {dia_semana_traduzido.text}, \033[32mportanto você tem almoço grátis.\033[m")
            return eu_almoco_hj

        else:

            print(f"Seus dias de almoço são: {self.dias_nome_week}. Hoje é {dia_semana_traduzido.text}, \033[32mportanto você não tem almoço grátis.\033[m")
            return eu_almoco_hj
 





# Visitantes-----------------------------------------------------------------------------------------------------

class Visitantes(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf):
        super().__init__(nome, email, senha, n_telefone, cpf)

    # Cadastro
    def cadastrar(self):
        if self.get_cpf() in banco_dados["Visitantes"]:
            print('Visitante já cadastrado.')

        else:
            banco_dados['Visitantes'][self.get_cpf()] = self
            print(f'\033[32mVisitante {banco_dados["Visitantes"][self.get_cpf()].get_nome()} cadastrado com sucesso.\033[m')

        # login

    def logar(self):
        logado = False
        if self.get_cpf() in banco_dados['Visitantes'] and self.get_senha() == \
                banco_dados['Visitantes'][self.get_cpf()].get_senha():
            print(f'\033[32mVisitante {banco_dados["Visitantes"][self.get_cpf()].get_nome()} logado com sucesso!\033[m\n')
            logado = True
            return logado
        else:
            return logado


# Restaurante-----------------------------------------------------------------------------------------------------

class Restaurante(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, cnpj, nomeEmpresa):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__cnpj = cnpj
        self.__nomeEmpresa = nomeEmpresa

    # get
    def get_cnpj(self):
        return self.__cnpj

    def get_nomeEmpresa(self):
        return self.__nomeEmpresa

    # set
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def set_nomeEmpresa(self, nomeEmpresa):
        self.__nomeEmpresa = nomeEmpresa

    # Cadastro
    def cadastrar(self):
        if self.get_cnpj() in banco_dados["Restaurantes"]:
            print('Restaurante já cadastrado.')

        else:
            banco_dados['Restaurantes'][self.get_cnpj()] = self
            print(
                f'\033[32mTitular do restaurante {banco_dados["Restaurantes"][self.get_cnpj()].get_nome()} cadastrado com sucesso.\033[m')

    # login
    def logar(self):
        logado = False
        if self.get_cnpj() in banco_dados['Restaurantes'] and self.get_senha() == \
                banco_dados['Restaurantes'][self.get_cnpj()].get_senha():
            print(
                f'\033[32mTitular do restaurante {banco_dados["Restaurantes"][self.get_cnpj()].get_nome()} logado com sucesso!\033[m\n')
            logado = True
            return logado
        else:
            return logado





# Funcionário Depae-----------------------------------------------------------------------------------------------------

class Func_Depae(Usuario):
    def __init__(self, nome, email, senha, n_telefone, cpf, siape):
        super().__init__(nome, email, senha, n_telefone, cpf)

        self.__siape = siape

    # get
    def get_siape(self):
        return self.__siape

    # set
    def set_siape(self, siape):
        self.__siape = siape

    # Cadastro
    def cadastrar(self):
        if self.get_siape() in banco_dados["Funcionario_Depae"]:
            print('Servidor do DEPAE já cadastrado.')

        else:
            banco_dados['Funcionario_Depae'][self.get_siape()] = self
            print(f'\033[32mServidor {banco_dados["Funcionario_Depae"][self.get_siape()].get_nome()} cadastrado com sucesso.\033[m')

    # login

    def logar(self):
        logado = False
        if self.get_siape() in banco_dados['Funcionario_Depae'] and self.get_senha() == \
                banco_dados['Funcionario_Depae'][self.get_siape()].get_senha():
            print(f'\033[32mServidor {banco_dados["Funcionario_Depae"][self.get_siape()].get_nome()} logado com sucesso!\033[m\n')
            logado = True
            return logado
        else:
            return logado





# -----------------------------------------------------------------------------------------------------

class Fila:
    def __init__(self, nome):
        self.__nome = nome
        self.__fichas = []  # Lista para armazenar as fichas na fila

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.__nome = nome

#agregação de ficha
    def adicionar_ficha(self, ficha):
        if isinstance(ficha, Ficha):
            self.__fichas.append(ficha)
            print(f'Ficha número {ficha.get_numero()} (Nome: {ficha.get_nome()}) adicionada à fila {self.__nome}.')
        else:
            print("Sua ficha não foi adicionada à fila :/ ")

    def senha(self):
        numero_senha = len(self.__fichas)
        return numero_senha

    def tempo_atendimento(self):
        minutos= len(self.__fichas)*2
        return minutos




#não sei se é correto adicionar isso
    def listar_fichas(self):
        return self.__fichas


#classe GerenciarFila que agrega a fila=======================================================================================
class GerenciarFila:
    def __init__(self, NomePessoas):
        self.__NomePessoas = NomePessoas  # Agregação: GerenciarFila contém uma referência a um objeto Fila

    def getNomePessoas(self):
        return self.NomePessoas

    def set_NomePessoas(self, NomePessoas):
        self.__NomePessoas = NomePessoas

    def exibir_nomes_pessoas(self):
        fichas = self.__NomePessoas.listar_fichas()  # Obtém as fichas na fila
        if fichas:
            print(f'Nomes das pessoas na fila {self.__fila.get_nome()}:') #talvez seja __nomepessoas
            for ficha in fichas:
                print(ficha.get_nome())
        else:
            print(f'A fila {self.__fila.get_nome()} está vazia.')

    def obter_nomes_pessoas(self):
        return [ficha.getNome() for ficha in self.__fila.listar_fichas()]

#---------------------------------------------------------------------------------------------------------------------

#classe almocogratis///////////////////////////////////////////////////////////////
class AlmocoGratis:
    def __init__(self, objeto_aluno_nome_e_contraturno):
        self.ListaAlunos = {}

        global nome_aluno
        global dias_contraturno

        #Aqui começa o relacionamento de COMPOSIÇÃO entre Aluno e AlmocoGratis

        if objeto_aluno_nome_e_contraturno.get_matricula() in banco_dados['Alunos']: #Aqui ele usa o nº de matricula do objeto (aluno_objeto) criado na interface para relacionar o respectivo objeto no banco de dados (adicionado no cadastro)
                                                                                        #Feito isso, ele extrai todas a informação necessária do objeto (que está no dicionário) identidicado pelo nº de matrícula (chave padrão do dicionário}
                                                                                        #OBS: aluno_objeto (presente no arq. main, na parte do login) é um objeto criado apenas para identificação do real objeto Aluno adicionado (no momento do cadastro) no banco de dados (dicionário)
            nome_aluno = banco_dados['Alunos'][objeto_aluno_nome_e_contraturno.get_matricula()].get_nome()


        if objeto_aluno_nome_e_contraturno.get_matricula() in banco_dados['Alunos']:
            dias_contraturno = banco_dados['Alunos'][objeto_aluno_nome_e_contraturno.get_matricula()].get_dias_contraturno()


        self.ListaAlunos[nome_aluno] = []
        for q in dias_contraturno:
            self.ListaAlunos[nome_aluno].append(q)
        #terminou o relacionamento


    def getListaAlunos(self):
        return self.ListaAlunos


    def exibir_almoco(self): #vai exibir todos os alunos que têm direito a almoço grátis hoje
        alunos_q_tem_almoco_gratis_hj = []
        dia_hj = datetime.datetime.now()
        dia_semana = int(dia_hj.weekday())+2

        for chave, valores in self.ListaAlunos.items():
            if str(dia_semana) in valores:
                alunos_q_tem_almoco_gratis_hj.append(chave)

        print('Os Alunos que têm direito a almoço grátis hoje são: ')
        return alunos_q_tem_almoco_gratis_hj


#classe ficha////////////////////////////////////////////////////////////////////////
class Ficha:
    def __init__(self,numero,nome):
        self.__nome = nome
        self.__numero = numero

    def getNome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero


#classe Fila///////////////////////////////////////////////////////////////
class Fila:
    def __init__(self, nome):
        self.__nome = nome
        self.__fichas = []  # Lista para armazenar as fichas na fila

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.__nome = nome

#agregação de ficha
    def adicionar_ficha(self, aluno):
        ficha = aluno.get_ficha()
        if ficha and ficha not in self.fichas:
            self.__fichas.append(ficha)
            print(f'Aluno {aluno.get_nome()} entrou na fila com a ficha número {ficha.get_numero()}.')
        elif not ficha:
            print(f'O aluno {aluno.get_nome()} não possui uma ficha associada')
        else:
            print(f'O aluno {aluno.get_nome()} já está na fila.')

    def listar_fichas(self):
        return self.__fichas


#classe GerenciarFila que agrega a fila/////////////////////////////////////////////////////////////////////////
class GerenciarFila:
    def __init__(self, NomePessoas):
        self.__NomePessoas = None # Agregação: GerenciarFila contém uma referência a um objeto Fila

    def getNomePessoas(self):
        return self.NomePessoas

    def set_NomePessoas(self, NomePessoas):
        self.__NomePessoas = NomePessoas

    def exibir_nomes_pessoas(self):
        fichas = self.__NomePessoas.listar_fichas()  # Obtém as fichas na fila
        if fichas:
            print(f'Nomes das pessoas na fila {self.__fila.get_nome()}:') #talvez seja __nomepessoas
            for ficha in fichas:
                print(ficha.get_nome())
        else:
            print(f'A fila {self.__fila.get_nome()} está vazia.')

    def obter_nomes_pessoas(self):
        return [ficha.getNome() for ficha in self.__fila.listar_fichas()]
        time.sleep(3)
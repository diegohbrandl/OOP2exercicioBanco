import abc

class Double:
    def __init__(self):
        self.valor = 0.0
    
    def getValor(self):
        return 0.0

    def setValor(self, valor):
        self.valor = valor

class Transacao:
    def __init__(self):
        self.gerenciadorDeTransacoes = GerenciadorDeTransacoes()
        self.contas = [2]

    def processaTransacao(self, Double, valor):
        pass
    
    def getValor(self):
        double = Double()
        return double.getValor

    def getGerenciadorDeTransacoes(self):
        return self.gerenciadorDeTransacoes

    def setGerenciadorDeTransacoes(self, gerenciadorDeTransacoes):
        self.gerenciadorDeTransacoes = gerenciadorDeTransacoes
    
    def getConta(self):
        return self.conta
    
    def setConta(self, conta):
        self.conta = conta

class Transferir:
    def __init__(self):
        self.transacao = Transacao()
    
    def getTransacao(self):
        return self.transacao
    
    def setTransacao(self, transacao):
        self.transacao = transacao

class Sacar:
    def __init__(self):
        self.transacao = Transacao()

    def getTransacao(self):
        return self.transacao
    
    def setTransacao(self, transacao):
        self.transacao = transacao

class Conta (abc.ABC):

    def __init__(self):
        self.gerenciadorDeContas = GerenciadorDeContas()
        self.transacao = Transacao()
        self.saldo = 0.0
    
    @abc.abstractmethod
    def atualizar(self):
        pass
    
    def getGerenciadorDeContas(self):
        return self.gerenciadorDeContas
    
    def setGerenciadorDeContas(self, gerenciadorDeContas):
        self.gerenciadorDeContas = gerenciadorDeContas

    def getTransacao(self):
        return self.transacao

    def setTransacao(self, transacao):
        self.trasacao = transacao

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

class Poupanca (Conta):
    def __init__(self):
        self.cliente = Cliente()
    
    def getCliente(self):
        return self.cliente
    
    def setCliente(self):
        self.cliente = Cliente

class ContaCorrente (Conta):
    def __init__(self):
        self.cliente = Cliente()
    
    def getCliente(self):
        return self.cliente
    
    def setCliente(self):
        self.cliente = Cliente

class Cliente:
    def __init__(self):
        self.poupanca = Poupanca()
        self.contaCorrente = ContaCorrente()
        self.gerenciadorDeTransacoes = GerenciadorDeTransacoes()
        self.gerenciadorDeClientes = GerenciadorDeClientes()
        self.nome = ''
        self.endereco = ''

    def sacar(self, Conta):
        pass

    def transferir(self, Conta):
        pass
    
    def getPoupanca(self):
        return self.poupanca

    def setPoupanca(self, poupanca):
        self.poupanca = poupanca

    def getContaCorrente(self):
        return self.contaCorrente
    
    def setContaCorrente(self, contaCorrente):
        self.contaCorrente = contaCorrente

    def getGerenciadorDeTransacoes(self):
        return self.gerenciadorDeTransacoes

    def setGerenciadorDeTransacoes(self, gerenciadorDeTransacoes):
        self.gerenciadorDeTransacoes = gerenciadorDeTransacoes
    
    def getGerenciadorDeClientes(self):
        return self.gerenciadorDeClientes
    
    def setGerenciadorDeClientes(self, gerenciadorDeClientes):
        self.gerenciadorDeClientes = gerenciadorDeClientes
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

class GerenciadorDeTransacoes:
        def __init__(self):
            self.vetorDeTransacoesEmExecucao = []
            self.vetorDeTransacoesEsperando = []
            self.cliente = Cliente()
            self.transacoes = []
        
        def efetuarTransacoes(self):
            pass

        def getEstatisticas(self):
            return False

        def getStatus(self):
            return False
        
        def getVetorDeTransacoesEmExecucao(self):
            return self.vetorDeTransacoesEmExecucao

        def setVetorDeTransacoesEmExecucao(self, vetorDeTransacoesEmExecucao):
            self.vetorDeTransacoesEmExecucao = vetorDeTransacoesEmExecucao

        def getVetorDeTransacoesEsperando(self):
            return self.vetorDeTransacoesEsperando

        def setVetorDeTransacoesEsperando(self, vetorDeTransacoesEsperando):
            self.vetorDeTransacoesEsperando = vetorDeTransacoesEsperando

        def getCliente(self):
            return self.cliente
        
        def setCliente(self, cliente):
            self.cliente = cliente

class GerenciadorDeContas:
    def __init__(self) :
        self.contas = []

    def adicionar(self):
        pass

    def remover(self):
        pass

    def atualizarConta(self):
        pass
    
    def getContas(self):
        return self.contas
    
    def setContas(self, contas):
        self.contas = contas

class GerenciadorDeClientes:
    def __init__(self):
        clientes = []

    def adicionar(self):
        pass

    def remover(self):
        pass   
    
    def getClientes(self):
        return self.clientes
    
    def setClientes(self, clientes):
        self.clientes = clientes

class Banco:
    def __init__(self):
        self.gerenciadorDeTransacoes = GerenciadorDeTransacoes()
        self.gerenciadordeContas = GerenciadorDeContas()
        self.gerenciadorDeClientes = GerenciadorDeClientes()
        self.nome = ''
        self.endereco = ''
    
    def atualizarConta(self):
        pass

    def getGerenciadorDeTransacoes(self):
        return self.gerenciadorDeTransacoes

    def setGerenciadorDeTransacoes(self, gerenciadorDeTransacoes):
        self.gerenciadorDeTransacoes = gerenciadorDeTransacoes
    
    def getGerenciadorDeContas(self):
        return self.gerenciadordeContas

    def setGerenciadorDeContas(self, gerenciadorDeContas):
        self.gerenciadordeContas = gerenciadorDeContas
    
    def getGerenciadorDeClientes(self):
        return self.gerenciadorDeClientes
    
    def setGerenciadorDeClientes(self, gerenciadorDeClientes):
        self.gerenciadorDeClientes = gerenciadorDeClientes

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

class Calendario:
    def __init__(self):
        self.diasUteis = ''

    def ehDiaUtil(self):
        pass

    def getDiasUteis(self):
        return self.diasUteis

    def setDiasUteis(self, diasUteis):
        self.diasUteis = diasUteis



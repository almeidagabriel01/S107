from math import ceil

import pytest
from src.main.buscaHorario import buscaHorario
from src.Test.MockHorarioService import MockHorarioService


# Mockando o serviço
@pytest.fixture
def mock_servico():
    return MockHorarioService()


# Criando uma instância da classe buscaHorario
@pytest.fixture
def busca(mock_servico):
    return buscaHorario(mock_servico)


# Função auxiliar para verificar se a sala está no prédio correto
def predio_correto(sala, predio):
    try:
        sala = int(sala)
        predio = int(predio)
    except Exception as err:
        return False
    predio_certo = ceil(sala / 5)

    if (sala or predio) < 0:
        return False

    if (predio_certo or predio) == 5:
        return False

    elif predio == predio_certo:
        return True

    return False


# Testa se a sala do PaiDoConrado está no prédio correto
def test_sala_PaiDoConrado(busca):
    resultado = busca.buscaHorario(1)
    assert predio_correto(resultado[4], resultado[5]), "Sala do PaiDoConrado está no prédio errado"


# Testa se o ID retornado do Chris está correto
def test_id_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert resultado[0] == "2", "ID incorreto do Chris"


# Testa se a sala do Chris está no prédio correto
def test_sala_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Chris está no prédio errado"


# Testa se o ID retornado do Marcelo está correto
def test_id_Marcelo(busca):
    resultado = busca.buscaHorario(3)
    assert resultado[0] == "3", "ID incorreto do Marcelo"


# Testa se a sala do Marcelo está no prédio correto
def test_sala_Marcelo(busca):
    resultado = busca.buscaHorario(3)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Marcelo está no prédio errado"


# Testa se a sala da Victoria está no prédio correto
def test_sala_Victoria(busca):
    resultado = busca.buscaHorario(6)
    assert predio_correto(resultado[4], resultado[5]), "Sala da Victoria está no prédio errado"


# Testa se a sala da Alessandra está no prédio correto
def test_sala_Alessandra(busca):
    resultado = busca.buscaHorario(7)
    assert predio_correto(resultado[4], resultado[5]), "Sala da Alessandra está no prédio errado"


# Testa se a sala do Vitor está no prédio correto
def test_sala_Vitor(busca):
    resultado = busca.buscaHorario(8)
    assert predio_correto(resultado[4], resultado[5]), "Sala do Vitor está no prédio errado"


# Testa se o horário de atendimento da Alessandra está correto
def test_horario_Alessandra(busca):
    resultado = busca.buscaHorario(7)
    assert resultado[2] == "12:00 - 14:00", "Horário de atendimento da Alessandra está errado"


def test_periodo_Chris(busca):
    resultado = busca.buscaHorario(2)
    assert resultado[3] == "noturno", "Período do Chris está errado"


# testes de falha

# Testa ID inválidos
def test_id_Invalido(busca):
    resultado = busca.buscaHorario(-999)
    assert resultado[0] == "-1", "Json retornado errado"


def test_id_Tipo_Incorreto(busca):
    resultado = busca.buscaHorario("Vitor")
    assert resultado[0] == "-1", "Json retornado errado"


def test_id_Injeção(busca):
    resultado = busca.buscaHorario([1, 2])
    assert resultado[0] == "-1", "Json retornado errado"


def test_não_Cadastro(busca):
    resultado = busca.buscaHorario(15)
    assert resultado[0] == "99", "Json retornado errado"


# verifica se a funçao de conmfirmação está ok via sala inválida
def test_verificaçao(busca):
    assert (predio_correto(23, 5) == False), "Está permitindo prédio 5"


def test_sala_cadastro(busca):
    resultado = busca.buscaHorario(9)
    assert (predio_correto(resultado[4], resultado[5]) == False), "Não está detectando erros de cadastros"

def test_type_str_first(busca):
    assert (predio_correto("a", 5) == False), "está permitindo erro de str elemento 1"

def test_type_str_second(busca):
    assert (predio_correto(12, "c") == False), "está permitindo erro de str elemento 2"

def test_type_str(busca):
    assert (predio_correto(12, "c") == False), "está permitindo erro de str elementos"

def test_value_predio(busca):
    assert (predio_correto(-1, 2) == False), "está permitindo erro de str elementos"







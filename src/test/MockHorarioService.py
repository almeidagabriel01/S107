from src.main.HorarioService import HorarioService
from src.Test.HorariosJsons import HorariosJsons

class MockHorarioService(HorarioService):
    def __init__(self):
        pass

    def Procura(self, id):
        if id == 1:
            return HorariosJsons.PaiDoConrado
        elif id == 2:
            return HorariosJsons.Chris
        elif id == 3:
            return HorariosJsons.Marcelo
        elif id == 4:
            return HorariosJsons.Joao
        elif id == 5:
            return HorariosJsons.Raphael
        elif id == 6:
            return HorariosJsons.Victoria
        elif id == 7:
            return HorariosJsons.Alessandra
        elif id == 8:
            return HorariosJsons.Vitor
        elif id == 9:
            return HorariosJsons.CadastroErrado
        elif id < 0:
            return HorariosJsons.Inexistente
        else:
            return HorariosJsons.Invalido
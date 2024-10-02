from abc import ABC, abstractmethod


class HorarioService(ABC):  # classe abstrata que opera similar a uma interface em python
    @abstractmethod
    def Procura(self):
        pass
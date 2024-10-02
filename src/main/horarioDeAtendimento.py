class horarioDeAtendimento:
    def __init__(self, idProfessor, Nome, horarioDeAtendimento, Periodo, Sala, Predio):
        self.idProfessor = idProfessor
        self.Nome = Nome
        self.horarioDeAtendimento = horarioDeAtendimento
        self.Periodo = Periodo
        self.Sala = Sala
        self.Predio = Predio


    def getIdProfessor(self):
        return self.idProfessor

    def getNome(self):
        return self.Nome

    def getHorarioDeAtendimento(self):
        return self.horarioDeAtendimento

    def getPeriodo(self):
        return self.Periodo

    def getSala(self):
        return self.Sala

    def getPredio(self):
        return self.Predio

    def setIdProfessor(self, idProfessor):
        self.idProfessor = idProfessor

    def setNome(self, Nome):
        self.Nome = Nome

    def setHorarioDeAtendimento(self, horarioDeAtendimento):
        self.horarioDeAtendimento = horarioDeAtendimento

    def setPeriodo(self, Periodo):
        self.Periodo = Periodo

    def setSala(self, Sala):
        self.Sala = Sala

    def setPredio(self, Predio):
        self.Predio = Predio
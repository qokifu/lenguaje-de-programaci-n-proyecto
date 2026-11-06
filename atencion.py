class Atencion:
    def __init__(self, codigo, cita, diagnostico, tratamiento):
        self._codigo = codigo
        self._cita = cita
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento

# getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def cita(self):
        return self._cita

    @property
    def diagnostico(self):
        return self._diagnostico

    @property
    def tratamiento(self):
        return self._tratamiento

# setters

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @cita.setter
    def cita(self, valor):
        self._cita = valor

    @diagnostico.setter
    def diagnostico(self, valor):
        self._diagnostico = valor

    @tratamiento.setter
    def tratamiento(self, valor):
        self._tratamiento = valor


    def resumen(self):
        return f"{self._codigo}-{self._cita.codigo}-{self._cita.paciente.nombre}-{self._diagnostico}-{self._tratamiento}"

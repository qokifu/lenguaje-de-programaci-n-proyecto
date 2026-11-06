from datetime import datetime

from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion

pacientes = {}
medicos = {}
citas = {}
historial = []


### VALIDACIONES!! IMPORTANTE NO BORRAR
def pedir_codigo_nuevo(mensaje, codigos_usados):
    while True:
        codigo = input(mensaje).strip().upper()
        if codigo == "":
            print("error: el código no puede estar vacío")
        elif codigo in codigos_usados:
            print("error: ese código ya existe")
        else:
            return codigo


def pedir_codigo_existente(mensaje, registrados):
    while True:
        codigo = input(mensaje).strip().upper()
        if codigo in registrados:
            return codigo
        print("error: ese código no está registrado")


def pedir_letras(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.replace(" ", "").isalpha():
            return texto
        print("error: solo se permiten letras y espacios")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("error: no puede estar vacío")


def pedir_edad():
    while True:
        try:
            edad = int(input("edad: "))
            if 0 <= edad <= 120:
                return edad
            print("error: la edad debe estar entre 0 y 120")
        except ValueError:
            print("error: la edad debe ser un número entero")


def pedir_fecha():
    while True:
        fecha = input("fecha (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("error: la fecha no es válida, usa el formato dd/mm/aaaa")


### MENÚ

def registrar_paciente():
    codigo = pedir_codigo_nuevo("código del paciente: ", pacientes)
    nombre = pedir_letras("nombre: ")
    edad = pedir_edad()
    pacientes[codigo] = Paciente(codigo, nombre, edad)
    print("paciente registrado:", pacientes[codigo].resumen())


def registrar_medico():
    codigo = pedir_codigo_nuevo("código del médico: ", medicos)
    nombre = pedir_letras("nombre: ")
    especialidad = pedir_letras("especialidad: ")
    medicos[codigo] = Medico(codigo, nombre, especialidad)
    print("médico registrado:", medicos[codigo].resumen())


def buscar_por_codigo():
    while True:
        tipo = input("buscar paciente (p) o médico (m): ").strip().lower()
        if tipo in ("p", "m"):
            break
        print("error: escribe p o m")
    registrados = pacientes if tipo == "p" else medicos
    if not registrados:
        print("todavía no hay registros de ese tipo")
        return
    codigo = pedir_codigo_existente("código: ", registrados)
    print(registrados[codigo].resumen())


def programar_cita():
    if not pacientes or not medicos:
        print("primero registra al menos un paciente y un médico")
        return
    codigo = pedir_codigo_nuevo("código de la cita: ", citas)
    codigo_paciente = pedir_codigo_existente("código del paciente: ", pacientes)
    codigo_medico = pedir_codigo_existente("código del médico: ", medicos)
    fecha = pedir_fecha()
    citas[codigo] = Cita(codigo, pacientes[codigo_paciente], medicos[codigo_medico], fecha)
    print("cita programada:", citas[codigo].resumen())


def registrar_atencion():
    if not citas:
        print("primero programa al menos una cita")
        return
    codigos_usados = [atencion.codigo for atencion in historial]
    codigo = pedir_codigo_nuevo("código de la atención: ", codigos_usados)
    codigo_cita = pedir_codigo_existente("código de la cita: ", citas)
    diagnostico = pedir_texto("diagnóstico: ")
    tratamiento = pedir_texto("tratamiento: ")
    atencion = Atencion(codigo, citas[codigo_cita], diagnostico, tratamiento)
    historial.append(atencion)
    print("atención registrada:", atencion.resumen())


def filtrar_medicos():
    especialidad = pedir_letras("especialidad: ").lower()
    # filter: crea una lista nueva solo con los médicos de esa especialidad
    encontrados = list(filter(lambda m: m.especialidad.lower() == especialidad,
                              medicos.values()))
    if not encontrados:
        print("no hay médicos con esa especialidad")
    for medico in encontrados:
        print(medico.resumen())


def ver_historial():
    if not historial:
        print("el historial está vacío")
        return
    # map: convierte cada atención en su texto resumen
    for linea in map(lambda a: a.resumen(), historial):
        print(linea)


OPCIONES = {
    "1": ("registrar paciente", registrar_paciente),
    "2": ("registrar médico", registrar_medico),
    "3": ("buscar por código", buscar_por_codigo),
    "4": ("programar cita", programar_cita),
    "5": ("registrar atención", registrar_atencion),
    "6": ("filtrar médicos por especialidad", filtrar_medicos),
    "7": ("ver historial", ver_historial),
}


def main():
    while True:
        print("\n--- kawsay ---")
        for numero, (texto, _) in OPCIONES.items():
            print(f"{numero}. {texto}")
        print("0. salir")
        eleccion = input("elige una opción: ").strip()
        if eleccion == "0":
            print("hasta pronto")
            break
        if eleccion in OPCIONES:
            OPCIONES[eleccion][1]()
        else:
            print("opción no válida")


if __name__ == "__main__":
    main()

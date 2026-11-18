import json
import csv
import os


# ==========================================================
# CLASE PUNTO 1: GESTIÓN DE CUENTAS BANCARIAS
# ==========================================================
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, tipo_cuenta, saldo=0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = float(saldo) if saldo else 0.0

    def to_dict(self):
        return {
            "Titular": self.titular,
            "NumeroCuenta": self.numero_cuenta,
            "TipoCuenta": self.tipo_cuenta,
            "Saldo": self.saldo
        }

    @classmethod
    def obtener_ruta_db(cls):
        ruta_backend = os.path.dirname(os.path.abspath(__file__))
        ruta_raiz = os.path.dirname(ruta_backend)
        return os.path.join(ruta_raiz, 'DataBase', 'DataBase')

    def guardar(self):
        ruta_db = self.obtener_ruta_db()
        os.makedirs(ruta_db, exist_ok=True)

        cuentas = self.leer_todas()
        cuentas.append(self.to_dict())
        self.reescribir_base_datos(cuentas)

    @classmethod
    def leer_todas(cls):
        ruta_json = os.path.join(cls.obtener_ruta_db(), 'cuentas.json')
        if not os.path.exists(ruta_json):
            return []
        with open(ruta_json, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @classmethod
    def reescribir_base_datos(cls, lista_cuentas):
        ruta_db = cls.obtener_ruta_db()
        ruta_json = os.path.join(ruta_db, 'cuentas.json')
        ruta_csv = os.path.join(ruta_db, 'cuentas.csv')

        with open(ruta_json, 'w', encoding='utf-8') as f:
            json.dump(lista_cuentas, f, indent=4)

        if len(lista_cuentas) > 0:
            with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
                campos = ["Titular", "NumeroCuenta", "TipoCuenta", "Saldo"]
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(lista_cuentas)

    @classmethod
    def realizar_operacion(cls, num_cuenta, tipo_op, valor=0.0):
        lista = cls.leer_todas()
        for cuenta in lista:
            if cuenta["NumeroCuenta"] == num_cuenta:
                if tipo_op == "Consultar":
                    return True, f"Saldo actual de la cuenta: ${cuenta['Saldo']:.2f}"

                elif tipo_op == "Imprimir":
                    info = f"Titular: {cuenta['Titular']} | No. Cuenta: {cuenta['NumeroCuenta']} | Tipo: {cuenta['TipoCuenta']} | Saldo actual: ${cuenta['Saldo']:.2f}"
                    print(info)  # Se imprime por consola estándar
                    return True, info  # Se retorna también para mostrarlo en el FrontEnd

                elif tipo_op == "Consignar":
                    cuenta["Saldo"] = float(cuenta["Saldo"]) + valor
                    cls.reescribir_base_datos(lista)
                    return True, f"Consignación exitosa. Nuevo saldo: ${cuenta['Saldo']:.2f}"

                elif tipo_op == "Retirar":
                    if valor > float(cuenta["Saldo"]):
                        return False, "Error: Fondos insuficientes. No puede retirar un valor mayor a su saldo actual."
                    cuenta["Saldo"] = float(cuenta["Saldo"]) - valor
                    cls.reescribir_base_datos(lista)
                    return True, f"Retiro exitoso. Nuevo saldo: ${cuenta['Saldo']:.2f}"

        return False, "Error: El número de cuenta ingresado no existe."


# ==========================================================
# CLASE PUNTO 2: PACIENTES CLÍNICA VETERINARIA PETCARE
# ==========================================================
class Mascota:
    def __init__(self, nombre, valor_consulta, tipo_animal, id_propietario, estado_salud, peso, es_vip):
        self.nombre = nombre
        self.valor_consulta = float(valor_consulta)
        self.tipo_animal = tipo_animal
        self.id_propietario = id_propietario

        # REQUERIMIENTO: Almacenamiento obligatorio en un arreglo de 3 elementos
        # [0]: Estado de salud, [1]: Peso en kg, [2]: Pertenece a club VIP (Booleano)
        self.evaluacion = [estado_salud, float(peso), bool(es_vip)]

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "ValorConsulta": self.valor_consulta,
            "TipoAnimal": self.tipo_animal,
            "IdPropietario": self.id_propietario,
            "Evaluacion_Inicial": {
                "EstadoSalud": self.evaluacion[0],
                "PesoKG": self.evaluacion[1],
                "ClubVIP": "Sí" if self.evaluacion[2] else "No"
            }
        }

    def guardar(self):
        ruta_db = CuentaBancaria.obtener_ruta_db()
        os.makedirs(ruta_db, exist_ok=True)

        mascotas = self.leer_todas()
        mascotas.append(self.to_dict())
        self.reescribir_base_datos(mascotas)

    @classmethod
    def leer_todas(cls):
        ruta_json = os.path.join(CuentaBancaria.obtener_ruta_db(), 'mascotas.json')
        if not os.path.exists(ruta_json):
            return []
        with open(ruta_json, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @classmethod
    def reescribir_base_datos(cls, lista_mascotas):
        ruta_db = CuentaBancaria.obtener_ruta_db()
        ruta_json = os.path.join(ruta_db, 'mascotas.json')
        ruta_csv = os.path.join(ruta_db, 'mascotas.csv')

        with open(ruta_json, 'w', encoding='utf-8') as f:
            json.dump(lista_mascotas, f, indent=4)

        if len(lista_mascotas) > 0:
            with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["Nombre", "ValorConsulta", "TipoAnimal", "IdPropietario", "EstadoSalud", "PesoKG", "ClubVIP"])
                for m in lista_mascotas:
                    writer.writerow([
                        m["Nombre"], m["ValorConsulta"], m["TipoAnimal"], m["IdPropietario"],
                        m["Evaluacion_Inicial"]["EstadoSalud"], m["Evaluacion_Inicial"]["PesoKG"],
                        m["Evaluacion_Inicial"]["ClubVIP"]
                    ])

    @classmethod
    def buscar_y_calcular_plan(cls, nombre_mascota, duracion_plan):
        lista = cls.leer_todas()
        for m in lista:
            if m["Nombre"].lower() == nombre_mascota.lower():
                val_base = float(m["ValorConsulta"])
                es_vip = m["Evaluacion_Inicial"]["ClubVIP"] == "Sí"

                descuento = 0.0
                # Cálculo de descuentos según parámetros de PetCare
                if duracion_plan == "Mensual":
                    if es_vip:
                        descuento = 0.10  # Solo club VIP: 10%
                elif duracion_plan == "Semestral":
                    descuento = 0.10  # Plan semestral base: 10%
                    if es_vip:
                        descuento += 0.20  # Más otro 20% si es VIP (30% total)
                elif duracion_plan == "Anual":
                    descuento = 0.30  # Plan anual base: 30%
                    if es_vip:
                        descuento += 0.20  # Más otro 20% si es VIP (50% total)

                total_pagar = val_base * (1.0 - descuento)
                info_p = f"Paciente: {m['Nombre']} ({m['TipoAnimal']}) | Peso: {m['Evaluacion_Inicial']['PesoKG']}kg | VIP: {m['Evaluacion_Inicial']['ClubVIP']}"
                costo_p = f"Costo Base: ${val_base:.2f} | Desc. Aplicado: {int(descuento * 100)}%\nTotal Neto del Plan: ${total_pagar:.2f}"
                return True, info_p, costo_p

        return False, "Error: La mascota indicada no se encuentra inscrita.", ""
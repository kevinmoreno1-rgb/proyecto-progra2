import tkinter as tk
from BackEnd.Format import CuentaBancaria, Mascota


# ==========================================
# MENÚ RAÍZ CENTRAL
# ==========================================
class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Multi-Sistemas Corporativos')
        self.ventana.geometry('450x240')
        self.ventana.resizable(False, False)

        self.titulo = tk.Label(self.ventana, text='Seleccione el Sistema',
                               font=('Times New Roman', 18, 'bold underline'), fg="#333333")
        self.titulo.place(relx=0.5, y=30, anchor='center')

        self.btn_banco = tk.Button(self.ventana, text='1. ENTIDAD FINANCIERA', font=('Times New Roman', 11, 'bold'),
                                   width=28, height=2, bg="#e1f5fe", command=self.ir_banco)
        self.btn_banco.place(relx=0.5, y=100, anchor='center')

        self.btn_petcare = tk.Button(self.ventana, text='2. CLÍNICA VETERINARIA PETCARE',
                                     font=('Times New Roman', 11, 'bold'), width=28, height=2, bg="#e8f5e9",
                                     command=self.ir_petcare)
        self.btn_petcare.place(relx=0.5, y=165, anchor='center')

        self.ventana.mainloop()

    def ir_banco(self): self.ventana.destroy(); MenuBanco()

    def ir_petcare(self): self.ventana.destroy(); MenuPetCare()


# ==========================================================
# INTERFAZ ASOCIADA AL PUNTO 1 (SISTEMA BANCARIO)
# ==========================================================
class MenuBanco:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Banco - Panel Principal')
        self.ventana.geometry('400x250')

        tk.Label(self.ventana, text='Gestión de Clientes y Cuentas',
                 font=('Times New Roman', 16, 'bold underline')).place(relx=0.5, y=25, anchor='center')

        tk.Button(self.ventana, text='Registrar Nueva Cuenta', font=('Times New Roman', 10), width=25,
                  command=self.crear).place(relx=0.5, y=85, anchor='center')
        tk.Button(self.ventana, text='Panel de Transacciones', font=('Times New Roman', 10), width=25,
                  command=self.operaciones).place(relx=0.5, y=135, anchor='center')
        tk.Button(self.ventana, text='Volver al Selector Central', font=('Times New Roman', 10), width=25, bg="#f5f5f5",
                  command=self.volver).place(relx=0.5, y=185, anchor='center')

        self.ventana.mainloop()

    def crear(self): self.ventana.destroy(); VentanaCrearCuenta()

    def operaciones(self): self.ventana.destroy(); VentanaOperacionesBanco()

    def volver(self): self.ventana.destroy(); VentanaPrincipal()


class VentanaCrearCuenta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Banco - Registro')
        self.ventana.geometry('500x310')

        tk.Label(self.ventana, text='Plantilla de Registro de Cuenta',
                 font=('Times New Roman', 14, 'bold underline')).place(relx=0.5, y=15, anchor='center')

        tk.Label(self.ventana, text='Nombres y Apellidos Titular:', font=('Times New Roman', 10)).place(x=25, y=60)
        self.txt_titular = tk.Entry(self.ventana, width=28);
        self.txt_titular.place(x=220, y=60)

        tk.Label(self.ventana, text='Número Cuenta Bancaria:', font=('Times New Roman', 10)).place(x=25, y=100)
        self.txt_numero = tk.Entry(self.ventana, width=28);
        self.txt_numero.place(x=220, y=100)

        tk.Label(self.ventana, text='Tipo Cuenta (Ahorros / Corriente):', font=('Times New Roman', 10)).place(x=25,
                                                                                                              y=140)
        self.txt_tipo = tk.Entry(self.ventana, width=28);
        self.txt_tipo.place(x=220, y=140)

        tk.Label(self.ventana, text='Saldo de Cuenta (Opcional):', font=('Times New Roman', 10)).place(x=25, y=180)
        self.txt_saldo = tk.Entry(self.ventana, width=28);
        self.txt_saldo.place(x=220, y=180)

        self.invisible = tk.Label(self.ventana, text='', font=('Times New Roman', 10, 'italic'))
        self.invisible.place(relx=0.5, y=225, anchor='center')

        tk.Button(self.ventana, text='Registrar', font=('Times New Roman', 10), width=12, command=self.registrar).place(
            x=130, y=260)
        tk.Button(self.ventana, text='Volver', font=('Times New Roman', 10), width=12, command=self.volver).place(x=260,
                                                                                                                  y=260)

        self.ventana.mainloop()

    def registrar(self):
        if not self.txt_titular.get() or not self.txt_numero.get() or not self.txt_tipo.get():
            self.invisible.config(text="Error: Complete los campos obligatorios.", fg="red")
            return

        saldo_enviado = self.txt_saldo.get() if self.txt_saldo.get() else 0.0
        nueva_cta = CuentaBancaria(self.txt_titular.get(), self.txt_numero.get(), self.txt_tipo.get(), saldo_enviado)
        nueva_cta.guardar()
        self.invisible.config(text=f"Cuenta No. {self.txt_numero.get()} creada exitosamente.", fg="green")

    def volver(self): self.ventana.destroy(); MenuBanco()


class VentanaOperacionesBanco:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Banco - Operaciones Especiales')
        self.ventana.geometry('560x340')

        tk.Label(self.ventana, text='Operaciones por Número Identificador',
                 font=('Times New Roman', 14, 'bold underline')).place(relx=0.5, y=15, anchor='center')

        tk.Label(self.ventana, text='Número Identificador de Cuenta:', font=('Times New Roman', 10, 'bold')).place(x=25,
                                                                                                                   y=60)
        self.txt_num = tk.Entry(self.ventana, width=24);
        self.txt_num.place(x=250, y=60)

        tk.Label(self.ventana, text='Monto Operación (Consignar/Retirar):', font=('Times New Roman', 10)).place(x=25,
                                                                                                                y=100)
        self.txt_monto = tk.Entry(self.ventana, width=24);
        self.txt_monto.place(x=250, y=100)

        self.lbl_respuesta = tk.Label(self.ventana, text='', font=('Times New Roman', 10, 'bold'), wraplength=500)
        self.lbl_respuesta.place(relx=0.5, y=160, anchor='center')

        # Fila de Acciones requeridas
        tk.Button(self.ventana, text='Consultar Saldo', width=15, command=lambda: self.ejecutar("Consultar")).place(
            x=35, y=210)
        tk.Button(self.ventana, text='Imprimir Info', width=15, command=lambda: self.ejecutar("Imprimir")).place(x=160,
                                                                                                                 y=210)
        tk.Button(self.ventana, text='Consignar', width=15, command=lambda: self.ejecutar("Consignar")).place(x=285,
                                                                                                              y=210)
        tk.Button(self.ventana, text='Retirar', width=15, command=lambda: self.ejecutar("Retirar")).place(x=410, y=210)

        tk.Button(self.ventana, text='Volver Atrás', width=15, command=self.volver).place(relx=0.5, y=280,
                                                                                          anchor='center')

        self.ventana.mainloop()

    def ejecutar(self, tipo_accion):
        id_cta = self.txt_num.get()
        if not id_cta:
            self.lbl_respuesta.config(text="Por favor, digite el número identificador de la cuenta.", fg="red")
            return

        monto_decimal = 0.0
        if tipo_accion in ["Consignar", "Retirar"]:
            try:
                monto_decimal = float(self.txt_monto.get())
            except ValueError:
                self.lbl_respuesta.config(text="Error: Ingrese un monto numérico válido en decimales.", fg="red")
                return

        exito, mensaje = CuentaBancaria.realizar_operacion(id_cta, tipo_accion, monto_decimal)
        self.lbl_respuesta.config(text=mensaje, fg="green" if exito else "red")

    def volver(self):
        self.ventana.destroy(); MenuBanco()


# ==========================================================
# INTERFAZ ASOCIADA AL PUNTO 2 (CLÍNICA PETCARE)
# ==========================================================
class MenuPetCare:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('PetCare - Panel Principal')
        self.ventana.geometry('400x250')

        tk.Label(self.ventana, text='Control Clínico PetCare', font=('Times New Roman', 16, 'bold underline')).place(
            relx=0.5, y=25, anchor='center')

        tk.Button(self.ventana, text='Inscribir Mascota y Evaluación', font=('Times New Roman', 10), width=25,
                  command=self.crear).place(relx=0.5, y=85, anchor='center')
        tk.Button(self.ventana, text='Calcular Valor Total Plan', font=('Times New Roman', 10), width=25,
                  command=self.planes).place(relx=0.5, y=135, anchor='center')
        tk.Button(self.ventana, text='Volver al Selector Central', font=('Times New Roman', 10), width=25, bg="#f5f5f5",
                  command=self.volver).place(relx=0.5, y=185, anchor='center')

        self.ventana.mainloop()

    def crear(self): self.ventana.destroy(); VentanaRegistrarMascota()

    def planes(self): self.ventana.destroy(); VentanaCalcularPlan()

    def volver(self): self.ventana.destroy(); VentanaPrincipal()


class VentanaRegistrarMascota:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('PetCare - Registro e Historial')
        self.ventana.geometry('560x410')

        tk.Label(self.ventana, text='Inscripción Paciente y Evaluación Inicial',
                 font=('Times New Roman', 13, 'bold underline')).place(relx=0.5, y=15, anchor='center')

        # --- Datos básicos ---
        tk.Label(self.ventana, text='Nombre Mascota:', font=('Times New Roman', 10)).place(x=25, y=55)
        self.txt_nom = tk.Entry(self.ventana, width=20);
        self.txt_nom.place(x=145, y=55)

        tk.Label(self.ventana, text='Valor Consulta:', font=('Times New Roman', 10)).place(x=295, y=55)
        self.txt_val = tk.Entry(self.ventana, width=18);
        self.txt_val.place(x=415, y=55)

        tk.Label(self.ventana, text='Tipo Animal:', font=('Times New Roman', 10)).place(x=25, y=95)
        self.txt_tipo_a = tk.Entry(self.ventana, width=20);
        self.txt_tipo_a.place(x=145, y=95)

        tk.Label(self.ventana, text='ID Propietario:', font=('Times New Roman', 10)).place(x=295, y=95)
        self.txt_id_p = tk.Entry(self.ventana, width=18);
        self.txt_id_p.place(x=415, y=95)

        # --- Elementos de Evaluación (Se guardan en el Arreglo) ---
        tk.Label(self.ventana, text='[ Componentes de la Evaluación Médica Inicial ]',
                 font=('Times New Roman', 10, 'bold'), fg="#1b5e20").place(relx=0.5, y=145, anchor='center')

        tk.Label(self.ventana, text='Estado de Salud (bueno / regular / malo):', font=('Times New Roman', 10)).place(
            x=25, y=180)
        self.txt_estado = tk.Entry(self.ventana, width=20);
        self.txt_estado.place(x=280, y=180)

        # SLIDER (Scale) PARA EL PESO EN KILOGRAMOS
        tk.Label(self.ventana, text='Peso en Kilogramos (Deslice):', font=('Times New Roman', 10)).place(x=25, y=230)
        self.slider_peso = tk.Scale(self.ventana, from_=1, to=100, orient='horizontal', length=180)
        self.slider_peso.place(x=280, y=210)

        # CHECKBUTTON PARA CLUB VIP
        self.vip_var = tk.BooleanVar()
        self.chk_vip = tk.Checkbutton(self.ventana, text='¿El paciente pertenece al Club VIP?', variable=self.vip_var,
                                      font=('Times New Roman', 10, 'italic'))
        self.chk_vip.place(x=25, y=275)

        self.invisible = tk.Label(self.ventana, text='', font=('Times New Roman', 10, 'bold'))
        self.invisible.place(relx=0.5, y=325, anchor='center')

        tk.Button(self.ventana, text='Registrar Mascota', font=('Times New Roman', 10), width=18,
                  command=self.guardar).place(x=130, y=360)
        tk.Button(self.ventana, text='Volver', font=('Times New Roman', 10), width=18, command=self.volver).place(x=290,
                                                                                                                  y=360)

        self.ventana.mainloop()

    def guardar(self):
        if not self.txt_nom.get() or not self.txt_val.get() or not self.txt_estado.get():
            self.invisible.config(text="Error: Rellene todos los campos del expediente.", fg="red")
            return
        try:
            nueva_m = Mascota(
                self.txt_nom.get(), self.txt_val.get(), self.txt_tipo_a.get(), self.txt_id_p.get(),
                self.txt_estado.get(), self.slider_peso.get(), self.vip_var.get()
            )
            nueva_m.guardar()
            self.invisible.config(text=f"¡Mascota '{self.txt_nom.get()}' registrada exitosamente!", fg="green")
        except ValueError:
            self.invisible.config(text="Error: Verifique el campo 'Valor Consulta' (Debe ser numérico).", fg="red")

    def volver(self):
        self.ventana.destroy(); MenuPetCare()


class VentanaCalcularPlan:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('PetCare - Cotización de Planes')
        self.ventana.geometry('550x290')

        tk.Label(self.ventana, text='Cotizador de Planes de Cuidado Médico',
                 font=('Times New Roman', 14, 'bold underline')).place(relx=0.5, y=15, anchor='center')

        tk.Label(self.ventana, text='Nombre de Mascota:', font=('Times New Roman', 10, 'bold')).place(x=25, y=55)
        self.txt_buscar = tk.Entry(self.ventana, width=22);
        self.txt_buscar.place(x=180, y=55)

        tk.Label(self.ventana, text='Duración Elegida (Mensual / Semestral / Anual):',
                 font=('Times New Roman', 10)).place(x=25, y=95)
        self.txt_duracion = tk.Entry(self.ventana, width=22);
        self.txt_duracion.place(x=310, y=95)

        # Mensajes dinámicos de respuesta
        self.lbl_info = tk.Label(self.ventana, text='', font=('Times New Roman', 10, 'italic'), fg="black",
                                 wraplength=500)
        self.lbl_info.place(relx=0.5, y=145, anchor='center')

        self.lbl_total = tk.Label(self.ventana, text='', font=('Times New Roman', 11, 'bold'), fg="#1b5e20",
                                  justify="center")
        self.lbl_total.place(relx=0.5, y=190, anchor='center')

        tk.Button(self.ventana, text='Calcular Plan', width=16, command=self.calcular).place(x=130, y=240)
        tk.Button(self.ventana, text='Volver Atrás', width=16, command=self.volver).place(x=280, y=240)

        self.ventana.mainloop()

    def calcular(self):
        nom = self.txt_buscar.get()
        plan = self.txt_duracion.get()

        if not nom or not plan:
            self.lbl_info.config(text="Error: Ingrese el nombre de la mascota y la duración del plan.", fg="red")
            self.lbl_total.config(text="")
            return

        if plan not in ["Mensual", "Semestral", "Anual"]:
            self.lbl_info.config(text="Error: La duración debe ser exactamente 'Mensual', 'Semestral' o 'Anual'.",
                                 fg="red")
            self.lbl_total.config(text="")
            return

        exito, inf_str, tot_str = Mascota.buscar_y_calcular_plan(nom, plan)
        if exito:
            self.lbl_info.config(text=inf_str, fg="blue")
            self.lbl_total.config(text=tot_str, fg="#1b5e20")
        else:
            self.lbl_info.config(text=inf_str, fg="red")
            self.lbl_total.config(text="")

    def volver(self):
        self.ventana.destroy(); MenuPetCare()
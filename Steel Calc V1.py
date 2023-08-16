from tkinter import ttk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import *

# DISEÑO DE VIGAS
ventana = Tk()
ventana.geometry("595x290")
ventana.resizable(0, 0)
ventana.title("STEEL CALC V1.0")
# DISEÑO DE VIGAS SIMPLEMENTE REFORZADAS
#ventana.iconbitmap("Viga_rectangular.ico")
ventana.config(bg="white")

# MATERIAL

# TITULO - MATERIAL

lbl = Label(ventana, text="DATOS DE MATERIAL", font=('Century Gothic', 9, 'bold'), anchor="w")
lbl.place(x=25, y=10, width=135, height=25)
lbl.config(bg="white")

# DATOS DE LA VIGA

# Concreto

fclbl = Label(ventana, text="f'c", font=('Century Gothic', 10, 'bold'))
fclbl.config(bg="steel blue")
fclbl.place(x=25, y=50, width=60, height=25)

fctxt = Entry(ventana, bg="red")
fctxt.place(x=100, y=50, width=60, height=25)
fctxt.config(bg="papaya whip")

fc_unidades = Label(ventana, text="kg/cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
fc_unidades.config(bg="white")
fc_unidades.place(x=165, y=50, width=55, height=25)

# Acero

lbl2 = Label(ventana, text="fy", font=('Century Gothic', 10, 'bold'))
lbl2.config(bg="steel blue")
lbl2.place(x=25, y=90, width=60, height=25)

fytxt = Entry(ventana, bg="red")
fytxt.place(x=100, y=90, width=60, height=25)
fytxt.config(bg="papaya whip")

fy_unidades = Label(ventana, text="kg/cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
fy_unidades.config(bg="white")
fy_unidades.place(x=165, y=90, width=55, height=25)

# TITULO - GEOMETRIA

lbl = Label(ventana, text="GEOMETRIA DE LA VIGA", font=('Century Gothic', 9, 'bold'), anchor="w")
lbl.place(x=25, y=130, width=150, height=25)
lbl.config(bg="white")

# Altura

altura = Label(ventana, text="h", font=('Century Gothic', 10, 'bold'))
altura.config(bg="steel blue")
altura.place(x=25, y=170, width=60, height=25)

alturatxt = Entry(ventana, bg="red")
alturatxt.place(x=100, y=170, width=60, height=25)
alturatxt.config(bg="papaya whip")

altura_unidades = Label(ventana, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
altura_unidades.config(bg="white")
altura_unidades.place(x=165, y=170, width=45, height=25)

# Base

base = Label(ventana, text="b", font=('Century Gothic', 10, 'bold'))
base.config(bg="steel blue")
base.place(x=25, y=210, width=60, height=25)

basetxt = Entry(ventana, bg="red")
basetxt.place(x=100, y=210, width=60, height=25)
basetxt.config(bg="papaya whip")

base_unidades = Label(ventana, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
base_unidades.config(bg="white")
base_unidades.place(x=165, y=210, width=45, height=25)

# Longitud de la viga

longitud = Label(ventana, text="l", font=('Century Gothic', 10, 'bold'))
longitud.config(bg="steel blue")
longitud.place(x=25, y=250, width=60, height=25)

longitudtxt = Entry(ventana, bg="red")
longitudtxt.place(x=100, y=250, width=60, height=25)
longitudtxt.config(bg="papaya whip")

longitud_unidades = Label(ventana, text="m", anchor="w", font=('Century Gothic', 9, 'bold'))
longitud_unidades.config(bg="white")
longitud_unidades.place(x=165, y=250, width=45, height=25)

# TITULO - ACERO - PRUEBAS

lbl = Label(ventana, text="ACERO", font=('Century Gothic', 9, 'bold'), anchor="w")
lbl.place(x=235, y=10, width=135, height=25)
lbl.config(bg="white")

# Acero longitudinal

aslong = Label(ventana, text="Long.", font=('Century Gothic', 9, 'bold'))
aslong.config(bg="steel blue")
aslong.place(x=235, y=50, width=60, height=25)

aslongtxt = ttk.Combobox(state="readonly", values=['3/8"', '1/2"', '5/8"', '3/4"', '1"'])
aslongtxt.place(x=310, y=50, width=60, height=25)

# Acero - Estribos

asETB = Label(ventana, text="Estribos", font=('Century Gothic', 9, 'bold'))
asETB.config(bg="steel blue")
asETB.place(x=235, y=90, width=60, height=25)

ETBtxt = ttk.Combobox(state="readonly", values=['3/8"', '1/2"', '5/8"', '3/4"', '1"'])
ETBtxt.place(x=310, y=90, width=60, height=25)

# Numero de barras longitudinales

numero_de_barras_long = Label(ventana, text="N° Barras", font=('Century Gothic', 9, 'bold'))
numero_de_barras_long.config(bg="steel blue")
numero_de_barras_long.place(x=235, y=130, width=60, height=25)

numero_de_barras_long.txt = ttk.Combobox(state="readonly", values=[1,2, 3, 4, 5, 6, 7, 8, 9, 10])
numero_de_barras_long.txt.place(x=310, y=130, width=60, height=25)

acero_bastones = Label(ventana, text="Bastones", font=('Century Gothic', 9, 'bold'))
acero_bastones.config(bg="steel blue")
acero_bastones.place(x=235, y=170, width=60, height=25)
acero_bastones.txt = ttk.Combobox(state="readonly", values=['3/8"', '1/2"', '5/8"', '3/4"', '1"'])
acero_bastones.txt.place(x=310, y=170, width=60, height=25)

# Titulo - Momento ultimo

lbl = Label(ventana, text="M.U Y C.U", font=('Century Gothic', 9, 'bold'), anchor="w")
lbl.place(x=395, y=10, width=135, height=25)
lbl.config(bg="white")

# Momento ultimo

momento_ultimo = Label(ventana, text="Mu", font=('Century Gothic', 9, 'bold'))
momento_ultimo.config(bg="steel blue")
momento_ultimo.place(x=395, y=50, width=60, height=25)

momento_ultimo_ = Entry(ventana, bg="red")
momento_ultimo_.config(bg="papaya whip")
momento_ultimo_.place(x=470, y=50, width=60, height=25)

momento_ultimo_unidades = Label(ventana, text="Tn-m", anchor="w", font=('Century Gothic', 9, 'bold'))
momento_ultimo_unidades.config(bg="white")
momento_ultimo_unidades.place(x=535, y=50, width=45, height=25)

# Cortante sismica

cortante_sismica = Label(ventana, text="Vu", font=('Century Gothic', 9, 'bold'))
cortante_sismica.config(bg="steel blue")
cortante_sismica.place(x=395, y=90, width=60, height=25)

cortante_sismica_ = Entry(ventana)
cortante_sismica_.config(bg="papaya whip")
cortante_sismica_.place(x=470, y=90, width=60, height=25)

cortante_sismica_unidades = Label(ventana, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
cortante_sismica_unidades.config(bg="white")
cortante_sismica_unidades.place(x=535, y=90, width=45, height=25)

# Zona sismica - Titulo

z_sismica = Label(ventana, text="Zona Simica", font=('Century Gothic', 9, 'bold'))
z_sismica.config(bg="steel blue")
z_sismica.place(x=395, y=130, width=90, height=25)

# Zona sismica - Desplegable

zona_sismica_ = ttk.Combobox(state="readonly", values=["SI", "NO"])
zona_sismica_.place(x=490, y=130, width=50, height=25)

#Recubrimiento

recubrimiento = Label(ventana, text="Recubrimiento", font=('Century Gothic', 9, 'bold'))
recubrimiento.config(bg="steel blue")
recubrimiento.place(x=395, y=170,width=90, height=25)

#Recubrimiento - Entry

recubrimiento_ =Entry(ventana)
recubrimiento_.config(bg="papaya whip")
recubrimiento_.place(x=490, y=170, width=50, height=25)

#Recubrimiento - Unidades

recubrimiento_unidades = Label(ventana, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
recubrimiento_unidades.config(bg="white")
recubrimiento_unidades.place(x=545, y=170, width=45, height=25)

# Viga rectangular

class material():
    """docstring for material"""

    def __init__(self):
        super(material, self).__init__()

        self.compresion_concreto = float(fctxt.get())

        self.fluencia_acero = float(fytxt.get())

        self.recubrimiento_final=int(recubrimiento_.get())

    def beta1(self):

        if self.compresion_concreto >= 210 and self.compresion_concreto <= 280:

            b1 = 0.85
            return b1

        elif self.compresion_concreto > 280:

            b1 = (0.85 - (0.05 * (self.compresion_concreto - 280) / 70))
            return b1

    def material_error(self):
        if self.compresion_concreto<210.0  or self.fluencia_acero == "":
            messagebox.showinfo(message="Error en los datos de material")
            ventana1.destroy()
        else:
            pass


class geometria():
    """docstring for geometria"""

    def __init__(self):
        super(geometria, self).__init__()

        self.altura = float(alturatxt.get())
        self.base = float(basetxt.get())
        self.lng = float(longitudtxt.get())

    def geometry_error(self):
        if self.base <25.0 or self.altura <25.0 or self.lng <= 0.0:
            messagebox.showinfo(message="Error en la geometria de la viga")
            ventana1.destroy()
        else:
            pass


class acero():
    """docstring for acero"""

    def __init__(self):
        super(acero, self).__init__()
        self.primeraseleccion = ETBtxt.get()
        self.segundaseleccion = aslongtxt.get()
        self.terceraseleccion = acero_bastones.txt.get()
        self.cuantilla_minima = 14.1
        self.cuantilla_maxima = 0
        self.barras = int(numero_de_barras_long.txt.get())
        self.zona_sismica = zona_sismica_.get()

    def c_maxima_(self):

        if self.zona_sismica == "SI":

            self.cuantilla_maxima = 0.5
            return self.cuantilla_maxima

        else:

            self.cuantilla_maxima = 0.75
            return self.cuantilla_maxima

    def acero_error(self):

        if self.primeraseleccion and self.segundaseleccion and self.terceraseleccion == "":
            messagebox.showinfo(message="Error en la selección de acero")
            ventana1.destroy()
        else:
            pass

class momento():
    """docstring for momento"""
    def __init__(self):
        super(momento, self).__init__()
        self.m_ultimo = float(momento_ultimo_.get())

    def reduccion_flexion(self):
        fi = 0.9
        return fi
    def momento_error(self):
        if self.m_ultimo <= 0:
            messagebox.showinfo(message="Eror en el momento ultimo")
            ventana1.destroy()
        else:
            pass

        # PARA LAS CUANTILLAS Y ACEROS
class cortante():
    """docstring for momento"""
    def __init__(self):
        super(cortante, self).__init__()
        self.cortante = float(cortante_sismica_.get())
    def reduccion_corte(self):
        fi_c = 0.85
        return fi_c
    def cortante_error(self):
        if self.cortante <= 0:
            messagebox.showinfo(message="Eror la cortante ingresada")
            ventana2.destroy()
        else:
            pass

def resultado_total():
    global ventana1
    viga_material = material()
    viga_geometria = geometria()
    viga_ac = acero()
    viga_momento_ultimo = momento()
    

    '''if viga_material.compresion_concreto < 210:
        messagebox.showinfo(message="f'c menor a 210, modificar")
        ventana1.destroy()
    if viga_geometria.base < 25:
        messagebox.showinfo(message="Base de la viga es menor a 25, modificar")
        ventana1.destroy()
    if viga_momento_ultimo.m_ultimo <= 0:
        messagebox.showinfo(message="Momento ultimo incorrecto, modificar")
        ventana1.destroy()
    if 

    else:
        pass'''

    # CONTENEDOR

    ventana1 = Toplevel(ventana)
    ventana1.geometry("700x565")
    ventana1.resizable(False, False)
    ventana1.title("DISEÑO POR FLEXION")
    ventana1.config(bg="white")

    #COMPROBACIONES

    viga_material.material_error()
    viga_geometria.geometry_error()
    viga_ac.acero_error()
    viga_momento_ultimo.momento_error()

    # ventana1.iconbitmap("Viga_rectangular.ico")

    # CUANTILLA MINIMA

    # Cuantilla minima-txt

    cuantilla_minima = Label(ventana1, text="Cuantilla minima", font=('Century Gothic', 9, 'bold'))
    cuantilla_minima.place(x=25, y=10, width=135, height=25)
    cuantilla_minima.config(bg="steel blue")

    # Cuantilla-resultado-minima

    cuantilla_minima_ = Entry(ventana1, bg="red")
    cuantilla_minima_.place(x=180, y=10, width=60, height=25)
    cuantilla_minima_.config(bg="silver")

    # Calculo de la cuantilla minima

    c_minima = viga_ac.cuantilla_minima / viga_material.fluencia_acero
    c_minima = round(c_minima, 4)
    cuantilla_minima_.delete(0, 'end')
    cuantilla_minima_.insert(0, c_minima)

    # CUANTILLA BALANECADA

    # Cuantilla balanceada-txt
    cuantilla_balanceada = Label(ventana1, text="Cuantilla balanceada", font=('Century Gothic', 9, 'bold'))
    cuantilla_balanceada.place(x=25, y=50, width=135, height=25)
    cuantilla_balanceada.config(bg="steel blue")

    # Cuantilla balanceada - resultado

    cuantilla_balanceada_ = Entry(ventana1, bg="red")
    cuantilla_balanceada_.place(x=180, y=50, width=60, height=25)
    cuantilla_balanceada_.config(bg="silver")

    # Cuantilla balanceada - calculo

    balanceada = viga_material.beta1() * 0.85 * (viga_material.compresion_concreto / viga_material.fluencia_acero) * (
                6000 / (6000 + viga_material.fluencia_acero))
    balanceada = round(balanceada, 4)
    cuantilla_balanceada_.delete(0, 'end')
    cuantilla_balanceada_.insert(0, balanceada)

    # CUANTILLA MAXIMA

    # Cuantilla maxima - txt

    cuantilla_maxima = Label(ventana1, text="Cuantilla maxima", font=('Century Gothic', 9, 'bold'))
    cuantilla_maxima.place(x=25, y=90, width=135, height=25)
    cuantilla_maxima.config(bg="steel blue")

    # Cuantilla maxima - resultado

    cuantilla_maxima_ = Entry(ventana1, bg="red")
    cuantilla_maxima_.place(x=180, y=90, width=60, height=25)
    cuantilla_maxima_.config(bg="silver")

    # Cuantilla maxima - calculo

    c_maxima = viga_ac.c_maxima_() * balanceada
    c_maxima = round(c_maxima, 4)
    cuantilla_maxima_.delete(0, 'end')
    cuantilla_maxima_.insert(0, c_maxima)

    # ACERO MINIMO

    # Acero minimo - txt
    acero_minimo = Label(ventana1, text="Acero minimo", font=('Century Gothic', 9, 'bold'))
    acero_minimo.place(x=25, y=130, width=135, height=25)
    acero_minimo.config(bg="steel blue")

    # Acero minimo - resultado

    acero_minimo_ = Entry(ventana1, bg="red")
    acero_minimo_.place(x=180, y=130, width=60, height=25)
    acero_minimo_.config(bg="silver")

    acero_minimo_unidades = Label(ventana1, text="cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
    acero_minimo_unidades.config(bg="white")
    acero_minimo_unidades.place(x=245, y=130, width=45, height=25)

    # ACERO MAXIMO

    # Acero maximo - txt

    acero_maximo = Label(ventana1, text="Acero maximo", font=('Century Gothic', 9, 'bold'))
    acero_maximo.place(x=25, y=170, width=135, height=25)
    acero_maximo.config(bg="steel blue")

    # Acero maximo - resultado

    acero_maximo_ = Entry(ventana1, bg="red")
    acero_maximo_.place(x=180, y=170, width=60, height=25)
    acero_maximo_.config(bg="silver")

    acero_maximo_unidades = Label(ventana1, text="cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
    acero_maximo_unidades.config(bg="white")
    acero_maximo_unidades.place(x=245, y=170, width=45, height=25)

    # Acero maximo - calculo

    Asmax = c_maxima * viga_geometria.base * viga_geometria.altura
    Asmax = round(Asmax, 4)
    acero_maximo_.delete(0, 'end')
    acero_maximo_.insert(0, Asmax)

    # PARA LOS RESULTADOS - DISEÑO - VIGA SIMPLEMENTE REFORZADA

    # Inercia de la seccion - txt

    inercia_seccion = Label(ventana1, text="Inercia de la seccion", font=('Century Gothic', 9, 'bold'))
    inercia_seccion.place(x=25, y=210, width=135, height=25)
    inercia_seccion.config(bg="steel blue")

    # Resultado de la inercia

    inercia_seccion_ = Entry(ventana1, bg="red")
    inercia_seccion_.place(x=180, y=210, width=60, height=25)
    inercia_seccion_.config(bg="silver")

    inercia_seccion_unidades = Label(ventana1, text="cm\u2074", anchor="w", font=('Century Gothic', 9, 'bold'))
    inercia_seccion_unidades.config(bg="white")
    inercia_seccion_unidades.place(x=245, y=210, width=45, height=25)

    # Calculo de la inercia

    Ig = (viga_geometria.base * (viga_geometria.altura ** 3)) / 12
    Ig = round(Ig, 2)
    inercia_seccion_.delete(0, 'end')
    inercia_seccion_.insert(0, Ig)

    # Modulo de rotura - txt

    modulo_rotura = Label(ventana1, text="Modulo de rotura", font=('Century Gothic', 9, 'bold'))
    modulo_rotura.place(x=25, y=250, width=135, height=25)
    modulo_rotura.config(bg="steel blue")

    # Resultado del módulo de rotura

    modulo_rotura_ = Entry(ventana1, bg="red")
    modulo_rotura_.place(x=180, y=250, width=60, height=25)
    modulo_rotura_.config(bg="silver")

    modulo_rotura_unidades = Label(ventana1, text="kg/cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
    modulo_rotura_unidades.config(bg="white")
    modulo_rotura_unidades.place(x=245, y=250, width=50, height=25)

    # Calculo del módulo de rotura

    Fr = 2 * (math.sqrt(viga_material.compresion_concreto))
    Fr = round(Fr, 2)
    modulo_rotura_.delete(0, 'end')
    modulo_rotura_.insert(0, Fr)

    # Momento de agrietamiento - txt

    momento_agrietamiento = Label(ventana1, text="Momento critico", font=('Century Gothic', 9, 'bold'))
    momento_agrietamiento.place(x=25, y=290, width=135, height=25)
    momento_agrietamiento.config(bg="steel blue")

    # Resultado de momento de agrietamiento

    momento_agrietamiento_ = Entry(ventana1, bg="red")
    momento_agrietamiento_.place(x=180, y=290, width=60, height=25)
    momento_agrietamiento_.config(bg="silver")

    momento_agrietamiento_unidades = Label(ventana1, text="Tn-m", anchor="w", font=('Century Gothic', 9, 'bold'))
    momento_agrietamiento_unidades.config(bg="white")
    momento_agrietamiento_unidades.place(x=245, y=290, width=45, height=25)

    # Calculo del momento de agrietamiento

    Mcr = ((Ig * Fr) / (viga_geometria.altura / 2)) / 100000
    Mcr = round(Mcr, 2)
    momento_agrietamiento_.delete(0, 'end')
    momento_agrietamiento_.insert(0, Mcr)

    # Peralte efectivo - txt

    peralteefectivo = Label(ventana1, text="Peralte efectivo", font=('Century Gothic', 9, 'bold'))
    peralteefectivo.place(x=25, y=330, width=135, height=25)
    peralteefectivo.config(bg="steel blue")

    # Resultado peralte efectivo

    peralteefectivo_ = Entry(ventana1, bg="red")
    peralteefectivo_.place(x=180, y=330, width=60, height=25)
    peralteefectivo_.config(bg="silver")

    peralteefectivo_unidades = Label(ventana1, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    peralteefectivo_unidades.config(bg="white")
    peralteefectivo_unidades.place(x=245, y=330, width=45, height=25)

    area_barras = {'3/8"': 0.71, '1/2"': 1.29, '5/8"': 1.99, '3/4"': 2.84, '1"': 5.10}
    diametro_de_barras = {'3/8"': 0.9525, '1/2"': 1.27, '5/8"': 1.5875, '3/4"': 1.905, '1"': 2.54}

    # ESTRIBOS

    barra_escogida = viga_ac.primeraseleccion

    area_escogida_ETB = area_barras[barra_escogida]
    diametro_de_estribo = diametro_de_barras[barra_escogida]

    # LONGITUDINAL

    barra_escogida2 = viga_ac.segundaseleccion

    area_escogida_aslong = area_barras[barra_escogida2]
    diametro_de_aslong = diametro_de_barras[barra_escogida2]

    # BASTONES
    
    barra_escogida3 = viga_ac.terceraseleccion

    area_escogida_bastones = area_barras[barra_escogida3]
    diametro_de_bastones = diametro_de_barras[barra_escogida3]
    
    #VERIFICAR ESPESOR DE RECUBRIMIENTO
    
    peralte_efectivo = viga_geometria.altura - viga_material.recubrimiento_final - diametro_de_estribo - (diametro_de_aslong / 2)
    peralte_efectivo = round(peralte_efectivo, 2)

    # Acero minimo - calculo

    Asmin = c_minima * viga_geometria.base * peralte_efectivo
    Asmin = round(Asmin, 4)
    acero_minimo_.delete(0, 'end')
    acero_minimo_.insert(0, Asmin)

    peralteefectivo_.delete(0, 'end')
    peralteefectivo_.insert(0, peralte_efectivo)

    # Acero requerido - txt

    acero_requerido = Label(ventana1, text="Acero requerido", font=('Century Gothic', 9, 'bold'))
    acero_requerido.place(x=25, y=370, width=135, height=25)
    acero_requerido.config(bg="steel blue")

    # Resultado acero requerido

    acero_requerido_ = Entry(ventana1, bg="red")
    acero_requerido_.place(x=180, y=370, width=60, height=25)
    acero_requerido_.config(bg="silver")

    acero_requerido_unidades = Label(ventana1, text="cm\u00b2", anchor="w", font=('Century Gothic', 9, 'bold'))
    acero_requerido_unidades.config(bg="white")
    acero_requerido_unidades.place(x=245, y=370, width=45, height=25)

    # CALCULO DE ACERO REQUERIDO

    A = peralte_efectivo / 5

    K = 0

    ac_iteracion = 0

    dif = 1

    while dif != 0:
        ac_iteracion = (viga_momento_ultimo.m_ultimo * 100000) / (
                    viga_momento_ultimo.reduccion_flexion() * viga_material.fluencia_acero * (
            (peralte_efectivo - (A / 2))))
        ac_iteracion = round(ac_iteracion, 2)

        K = (ac_iteracion * viga_material.fluencia_acero) / (
                    0.85 * viga_material.compresion_concreto * viga_geometria.base)

        K = round(K, 2)

        dif = abs(K - A)

        A = K

        ac_iteracion = round(ac_iteracion, 4)

    acero_requerido_.delete(0, 'end')

    acero_requerido_.insert(0, ac_iteracion)

    # Area de acero seleccionado
    resultado_area_seleccionado = Label(ventana1, text="Area total de acero", font=('Century Gothic', 9, 'bold'))
    resultado_area_seleccionado.place(x=25, y=450, width=135, height=25)
    resultado_area_seleccionado.config(bg="tan1")

    # Resultado de area seleccionada
    resultado_area_seleccionado_ = Entry(ventana1, bg="red")
    resultado_area_seleccionado_.place(x=180, y=450, width=60, height=25)
    resultado_area_seleccionado_.config(bg="silver")

    resultado_area_seleccionado_unidades = Label(ventana1, text="cm\u00b2", anchor="w",
                                                 font=('Century Gothic', 9, 'bold'))
    resultado_area_seleccionado_unidades.config(bg="white")
    resultado_area_seleccionado_unidades.place(x=245, y=450, width=45, height=25)

    # Resultado USAR acero minimo o  requerido
    # Bastones requeridos - txt

    bastones_requerido = Label(ventana1, text="Bastones requeridos", font=('Century Gothic', 9, 'bold'))
    bastones_requerido.place(x=25, y=490, width=135, height=25)
    bastones_requerido.config(bg="tan1")

    # Resultados bastones requeridos

    bastones_requerido_ = Entry(ventana1, bg="red")
    bastones_requerido_.place(x=180, y=490, width=60, height=25)
    bastones_requerido_.config(bg="silver")

    bastones_requerido_unidades = Label(ventana1, text="Ø" + viga_ac.terceraseleccion, anchor="w",
                                        font=('Century Gothic', 9, 'bold'))
    bastones_requerido_unidades.config(bg="white")
    bastones_requerido_unidades.place(x=245, y=490, width=45, height=25)

    area_total = 0

    if ac_iteracion > Asmin:
        usar = "Usar acero requerido"

        # area_escogida_aslong=area_barras[selection1]

        area_escogida = viga_ac.barras * area_escogida_aslong

        area_escogida = round(area_escogida, 2)

        if ac_iteracion < area_escogida:
            area_de_bastones = 0
            numero_de_bastones = 0
        else:
            area_de_bastones = ac_iteracion - area_escogida
            numero_de_bastones = (area_de_bastones // area_escogida_bastones) + 1
            area_de_bastones = numero_de_bastones * area_escogida_bastones

        bastones_requerido_.delete(0, 'end')

        bastones_requerido_.insert(0, numero_de_bastones)

        resultado_area_seleccionado_.delete(0, 'end')

        resultado_area_seleccionado_.insert(0, round(area_escogida + area_de_bastones, 2))

        area_total = area_escogida + area_de_bastones


    else:
        usar = "Usar acero minimo "

        acero_requerido_.delete(0, 'end')

        acero_requerido_.insert(0, ac_iteracion)

        area_escogida = viga_ac.barras * area_escogida_aslong

        area_escogida = round(area_escogida, 2)

        resultado_area_seleccionado_.delete(0, 'end')

        resultado_area_seleccionado_.insert(0, area_escogida)

        area_total = area_escogida

        if area_escogida < Asmin:

            messagebox.showinfo(message="No cumple con el acero minimo en toda la viga, aumente el numero de barras")
            ventana1.destroy()
        else:
            numero_de_bastones = 0

            bastones_requerido_.delete(0, 'end')

            bastones_requerido_.insert(0, numero_de_bastones)

    # MODIFICAR ESTE APARTADO.

    acero_usar = Label(ventana1, text=usar + " |", font=('Helvetica', 7, 'bold'), anchor="center")
    acero_usar.config(bg="white", fg="blue")
    acero_usar.place(x=25, y=410, width=105, height=25)

    # Nueva cuantilla

    cuantilla_new = area_total / (viga_geometria.base * peralte_efectivo)

    if cuantilla_new > c_maxima:

        comprobacion = "Falla fragil"

    elif cuantilla_new == c_maxima:

        comprobacion = "Falla balanceada"
    else:
        comprobacion = "Falla ductil"

    comprobacion_ = Label(ventana1, text=" " + comprobacion + " |", font=('Helvetica', 7, 'bold'), anchor="center")
    comprobacion_.config(bg="white", fg="red")
    comprobacion_.place(x=130, y=410, width=60, height=25)

    valor_new_a = (area_total) * viga_material.fluencia_acero / (
                0.85 * viga_material.compresion_concreto * viga_geometria.base)
    valor_new_a = round(valor_new_a, 4)

    momento_nominal = (area_total) * viga_material.fluencia_acero * (peralte_efectivo - valor_new_a / 2) / 100000
    momento_nominal = round(momento_nominal, 2)

    if viga_momento_ultimo.reduccion_flexion() * momento_nominal > 1.2 * Mcr:
        comprobacion_mn = "Cumple"
    else:
        comprobacion_mn = "No cumple"

    comprobacion_mn_ = Label(ventana1, text=" " + "Ø Mn > 1.2 Mcr" + "\n"'"' + comprobacion_mn + '"',
                             font=('Helvetica', 7, 'bold'), anchor="center")
    comprobacion_mn_.config(bg="white")
    comprobacion_mn_.place(x=190, y=410, width=80, height=25)

    m_nominal_ = Label(ventana1, text="Momento nominal", font=('Century Gothic', 9, 'bold'))
    m_nominal_.config(bg="tan1")
    m_nominal_.place(x=25, y=530, width=135, height=25)

    m_nominal_e = Entry(ventana1, bg="red")
    m_nominal_e.place(x=180, y=530, width=60, height=25)
    m_nominal_e.config(bg="silver")

    m_nominal_unidades = Label(ventana1, text="Tn-m", anchor="w", font=('Century Gothic', 9, 'bold'))
    m_nominal_unidades.config(bg="white")
    m_nominal_unidades.place(x=245, y=530, width=45, height=25)

    m_nominal_e.delete(0, 'end')
    m_nominal_e.insert(0, momento_nominal)

    figura1 = Figure(figsize=(5, 8), dpi=65, facecolor='white')
    xdata = [0, 0, viga_geometria.base, viga_geometria.base]
    ydata = [0, viga_geometria.altura, viga_geometria.altura, 0]

    plot1 = figura1.add_subplot(111)
    plot1.plot(xdata, ydata, label="VIGA" + str(viga_geometria.base) + "cm" " x " + str(
        viga_geometria.altura) + "cm" + "\n   f'c" + " " + str(viga_material.compresion_concreto) + " kg/cm\u00b2")
    plot1.grid()
    plot1.legend(loc='center')
    plot1.set_facecolor("silver")
    # plot1=figura1(x,y)

    plot1.hlines(y=0, xmin=0, xmax=viga_geometria.base)
    canvas = FigureCanvasTkAgg(figura1, master=ventana1)
    canvas.draw()
    canvas.get_tk_widget().place(x=340, y=5)


# DISEÑO DE CORTE DE LA VIGA

def diseño_corte():
    global ventana2
    ventana2 = Toplevel(ventana)
    ventana2.geometry("695x450")
    ventana2.resizable(False, False)
    ventana2.config(bg="white")
    ventana2.title("DISEÑO POR CORTE")

    viga_material1 = material()
    viga_geometria1 = geometria()
    viga_ac1 = acero()
    viga_cortante_ultimo1 = cortante()
    
    #COMPROBACIONES

    viga_material1.material_error()
    viga_geometria1.geometry_error()
    viga_ac1.acero_error()
    viga_cortante_ultimo1.cortante_error()

    area_barras = {'3/8"': 0.71, '1/2"': 1.29, '5/8"': 1.99, '3/4"': 2.84, '1"': 5.10}
    diametro_de_barras = {'3/8"': 0.9525, '1/2"': 1.27, '5/8"': 1.5875, '3/4"': 1.905, '1"': 2.54}


        # ESTRIBOS

    barra_escogida = viga_ac1.primeraseleccion
    area_escogida_ETB = area_barras[barra_escogida]
    diametro_de_estribo = diametro_de_barras[barra_escogida]

    # LONGITUDINAL

    barra_escogida2 = viga_ac1.segundaseleccion
    diametro_de_aslong = diametro_de_barras[barra_escogida2]

    #PERALTE EFECTIVO

    peralte_efectivo = viga_geometria1.altura - viga_material1.recubrimiento_final - diametro_de_estribo - (diametro_de_aslong / 2)
    peralte_efectivo = round(peralte_efectivo, 2)

    # TITULO - CORTANTES

    lbl = Label(ventana2, text="CORTANTES", font=('Century Gothic', 9, 'bold'), anchor="center")
    lbl.place(x=25, y=10, width=165, height=25)
    lbl.config(bg="white")
    
    #CALCULO DEL CORTANTE ULTIMO DE DISEÑO

    Vud_txt = Label(ventana2,text="Vud", font=('Century Gothic', 9, 'bold'))
    Vud_txt.place(x=25, y=50, width=55, height=25)
    Vud_txt.config(bg="steel blue")

    Vud_ = Entry(ventana2, bg="red",justify='center')
    Vud_.place(x=90, y=50, width=60, height=25)
    Vud_.config(bg="silver")

    Vud = viga_cortante_ultimo1.cortante * ((viga_geometria1.lng / 2) - (peralte_efectivo / 100)) / (
                viga_geometria1.lng / 2)
    Vud = round(Vud,2)
    Vud_.delete(0,'end')
    Vud_.insert(0,Vud)
    #
    Vud_unidades = Label(ventana2, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
    Vud_unidades.config(bg="white")
    Vud_unidades.place(x=145, y=50, width=45, height=25)

    #CALCULO DEL CORTANTE NOMINAL

    Vn_txt = Label(ventana2, text="Vn", font=('Century Gothic', 9, 'bold'))
    Vn_txt.place(x=25, y=90, width=55, height=25)
    Vn_txt.config(bg="steel blue")

    Vn_ = Entry(ventana2,bg='red',justify='center')
    Vn_.place(x=90, y=90, width=60, height=25)
    Vn_.config(bg="silver")

    Vn = Vud/viga_cortante_ultimo1.reduccion_corte()
    Vn = round(Vn,2)
    Vn_.delete(0,'end')
    Vn_.insert(0,Vn)

    Vn_unidades = Label(ventana2, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
    Vn_unidades.config(bg="white")
    Vn_unidades.place(x=145, y=90, width=45, height=25)

    #CALCULO DEL APORTE DEL CONCRETO AL CORTE

    Vc_txt = Label(ventana2,text="Vc", font=('Century Gothic', 9, 'bold'))
    Vc_txt.place(x=25,y=130, width=55, height=25)
    Vc_txt.config(bg="steel blue")

    Vc_ = Entry(ventana2,bg="red",justify='center')
    Vc_.place(x=90, y=130, width=60, height=25)
    Vc_.config(bg="silver")

    Vc = 0.53*math.sqrt(viga_material1.compresion_concreto)*viga_geometria1.base/100*peralte_efectivo/100*10
    Vc = round(Vc,2)
    Vc_.delete(0, 'end')
    Vc_.insert(0,Vc)

    Vc_unidades = Label(ventana2, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
    Vc_unidades.config(bg="white")
    Vc_unidades.place(x=145, y=130, width=45, height=25)

    #CALCULO DEL APORTE DEL ACERO AL Corte

    Vs_txt=Label(ventana2,text="Vs", font=('Century Gothic', 9, 'bold'))
    Vs_txt.place(x=25,y=170,width=55, height=25)
    Vs_txt.config(bg="steel blue")

    Vs_ = Entry(ventana2, bg="red",justify='center')
    Vs_.place(x=90,y=170, width=60, height=25)
    Vs_.config(bg="silver")

    Vs = Vn - Vc
    Vs =round(Vs,2)
    Vs_.delete(0, 'end')
    Vs_.insert(0,Vs)

    Vs_unidades = Label(ventana2, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
    Vs_unidades.config(bg="white")
    Vs_unidades.place(x=145, y=170, width=45, height=25)


    #CALCULO DE ESPACIAMIENTO EN FUNCIÓN DEL VS CALCULADO
    #s_c: separación central 
    s_c_lbl=Label(ventana2,text="S",font=('Century Gothic', 9, 'bold'))
    s_c_lbl.place(x=25,y=210,width=55, height=25)
    s_c_lbl.config(bg="steel blue")

    s_c_ = Entry(ventana2, bg="red",justify='center')
    s_c_.place(x=90,y=210, width=60, height=25)
    s_c_.config(bg="silver")
    
    s_c=2*area_escogida_ETB*viga_material1.fluencia_acero*peralte_efectivo/(Vs*1000)
    s_c=round(s_c,2)
    s_c_.delete(0, 'end')
    s_c_.insert(0,s_c)

    '''Vs_unidades = Label(ventana2, text="Tn", anchor="w", font=('Century Gothic', 9, 'bold'))
    Vs_unidades.config(bg="white")
    Vs_unidades.place(x=95, y=170, width=45, height=25)'''

    #VERIFICACIÓN DE REQUISITOS
    # TITULO - CASOS

    lbl = Label(ventana2, text="CASOS", font=('Century Gothic', 9, 'bold'), anchor="center")
    lbl.place(x=220, y=10, width=260, height=25)
    lbl.config(bg="white")

    # TITULO - Scal

    lbl = Label(ventana2, text="s-cal", font=('Century Gothic', 9, 'bold'), anchor="center")
    lbl.place(x=490, y=10, width=70, height=25)
    lbl.config(bg="white")

    # TITULO - Sasu

    lbl = Label(ventana2, text="s-asu", font=('Century Gothic', 9, 'bold'), anchor="center")
    lbl.place(x=585, y=10, width=70, height=25)
    lbl.config(bg="white")

    #CASO I

    caso_I_lbl=Label(ventana2,text="CASO I",font=('Century Gothic', 9, 'bold'))
    caso_I_lbl.place(x=220,y=50,width=70, height=25)
    caso_I_lbl.config(bg="steel blue")

    if Vn <= Vc/2:
        caso_I_resultado="NO REQUIERE REFUERZO"
    else:
        caso_I_resultado="REQUIERE REFUERZO"

    caso_I_E = Label(ventana2,text=caso_I_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
    caso_I_E.place(x=300,y=50, width=180, height=25)
    caso_I_E.config(bg="silver")

        #S CALCULADO
    caso_I_s=Entry(ventana2,bg="red",justify='center')
    caso_I_s.place(x=490,y=50,width=50, height=25)
    caso_I_s.config(bg="silver")

    if caso_I_resultado =="NO REQUIERE REFUERZO":
        caso_I_s.delete(0, 'end')
        caso_I_s.insert(0,'-')
    else:
        caso_I_s.delete(0, 'end')
        caso_I_s.insert(0,'-')   

    caso_I_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_I_unidades.config(bg="white")
    caso_I_unidades.place(x=545, y=50, width=30, height=25) 
    
        #S ASUMIDO
    caso_I_a=Entry(ventana2,bg="red",justify='center')
    caso_I_a.place(x=585,y=50,width=50, height=25)
    caso_I_a.config(bg="silver")
    caso_I_a.delete(0, 'end')
    caso_I_a.insert(0,'-')

    caso_I_a_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_I_a_unidades.config(bg="white")
    caso_I_a_unidades.place(x=640, y=50, width=30, height=25) 

    #CASO II
    
    caso_II_lbl=Label(ventana2,text="CASO II",font=('Century Gothic', 9, 'bold'))
    caso_II_lbl.place(x=220,y=90,width=70, height=25)
    caso_II_lbl.config(bg="steel blue")

    if Vn >= Vc/2 and Vn <= Vc:
        caso_II_resultado="REQUIERE REFUERZO MÍNIMO"
    else:
        caso_II_resultado="NO REQUIERE REFUERZO"

    caso_II_E = Label(ventana2,text=caso_II_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
    caso_II_E.place(x=300,y=90, width=180, height=25)
    caso_II_E.config(bg="silver")

    caso_II_s=Entry(ventana2,bg="red",justify='center')
    caso_II_s.place(x=490,y=90,width=50, height=25)
    caso_II_s.config(bg="silver")

                #S ASUMIDO
    caso_II_a=Entry(ventana2,bg="red",justify='center')
    caso_II_a.place(x=585,y=90,width=50, height=25)
    caso_II_a.config(bg="silver")

    caso_II_a_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_II_a_unidades.config(bg="white")
    caso_II_a_unidades.place(x=640, y=90, width=30, height=25) 
 
    if caso_II_resultado =="REQUIERE REFUERZO MÍNIMO":
        s_II=area_escogida_ETB*viga_material1.fluencia_acero/(3.5*viga_geometria1.base)
        s_II=round(s_II,2)

        if s_II <= peralte_efectivo/2 and s_II <= 60:
            s_II=round(s_II,2)
            for i in range(0,65,5):
                i=i/2
                if s_II >= 2.5+i and s_II <= 5.00+i:
                    s_II_a=2.5+i

                elif s_II >=5.00 and s_II <7.5:
                    s_II_a=5.00

        elif s_II >peralte_efectivo/2 and peralte_efectivo/2 <= 60:
            s_II = peralte_efectivo/2
            s_II=round(s_II,2)
            for j in range(0,65,5):
                j=j/2
                if s_II >= 2.5+j and s_II <= 5.00+j:
                    s_II_a=2.5+j

                elif s_II >=5.00 and s_II <7.5:
                    s_II_a=5.00

        elif peralte_efectivo/2 >= 60:
            s_II=60
            s_II=round(s_II,2)
            s_II_a=60

        caso_II_s.delete(0, 'end')
        caso_II_s.insert(0,s_II)
        caso_II_a.delete(0, 'end')
        caso_II_a.insert(0,s_II_a)

    else:
        caso_II_s.delete(0, 'end')
        caso_II_s.insert(0,'-')
        caso_II_a.delete(0, 'end')
        caso_II_a.insert(0,'-')
    
    caso_II_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_II_unidades.config(bg="white")
    caso_II_unidades.place(x=545, y=90, width=30, height=25)

    if caso_II_resultado=="NO REQUIERE REFUERZO":
        caso_II_a.delete(0, 'end')
        caso_II_a.insert(0,'-')

        #CASO III-A
    
    caso_IIIA_lbl=Label(ventana2,text="CASO III-A",font=('Century Gothic', 9, 'bold'))
    caso_IIIA_lbl.place(x=220,y=130,width=70, height=25)
    caso_IIIA_lbl.config(bg="steel blue")

    if Vn >= Vc:
        caso_IIIA_resultado="REQUIERE REFUERZO"
    else:
        caso_IIIA_resultado="NO REQUIERE REFUERZO"

    caso_IIIA_E = Label(ventana2,text=caso_IIIA_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
    caso_IIIA_E.place(x=300,y=130, width=180, height=25)
    caso_IIIA_E.config(bg="silver")

    caso_IIIA_s=Entry(ventana2,bg="red",justify='center')
    caso_IIIA_s.place(x=490,y=130,width=50, height=25)
    caso_IIIA_s.config(bg="silver")

    caso_IIIA_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IIIA_unidades.config(bg="white")
    caso_IIIA_unidades.place(x=545, y=130, width=30, height=25)

                    #S ASUMIDO
    caso_IIIA_a=Entry(ventana2,bg="red",justify='center')
    caso_IIIA_a.place(x=585,y=130,width=50, height=25)
    caso_IIIA_a.config(bg="silver")

    caso_IIIA_a_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IIIA_a_unidades.config(bg="white")
    caso_IIIA_a_unidades.place(x=640, y=130, width=30, height=25) 

    if caso_IIIA_resultado =="REQUIERE REFUERZO":
        if Vs<=Vc*2:
            s_IIIA=0
            if peralte_efectivo/2 <= 60:
                s_IIIA = peralte_efectivo/2
                s_IIIA=round(s_IIIA,2)
                for i in range(0,65,5):
                    i=i/2
                    if s_IIIA >= 2.5+i and s_IIIA <= 5.00+i:
                        s_IIIA_a=2.5+i

                    elif s_IIIA >=5.00 and s_IIIA <7.5:
                        s_IIIA_a=5.00

            elif peralte_efectivo/2 >= 60:
                s_IIIA = 60
                s_IIIA=round(s_IIIA,2)
                s_IIIA_a=round(s_IIIA)

            caso_IIIA_s.delete(0, 'end')
            caso_IIIA_s.insert(0,s_IIIA)
            caso_IIIA_a.delete(0, 'end')
            caso_IIIA_a.insert(0,s_IIIA_a)
        else:

            caso_IIIA_s.delete(0, 'end')
            caso_IIIA_s.insert(0,'-')
            caso_IIIA_a.delete(0, 'end')
            caso_IIIA_a.insert(0,'-')

    else:
        caso_IIIA_s.delete(0, 'end')
        caso_IIIA_s.insert(0,'-') 
        caso_IIIA_a.delete(0, 'end')
        caso_IIIA_a.insert(0,'-')

            #CASO III-B
    
    caso_IIIB_lbl=Label(ventana2,text="CASO III-B",font=('Century Gothic', 9, 'bold'))
    caso_IIIB_lbl.place(x=220,y=170,width=70, height=25)
    caso_IIIB_lbl.config(bg="steel blue")

    if Vn >= Vc:
        caso_IIIB_resultado="REQUIERE REFUERZO"
    else:
        caso_IIIB_resultado="NO REQUIERE REFUERZO"

    caso_IIIB_E = Label(ventana2,text=caso_IIIB_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
    caso_IIIB_E.place(x=300,y=170, width=180, height=25)
    caso_IIIB_E.config(bg="silver")

    caso_IIIB_s=Entry(ventana2,bg="red",justify='center')
    caso_IIIB_s.place(x=490,y=170,width=50, height=25)
    caso_IIIB_s.config(bg="silver")

    caso_IIIB_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IIIB_unidades.config(bg="white")
    caso_IIIB_unidades.place(x=545, y=170, width=30, height=25)

                        #S ASUMIDO
    caso_IIIB_a=Entry(ventana2,bg="red",justify='center')
    caso_IIIB_a.place(x=585,y=170,width=50, height=25)
    caso_IIIB_a.config(bg="silver")

    caso_IIIB_a_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IIIB_a_unidades.config(bg="white")
    caso_IIIB_a_unidades.place(x=640, y=170, width=30, height=25)

    if caso_IIIB_resultado =="REQUIERE REFUERZO":
        if Vs>=Vc*2:
            s_IIIB=0
            if peralte_efectivo/4 <= 30:
                s_IIIB = peralte_efectivo/4
                s_IIIB=round(s_IIIB,2)
                for i in range(0,65,5):
                    i=i/2
                    if s_IIIB >= 2.5+i and s_IIIB <= 5.00+i:
                        s_IIIB_a=2.5+i

                    elif s_IIIB >=5.00 and s_IIIB <7.5:
                        s_IIIB_a=5.00

            elif peralte_efectivo/4 >= 30:
                s_IIIB = 30
                s_IIIB=round(s_IIIB,2)

            caso_IIIB_s.delete(0, 'end')
            caso_IIIB_s.insert(0,s_IIIB)
            caso_IIIB_a.delete(0, 'end')
            caso_IIIB_a.insert(0,s_IIIB_a)
        else:

            caso_IIIB_s.delete(0, 'end')
            caso_IIIB_s.insert(0,'-')
            caso_IIIB_a.delete(0, 'end')
            caso_IIIB_a.insert(0,'-')
    else:
        caso_IIIB_s.delete(0, 'end')
        caso_IIIB_s.insert(0,'-')
        caso_IIIB_a.delete(0, 'end')
        caso_IIIB_a.insert(0,'-')

        #CASO IV
    
    caso_I_lbl=Label(ventana2,text="CASO IV",font=('Century Gothic', 9, 'bold'))
    caso_I_lbl.place(x=220,y=210,width=70, height=25)
    caso_I_lbl.config(bg="steel blue")
       
    if Vs >= 4*Vc:
        caso_IV_resultado="CAMBIAR SECCIÓN"

        caso_IV_E = Label(ventana2,text=caso_IV_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
        caso_IV_E.place(x=300,y=210, width=180, height=25)

        caso_I_a.delete(0, 'end')
        caso_I_a.insert(0,'-')
        caso_II_s.delete(0, 'end')
        caso_II_s.insert(0,'-')        
        caso_II_a.delete(0, 'end')
        caso_II_a.insert(0,'-')
        caso_IIIA_s.delete(0, 'end')
        caso_IIIA_s.insert(0,'-')        
        caso_IIIA_a.delete(0, 'end')
        caso_IIIA_a.insert(0,'-')
        caso_IIIB_s.delete(0, 'end')
        caso_IIIB_s.insert(0,'-')
        caso_IIIB_a.delete(0, 'end')
        caso_IIIB_a.insert(0,'-')
        
        caso_IV_E.config(bg="silver", fg="red")
    else:
        caso_IV_resultado="MANTENER SECCIÓN"

        caso_IV_E = Label(ventana2,text=caso_IV_resultado,font=('Century Gothic', 9, 'bold'),anchor="w")
        caso_IV_E.place(x=300,y=210, width=180, height=25)
        caso_IV_E.config(bg="silver", fg="blue")

    caso_IV_s=Entry(ventana2,bg="red",justify='center')
    caso_IV_s.place(x=490,y=210,width=50, height=25)
    caso_IV_s.config(bg="silver")

    caso_IV_s.delete(0, 'end')
    caso_IV_s.insert(0,'-')

    caso_IV_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IV_unidades.config(bg="white")
    caso_IV_unidades.place(x=545, y=210, width=30, height=25)

                            #S ASUMIDO
    caso_IV_a=Entry(ventana2,bg="red",justify='center')
    caso_IV_a.place(x=585,y=210,width=50, height=25)
    caso_IV_a.config(bg="silver")

    caso_IV_a_unidades = Label(ventana2, text="cm", anchor="w", font=('Century Gothic', 9, 'bold'))
    caso_IV_a_unidades.config(bg="white")
    caso_IV_a_unidades.place(x=640, y=210, width=30, height=25)
    
    caso_IV_a.delete(0, 'end')
    caso_IV_a.insert(0,'-')
    #PARA LOS ESTRIBOS EN LA ZONA DE CONFINAMIENTOS
    a=peralte_efectivo/4
    b=6*diametro_de_estribo
    if a>b:
        #ESPACIAMIENTO EN LA ZONA DE CONFINAMIENTO CALCULADO
        s_confin_c = 6*diametro_de_estribo
        s_confin_c=round(s_confin_c,2)
        #ESPACIAMIENTO EN LA ZONA DE CONFINAMIENTO ASUMIDO
        for i in range(0,65,5):
            i=i/2
            if s_confin_c >= 2.5+i and s_confin_c <= 5.00+i:
                s_confin_a=2.5+i
    else:
        #ESPACIAMIENTO EN LA ZONA DE CONFINAMIENTO CALCULADO
        s_confin_c=a=peralte_efectivo/4
        s_confin_c=round(s_confin_c,2)
        #ESPACIAMIENTO EN LA ZONA DE CONFINAMIENTO ASUMIDO
        for i in range(0,65,5):
            i=i/2
            if s_confin_c >= 2.5+i and s_confin_c <= 5.00+i:
                s_confin_a=2.5+i

    figura2 = Figure(figsize=(12.5, 3), dpi=55, facecolor='white')
    longitud_viga=viga_geometria1.lng*100
    longitud_confinamiento=viga_geometria1.altura*2

    #CANTIDAD DE ESTRIBOS EN LA ZONA DE CONFINAMIENTO

    c_estribos_lc=round(longitud_confinamiento/s_confin_a,0)
    c_estribos_lc=int(math.ceil(c_estribos_lc))
    xdata = [0, 0, longitud_viga, longitud_viga]
    ydata = [0, viga_geometria1.altura, viga_geometria1.altura, 0]
    xdata2 =[5,5]
    ydata2 =[0,viga_geometria1.altura]
    xdata3 =[longitud_viga-5,longitud_viga-5]
    ydata3 =[0,viga_geometria1.altura]
    xdata4=[]
    ydata4=[]
    for i in range(1,c_estribos_lc+1,1):
        xdata_p=[5.00+s_confin_a*i,5.00+s_confin_a*i,s_confin_a+s_confin_a*i]
        ydata_p=[0,viga_geometria1.altura,viga_geometria1.altura]
        xdata4.append(xdata_p)
        ydata4.append(ydata_p)
    #VERIFICAR ESTE BUCLE PARA LOS ESTRIBOS DE LA VIGA

    plot2 = figura2.add_subplot(111)

    plot2.plot(xdata, ydata, xdata2, ydata2, xdata3, ydata3, xdata4, ydata4)
    plot2.set_facecolor("silver")
    # plot1=figura1(x,y)

    plot2.hlines(y=0, xmin=0, xmax=longitud_viga)
    canvas = FigureCanvasTkAgg(figura2, master=ventana2)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=240)



'''graficar la viga con su acero, colocar la distribución del acero final por el diseño de corte
colocar filas y columnas de aceros en la viga, graficas los aceros en la viga'''

    #CLASE 17 - 44:30



# RESULTADOS

# CUANTILLA

d_flexion = Button(ventana, text="D.Flexion", command=resultado_total, activebackground="royal blue",
                   activeforeground="white", borderwidth=3)
d_flexion.config(fg="white", bg="gray2", cursor="hand2", font=('Century Gothic', 9, 'bold'))
d_flexion.place(x=240, y=230, width=100, height=40)

d_corte = Button(ventana, text="D.Corte", command=diseño_corte, activebackground="royal blue", activeforeground="white",
                 borderwidth=3)
d_corte.config(fg="white", bg="gray2", cursor="hand2", font=('Century Gothic', 9, 'bold'))
d_corte.place(x=360, y=230, width=100, height=40)

d_otros = Button(ventana, text="Otros", activebackground="royal blue", activeforeground="white", borderwidth=3)
d_otros.config(fg="white", bg="gray2", cursor="hand2", font=('Century Gothic', 9, 'bold'))
d_otros.place(x=480, y=230, width=100, height=40)

ventana.mainloop()

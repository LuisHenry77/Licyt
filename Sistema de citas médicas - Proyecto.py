class PERSON:
   def __init__(self,nombre, apellido, ocupacion):
       self.nombre = nombre
       self.apellido = apellido
       self.ocupacion = ocupacion
   def saludar(self):
       return f"hola mi nombre es  {self.nombre} {self.apellido} soy su {self.ocupacion}  "
class A(PERSON):
   def saludardoctor(self,especialidad):
       return f"hola mi nombre es  {self.nombre} {self.apellido} mi ocupacion es {self.ocupacion} y mi especialidad es {especialidad}"
class B(PERSON):
   def saludarenfermera(self, cargo):
       return f"hola  mi nombre es  {self.nombre} {self.apellido} soy su {self.ocupacion} y cuido a los {cargo}"
class C(PERSON):
   def saludarcardiologo(self,especialidad):
       return f"hola mi nombre es  {self.nombre} {self.apellido} soy {self.ocupacion} y soy {especialidad}"
class D(PERSON):
   def saludardoctora(self,especialidad):
       return f"hola mi nombre es  {self.nombre} {self.apellido} soy {self.ocupacion} y mi especialidad es {especialidad}"
class I(PERSON):
   def personal(self,cargo):
       return f"hola mi nombre es  {self.nombre} {self.apellido}  soy el {self.ocupacion} y administro el reparto de las {cargo}"


print("HOSPITAL SANTA CALATINA")
print("""
################
1.RESERVAR CITA
2.ESPECIALIDADES
3.EMERGEGENCIAS
4.SALIR
################
""")
usuario = input("Seleccione un número por favor -> ")
if (usuario == "1"):
   print("""
   SELECCIONE SU CITA
   1.MEDICO GENERAL
   2.ENFERMERIA
   3.PERSONAL ADMINISTRATIVO
   4.SALIR
    """)
   cita = input("Médico-> ")
   if (cita == "1"):
       diego = PERSON("Daniel","Soliz","Médico general")
       print(diego.saludar())
   if (cita == "2"):
       tania = B("Tatiana","Mendez","Enfermera")
       print(tania.saludarenfermera("atiendo a los pacientes"))
   if (cita == "3"):
       henry = I("Harold","Cruz","Administrador")
       print(henry.personal("Fichas"))
   if (cita == "4"):
       print("Gracias, regrese pronto")

if (usuario == "2"):
   print("""
     ESPECIALIDADES
     1.CARDIOLOGO
     2.ENDOSCOPIA
     3.UROLOGO
     4.GINECOLOGO
     5.RAYOS X
     6.CIRUJIA GENERAL
     7.GASTROENTEREOLOGIA
     8.INFECTOLOGIA
     9.NEFROLOGIA
     10.NEUMOLOGIA
     11.NEUROLOGIA
     12.NUTRIOLOGIA
     13.OFTALMOLIGA
     14.SALIR

   """)
   cita = input("Médico -> " )

   if (cita == "1"):
       lola = C("Lastenia","Tambare", "Médico")
       print(lola.saludarcardiologo("Cardiólogo"))
   elif (cita == "2"):
       andrea = D("Abigail","Aguirre","Médico")
       print(andrea.saludardoctora("endoscopia"))
   elif (cita == "3"):
       hugo = C("Héctor","Jimenez","Méedico")
       print(hugo.saludarcardiologo("Urólogo"))
   elif (cita == "4"):
       carlos = C("Caleb","Santander","Médico")
       print(carlos.saludarcardiologo("Ginecólogo"))
   elif (cita == "5"):
       lola = D("Leandra","Strait","Médico")
       print(lola.saludardoctora("Rayos x"))
   elif (cita == "6"):
       martin = D("Marco","Arenas","Médico")
       print(martin.saludardoctora("Cirugía general"))
   elif (cita == "7"):
       paola = D("Pamela","Jaimez","Médico")
       print(paola.saludardoctora("Gastroentereología"))
   elif (cita == "8"):
       stefany = D("Saida","Miranda","Médico")
       print(stefany.saludardoctora("Infectologiía"))
   elif (cita == "9"):
       jhanet = D("Jimena","Heredia","Médico")
       print(jhanet.saludardoctora("Nefrologia"))
   elif (cita == "10"):
       estrella = D("Eva","Ledezma","Médico")
       print(estrella.saludardoctora("Neumología"))
   elif (cita == "11"):
       angela = D("Abril","Padilla","Médico")
       print(angela.saludardoctora("NeurologÍa"))
   elif (cita == "12"):
       abigail = C("Aída","Paniagua","Médico")
       print(abigail.saludarcardiologo("Nutrióloga"))
   elif (cita == "13"):
       mariana = A("María","Soliz","Médico")
       print(mariana.saludardoctor("OftalmologÍa"))
if (usuario == "3"):
   print("Hola, ¿Cómo podemos ayudarlo? ")
if (usuario == "4"):
   print("Gracias por su visita ")
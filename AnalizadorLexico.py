from prettytable import PrettyTable
from claseToken import *
from claseError import *
import re
class AnalizadorLexico:
  def __init__(self):
    self.listaTokens = []
    self.listaErrores = []
    self.PalabrasReservadas = ["formulario","tipo","valor","fondo","nombre","valores","evento","etiqueta","texto","grupo-radio","grupo-option","boton"]
    self.linea = 1 
    self.columna = 0
    self.buffer = ""
    self.estado = 0 # Estado Inicial 
    self.i = 0 #Contador para recorrer la cadena

  def agregarToken(self,lexema,linea,columna,token):
      self.listaTokens.append(Token(lexema,linea,columna,token))  
      self.buffer = ""

  def agregarError(self,caracter,linea,columna):
      self.listaErrores.append(Error('Caracter '+caracter+' no reconocido en el lenguaje ',linea,columna))  

  def s0(self,caracter:str):
    '''Estado S0'''
    if caracter.isalpha() or caracter.isdigit():
      self.estado = 1
      self.buffer += caracter
      self.columna += 1
    elif caracter == "'":
      self.estado = 2
      self.buffer += caracter
      self.columna +=1
    elif caracter == '"':
      self.estado = 3
      self.buffer += caracter
      self.columna +=1
    elif caracter == '~':
      self.estado = 4
      self.buffer += caracter
      self.columna +=1
    elif caracter == ',':
      self.estado = 5
      self.buffer += caracter
      self.columna +=1
    elif caracter == '[':
      self.estado = 6
      self.buffer += caracter
      self.columna +=1
    elif caracter == ']':
      self.estado = 7
      self.buffer += caracter
      self.columna +=1
    elif caracter == '<':
      self.estado = 8
      self.buffer += caracter
      self.columna +=1
    elif caracter == '>':
      self.estado = 9
      self.buffer += caracter
      self.columna +=1
    elif caracter == ':':
      self.estado = 10
      self.buffer += caracter
      self.columna +=1
    elif caracter == '\n':       #Saltos de línea 
      self.columna = 0
      self.linea += 1
    elif caracter in ["\t"," "]: #Espacios en blanco y tabulaciones
      self.columna += 1
    elif caracter == '$':
      print('Se terminó el análisis ')
    else:
      self.agregarError(caracter,self.linea,self.columna)


  def s1(self,caracter:str):
    '''Estado S1'''  
    if caracter.isalpha():
      self.estado = 1
      self.buffer += caracter
      self.columna += 1
    elif caracter.isdigit():
      self.estado = 1
      self.buffer += caracter
      self.columna += 1  
    elif caracter == '-':
      self.estado = 1
      self.buffer += caracter
      self.columna += 1
    elif caracter == " ":
      self.estado = 1
      self.buffer += caracter
      self.columna += 1
    else:
      if self.buffer in self.PalabrasReservadas:
         self.agregarToken(self.buffer,self.linea,self.columna,"palabra reservada {}".format(self.buffer))
      else:
        self.agregarToken(self.buffer,self.linea,self.columna,'contenido')
      self.estado = 0
      self.i -= 1

  def s2(self):
    '''Estado S2'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Comilla Simple")
    self.estado = 0
    self.i -= 1

  def s3(self):
    '''Estado S3'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Comilla Doble")
    self.estado = 0
    self.i -= 1

  def s4(self):
    '''Estado S4'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Virgulilla")
    self.estado = 0
    self.i -= 1
      
  def s5(self):
    '''Estado S5'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Coma")
    self.estado = 0
    self.i -= 1

  def s6(self):
    '''Estado S6'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Corchete Izquierdo")
    self.estado = 0
    self.i -= 1

  def s7(self):
    '''Estado S7'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Corchete Derecho")
    self.estado = 0
    self.i -= 1
    
  def s8(self):
    '''Estado S8'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Menor que")
    self.estado = 0
    self.i -= 1

  def s9(self):
    '''Estado S9'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Mayor que")
    self.estado = 0
    self.i -= 1 

  def s10(self):
    '''Estado S10'''
    self.agregarToken(self.buffer,self.linea,self.columna,"Dos puntos")
    self.estado = 0
    self.i -= 1 
    
  def analizar(self,cadena):
    cadena += '$'
    self.listaErrores = []
    self.listaTokens = []
    self.i = 0

    while self.i < len(cadena):
      if self.estado == 0:
          self.s0(cadena[self.i])
      elif self.estado == 1:
          self.s1(cadena[self.i])
      elif self.estado == 2:
          self.s2()
      elif self.estado == 3:
          self.s3()
      elif self.estado == 4:
          self.s4()
      elif self.estado == 5:
          self.s5()
      elif self.estado == 6:
          self.s6()
      elif self.estado == 7:
          self.s7()
      elif self.estado == 8:
          self.s8()
      elif self.estado == 9:
          self.s9()
      elif self.estado == 10:
          self.s10()
      self.i += 1


  def imprimirTokens(self):
      x = PrettyTable()
      x.field_names = ["lexema","linea","columna","tipo"]
      for token in self.listaTokens:
        x.add_row([token.lexema,token.linea,token.columna,token.tipo])
      print(x)

  def imprimirErrores(self):
      x = PrettyTable()
      x.field_names = ["Descripción","linea","columna"]
      for error in self.listaErrores:
        x.add_row([error.descripcion,error.linea,error.columna])
      print(x)


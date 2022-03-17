from AnalizadorLexico import *
from TabladeTokens import *
from TabladeErrores import *
from generarFormulario import *
from archivoEntrada import*


entrada = '''
 formulario ~>> [
	<
		tipo: "etiqueta",
		valor: "Formulario"
	>,
	<
		tipo: *"texto",
		valor: #"Nombre",
		fondo: //"Ingrese nombre" +
	>,
	<
		tipo: "grupo-radio", -
		nombre: "Sexo",
		valores: ['Masculino', 'Femenino'] /*
	>,
	<
		tipo: "grupo-option",
		nombre: "Pais",
		valores: ['Guatemala', 'El Salvador', 'Honduras']
	>,
 	<
		tipo: "grupo-radio", -
		nombre: "Colores",
		valores: ['Rojo', 'Azul','Amarillo','Negro'] /*
	>,
 	<
		tipo: "grupo-option",
		nombre: "Nombres",
		valores: ['Pedro', 'Carlos', 'Juan']
	>,
	<
		tipo: "boton",
		valor: "Valor",
		evento: <info>
	>
 
]
'''

analizadorLexico = AnalizadorLexico()
escribirArchivoEntrada(entrada)

analizadorLexico.analizar(entrada)
analizadorLexico.imprimirTokens()
analizadorLexico.imprimirErrores()

generarTablaTokens(analizadorLexico.listaTokens)
generarTablaErrores(analizadorLexico.listaErrores)

listadeTokens = analizadorLexico.listaTokens

extraerElementos(listadeTokens)

            
        
        






    



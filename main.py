from AnalizadorLexico import *



entrada = '''
 formulario ~>> [
	<
		tipo: "etiqueta",
		valor: "Nombre"
	>,
	<
		tipo: "texto",
		valor: "Nombre",
		fondo: "Ingrese nombre" +
	>,
	<
		tipo: "grupo-radio", -
		nombre: "sexo",
		valores: ['Masculino', 'Femenino'] /*
	>,
	<
		tipo: "grupo-option",
		nombre: "pais",
		valores: ['Guatemala', 'El Salvador', 'Honduras']
	>,
	<
		tipo: "boton",
		valor: "Valor",
		evento: <EVENTO>
	>
]
'''

analizadorLexico = AnalizadorLexico()

analizadorLexico.analizar(entrada)
analizadorLexico.imprimirTokens()
analizadorLexico.imprimirErrores()
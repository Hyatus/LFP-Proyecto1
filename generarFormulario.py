from TabladeTokens import *
from TabladeErrores import *


def escribirFormulario(listaElementos):
    
    encabezado = '''
        <!DOCTYPE html>
        <html>
        <head>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	    <title>Formulario</title>
        <link rel="stylesheet" type="text/css" href="estilo.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@500&family=Roboto:wght@700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
        <br>
        <br>
        <br>
        '''

                 
    final = ''' 
           </body>
           </html> 
            '''
    
    file = open('formulario.html',"w")
    file.write(encabezado)
    file.write("<div>")
    file.write('<form class="w-50 p-3" style="background-color: #eee;">')
    
    for i in range(len(listaElementos)):
        # Tipo de elemento 
        NumeroRadio = 0
        NumeroLista = 0
        if "tipo" in listaElementos[i].keys():
            valorTipo = listaElementos[i]["tipo"]
            #Clave del diccionario
            #print("--------- # TIPO DE ELEMENTO # ----------")
            #print(valorTipo)
            if valorTipo == "etiqueta":
                if "valor" in listaElementos[i+1].keys():
                    #Valor que ira dentro de la etiqueta
                    valorEtiqueta = listaElementos[i+1]["valor"]
                    #print(valorEtiqueta)
                    file.write(f'''
                    <div class="mb-3">
                    <label class="form-label">{valorEtiqueta}</label>
                    </div>
                    ''')
                    
            if valorTipo == "texto":
                valorTexto = ""
                fondoTexto = ""
                if "valor" in listaElementos[i+1].keys():
                #Valor que ira dentro de la etiqueta
                    valorTexto = listaElementos[i+1]["valor"]
                    #print(valorEtiqueta)
                if "fondo" in listaElementos[i+2].keys():
                    fondoTexto = listaElementos[i+2]["fondo"]
                    #print(fondoTexto)
                    
                file.write(f'''
                    <div class="mb-3">
                    <label class="form-label">{valorTexto}:</label>
                    <input type="text" class="form-control" placeholder="{fondoTexto}">
                    </div>
                    ''')
                
            if valorTipo == "grupo-radio":
                valorNombreRadio = ""
                if "nombre" in listaElementos[i+1].keys():
                    valorNombreRadio = listaElementos[i+1]["nombre"]
                    file.write(f'''
                      <fieldset>
                      <legend>{valorNombreRadio}</legend>
                       ''')
                    #print(valorNombreRadio)
                if "valores" in listaElementos[i+2].keys():
                    valoresRadio = listaElementos[i+2].values()
                    for elemento in valoresRadio:
                        for i in range(len(elemento)):
                            file.write(f'''
                            <label>
                            <input type="radio" name="{valorNombreRadio}" value="{elemento[i]}"> {elemento[i]}
                            </label>
                            ''')
                    file.write('</fieldset>')
                        #print(elemento[i])

            if valorTipo == "grupo-option":
                valorNombreOption = ""
                if "nombre" in listaElementos[i+1].keys():
                    valorNombreOption = listaElementos[i+1]["nombre"]
                    #print(valorNombreOption)
                    file.write(f'''
                    <div class="mb-3">
                    <label class="form-label form-check-inline"> {valorNombreOption}</label>
                    </div>
                    ''')
                if "valores" in listaElementos[i+2].keys():
                    valoresOption = listaElementos[i+2].values()
                    file.write(f'''
                              <select class="form-select form-select-lg mb-3">
                              <option selected>{valorNombreOption}</option>
                               ''')
                    for elemento in valoresOption:
                        valor = 1
                        for i in range(len(elemento)):
                            file.write(f'''
                                       <option value="{valor}">{elemento[i]}</option>
                                       ''')
                            valor += 1
                            #print(elemento[i])
                file.write("</select>")
                
            if valorTipo == "boton":
                valorBoton = ""
                eventoBoton = ""
                if "valor" in listaElementos[i+1].keys():
                    #Valor que ira dentro de la etiqueta
                    valorBoton = listaElementos[i+1]["valor"]
                    #print(valorBoton)
                if "evento" in listaElementos[i+2].keys():
                    #Valor que ira dentro de la etiqueta
                    eventoBoton = listaElementos[i+2]["evento"]
                    #print(eventoBoton)
                    
                file.write(f'''
                           <div class="mb-3">
                           <button type="button" id="evento" class="btn btn-primary btn-lg">{valorBoton}</button>
                           </div>
                           ''')
                if eventoBoton == "entrada":
                    file.write(f'''
                             <script type="text/javascript" src="script.js"></script>
                           ''')
                
    file.write("</form>")
    file.write("</div>")
    file.write(final)
    file.close()
    
    
def extraerElementos(listadeTokens):
    listaElementos = []
    for i in range(len(listadeTokens)):
        # tipo  :    "  etiqueta " ,
        #  i   i+1  i+2   i+3
        if listadeTokens[i].tipo == "palabra reservada tipo":
            aux = {}
            aux[listadeTokens[i].lexema] = listadeTokens[i+3].lexema
            listaElementos.append(aux)
        # valor    :   "      contenido  "
        #  i      i+1  i+2      i+3
        if listadeTokens[i].tipo == "palabra reservada valor":
            aux = {}
            aux[listadeTokens[i].lexema] = listadeTokens[i+3].lexema
            listaElementos.append(aux)
        # fondo   :     "      texto   " 
        #  i      i+1   i+2     i+3
        if listadeTokens[i].tipo == "palabra reservada fondo":
            aux = {}
            aux[listadeTokens[i].lexema] = listadeTokens[i+3].lexema
            listaElementos.append(aux)
        # nombre   :     "      texto   
        #  i      i+1   i+2      i+3   
        if listadeTokens[i].tipo == "palabra reservada nombre":
            aux = {}
            aux[listadeTokens[i].lexema] = listadeTokens[i+3].lexema
            listaElementos.append(aux)
        
        # Armar lista con valores 
        if listadeTokens[i].tipo == "palabra reservada valores":
            aux = {}
            listaValores = []
            clave = listadeTokens[i].lexema
            i += 1
            while listadeTokens[i].lexema != ']':
                if listadeTokens[i].tipo == "contenido":
                    listaValores.append(listadeTokens[i].lexema)
                i += 1
       
            aux[clave] = listaValores
            listaElementos.append(aux)
        
        # evento    :   <    EVENTO  
        #   i      i+1  i+2    i+3    
        if listadeTokens[i].tipo == "palabra reservada evento":
            aux = {}
            aux[listadeTokens[i].lexema] = listadeTokens[i+3].lexema
            listaElementos.append(aux)

    escribirFormulario(listaElementos)


        
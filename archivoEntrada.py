


def escribirArchivoEntrada(contenido):
    file = open('entrada.html',"w")
    
    encabezado = '''
        <!DOCTYPE html>
        <html>
        <head>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	    <title>Archivo Entrada</title>
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
    
    entrada = f'''<div><p><br>
                {contenido}
                <br></p></div>'''
                 
    final = ''' 
           </body>
           </html> 
            '''
            
    file.write(encabezado)
    file.write(entrada)
    file.write(final)
    file.close()
import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from AnalizadorLexico import *
from TabladeTokens import *
from TabladeErrores import *
from generarFormulario import *
from archivoEntrada import *
import os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("ANALIZAR")
        self.text = QtWidgets.QLabel("PROYECTO 1 LENGUAJES FORMALES DE PROGRAMACION",
                                     alignment=QtCore.Qt.AlignCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.comboX = QtWidgets.QComboBox()
        self.comboX.addItem("REPORTES")
        self.comboX.addItem("REPORTE DE TOKENS")
        self.comboX.addItem("REPORTE DE ERRORES")
        self.comboX.addItem("MANUAL DE USUARIO")
        self.comboX.addItem("MANUAL TECNICO")
        self.comboX.activated.connect(self.funcionCombo)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.plainTextEdit)
        self.layout.addWidget(self.comboX)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)
    
    def funcionCombo(self):
        opcion = self.comboX.currentText()
        if opcion == "REPORTE DE TOKENS":
            os.system("TablaTokens.html")
        if opcion == "REPORTE DE ERRORES":
            os.system("TablaErrores.html")
        if opcion == "MANUAL DE USUARIO":
            pass
        if opcion == "MANUAL TECNICO":
            pass
        
    @QtCore.Slot()
    def magic(self):
        #self.text.setText(random.choice(self.hello))
        entrada = self.plainTextEdit.toPlainText()
        analizadorLexico = AnalizadorLexico()
        if len(entrada) > 0:
            escribirArchivoEntrada(entrada)
            analizadorLexico.analizar(entrada)
            #analizadorLexico.imprimirTokens()
            #analizadorLexico.imprimirErrores()
            generarTablaTokens(analizadorLexico.listaTokens)
            generarTablaErrores(analizadorLexico.listaErrores)
            listadeTokens = analizadorLexico.listaTokens
            extraerElementos(listadeTokens)
            os.system("formulario.html")
            
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
        
        
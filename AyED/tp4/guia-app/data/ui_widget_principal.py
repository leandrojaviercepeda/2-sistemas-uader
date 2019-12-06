

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_principal(object):
    def setupUi(self, widget_principal):
        widget_principal.setObjectName("widget_principal")
        widget_principal.resize(1250, 650)
        widget_principal.setMinimumSize(QtCore.QSize(1250, 650))
        widget_principal.setMaximumSize(QtCore.QSize(1250, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/guia-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget_principal.setWindowIcon(icon)
        widget_principal.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.box_listado = QtWidgets.QGroupBox(widget_principal)
        self.box_listado.setGeometry(QtCore.QRect(10, 80, 1230, 401))
        self.box_listado.setStyleSheet("color: rgb(255, 255, 255);")
        self.box_listado.setObjectName("box_listado")
        self.tabla_listado = QtWidgets.QTableWidget(self.box_listado)
        self.tabla_listado.setGeometry(QtCore.QRect(10, 30, 1211, 361))
        self.tabla_listado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(0, 0, 0);")
        self.tabla_listado.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_listado.setProperty("showDropIndicator", True)
        self.tabla_listado.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabla_listado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_listado.setObjectName("tabla_listado")
        self.tabla_listado.setColumnCount(5)
        self.tabla_listado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(4, item)
        self.tabla_listado.horizontalHeader().setDefaultSectionSize(241)
        self.box_operaciones = QtWidgets.QGroupBox(widget_principal)
        self.box_operaciones.setGeometry(QtCore.QRect(670, 510, 570, 100))
        self.box_operaciones.setStyleSheet("color: rgb(255, 255, 255);")
        self.box_operaciones.setObjectName("box_operaciones")
        self.layoutWidget = QtWidgets.QWidget(self.box_operaciones)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 26, 551, 71))
        self.layoutWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_operaciones = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.layout_operaciones.setContentsMargins(0, 0, 0, 0)
        self.layout_operaciones.setObjectName("layout_operaciones")
        self.boton_agregar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_agregar.setMinimumSize(QtCore.QSize(45, 45))
        self.boton_agregar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_agregar.setStyleSheet("background-color: rgb(46, 52, 54);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imagenes/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_agregar.setIcon(icon1)
        self.boton_agregar.setIconSize(QtCore.QSize(44, 44))
        self.boton_agregar.setAutoDefault(False)
        self.boton_agregar.setObjectName("boton_agregar")
        self.layout_operaciones.addWidget(self.boton_agregar)
        self.boton_borrar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_borrar.setMinimumSize(QtCore.QSize(45, 45))
        self.boton_borrar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_borrar.setStyleSheet("background-color: rgb(46, 52, 54);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imagenes/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_borrar.setIcon(icon2)
        self.boton_borrar.setIconSize(QtCore.QSize(44, 44))
        self.boton_borrar.setAutoDefault(False)
        self.boton_borrar.setObjectName("boton_borrar")
        self.layout_operaciones.addWidget(self.boton_borrar)
        self.boton_editar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_editar.setMinimumSize(QtCore.QSize(45, 45))
        self.boton_editar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_editar.setStyleSheet("background-color: rgb(46, 52, 54);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imagenes/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_editar.setIcon(icon3)
        self.boton_editar.setIconSize(QtCore.QSize(44, 44))
        self.boton_editar.setAutoDefault(False)
        self.boton_editar.setObjectName("boton_editar")
        self.layout_operaciones.addWidget(self.boton_editar)
        self.boton_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_buscar.setMinimumSize(QtCore.QSize(45, 45))
        self.boton_buscar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_buscar.setStyleSheet("background-color: rgb(46, 52, 54);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imagenes/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_buscar.setIcon(icon4)
        self.boton_buscar.setIconSize(QtCore.QSize(44, 44))
        self.boton_buscar.setAutoDefault(False)
        self.boton_buscar.setObjectName("boton_buscar")
        self.layout_operaciones.addWidget(self.boton_buscar)
        self.input_buscar = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_buscar.setMinimumSize(QtCore.QSize(200, 30))
        self.input_buscar.setMaximumSize(QtCore.QSize(200, 30))
        self.input_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_buscar.setText("")
        self.input_buscar.setMaxLength(40)
        self.input_buscar.setPlaceholderText("")
        self.input_buscar.setObjectName("input_buscar")
        self.layout_operaciones.addWidget(self.input_buscar)
        self.combo_buscar = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_buscar.setMinimumSize(QtCore.QSize(90, 30))
        self.combo_buscar.setMaximumSize(QtCore.QSize(90, 30))
        self.combo_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.combo_buscar.setObjectName("combo_buscar")
        self.combo_buscar.addItem("")
        self.combo_buscar.addItem("")
        self.combo_buscar.addItem("")
        self.combo_buscar.addItem("")
        self.layout_operaciones.addWidget(self.combo_buscar)
        self.box_campos = QtWidgets.QGroupBox(widget_principal)
        self.box_campos.setGeometry(QtCore.QRect(10, 490, 651, 151))
        self.box_campos.setStyleSheet("color: rgb(255, 255, 255);")
        self.box_campos.setObjectName("box_campos")
        self.layoutWidget1 = QtWidgets.QWidget(self.box_campos)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 651, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layout_campos = QtWidgets.QGridLayout(self.layoutWidget1)
        self.layout_campos.setContentsMargins(0, 0, 0, 0)
        self.layout_campos.setObjectName("layout_campos")
        self.input_nombre = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_nombre.setMinimumSize(QtCore.QSize(145, 30))
        self.input_nombre.setMaximumSize(QtCore.QSize(145, 30))
        self.input_nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.input_nombre.setText("")
        self.input_nombre.setMaxLength(40)
        self.input_nombre.setObjectName("input_nombre")
        self.layout_campos.addWidget(self.input_nombre, 0, 0, 1, 1)
        self.input_apellido = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_apellido.setMinimumSize(QtCore.QSize(145, 30))
        self.input_apellido.setMaximumSize(QtCore.QSize(145, 30))
        self.input_apellido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.input_apellido.setText("")
        self.input_apellido.setMaxLength(40)
        self.input_apellido.setObjectName("input_apellido")
        self.layout_campos.addWidget(self.input_apellido, 0, 1, 1, 2)
        self.input_direccion = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_direccion.setMinimumSize(QtCore.QSize(295, 30))
        self.input_direccion.setMaximumSize(QtCore.QSize(295, 30))
        self.input_direccion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.input_direccion.setMaxLength(40)
        self.input_direccion.setObjectName("input_direccion")
        self.layout_campos.addWidget(self.input_direccion, 0, 3, 1, 1)
        self.input_caracteristica = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_caracteristica.setMinimumSize(QtCore.QSize(145, 30))
        self.input_caracteristica.setMaximumSize(QtCore.QSize(145, 30))
        self.input_caracteristica.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "color: rgb(0, 0, 0);")
        self.input_caracteristica.setText("")
        self.input_caracteristica.setMaxLength(4)
        self.input_caracteristica.setObjectName("input_caracteristica")
        self.layout_campos.addWidget(self.input_caracteristica, 1, 0, 1, 1)
        self.label_guion = QtWidgets.QLabel(self.layoutWidget1)
        self.label_guion.setMinimumSize(QtCore.QSize(20, 20))
        self.label_guion.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_guion.setFont(font)
        self.label_guion.setObjectName("label_guion")
        self.layout_campos.addWidget(self.label_guion, 1, 1, 1, 1)
        self.input_telefono = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_telefono.setMinimumSize(QtCore.QSize(145, 30))
        self.input_telefono.setMaximumSize(QtCore.QSize(145, 30))
        self.input_telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.input_telefono.setText("")
        self.input_telefono.setMaxLength(8)
        self.input_telefono.setObjectName("input_telefono")
        self.layout_campos.addWidget(self.input_telefono, 1, 2, 1, 1)
        self.input_localidad = QtWidgets.QLineEdit(self.layoutWidget1)
        self.input_localidad.setMinimumSize(QtCore.QSize(295, 30))
        self.input_localidad.setMaximumSize(QtCore.QSize(295, 30))
        self.input_localidad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.input_localidad.setText("")
        self.input_localidad.setMaxLength(40)
        self.input_localidad.setObjectName("input_localidad")
        self.layout_campos.addWidget(self.input_localidad, 1, 3, 1, 1)
        self.box_avisos = QtWidgets.QGroupBox(widget_principal)
        self.box_avisos.setGeometry(QtCore.QRect(10, 10, 981, 71))
        self.box_avisos.setStyleSheet("color: rgb(255, 255, 255);")
        self.box_avisos.setObjectName("box_avisos")
        self.label_avisos = QtWidgets.QLabel(self.box_avisos)
        self.label_avisos.setGeometry(QtCore.QRect(20, 30, 940, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_avisos.setFont(font)
        self.label_avisos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(191, 64, 64);")
        self.label_avisos.setText("")
        self.label_avisos.setObjectName("label_avisos")
        self.box_operaciones_listado = QtWidgets.QGroupBox(widget_principal)
        self.box_operaciones_listado.setGeometry(QtCore.QRect(1000, 0, 241, 91))
        self.box_operaciones_listado.setStyleSheet("color: rgb(255, 255, 255);")
        self.box_operaciones_listado.setObjectName("box_operaciones_listado")
        self.layoutWidget2 = QtWidgets.QWidget(self.box_operaciones_listado)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 221, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layout_lista = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.layout_lista.setContentsMargins(0, 0, 0, 0)
        self.layout_lista.setObjectName("layout_lista")
        self.boton_listar = QtWidgets.QPushButton(self.layoutWidget2)
        self.boton_listar.setMinimumSize(QtCore.QSize(45, 45))
        self.boton_listar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_listar.setStyleSheet("background-color: rgb(46, 52, 54);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imagenes/listar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_listar.setIcon(icon5)
        self.boton_listar.setIconSize(QtCore.QSize(44, 44))
        self.boton_listar.setAutoDefault(False)
        self.boton_listar.setObjectName("boton_listar")
        self.layout_lista.addWidget(self.boton_listar)
        self.combo_listar = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo_listar.setMinimumSize(QtCore.QSize(120, 30))
        self.combo_listar.setMaximumSize(QtCore.QSize(120, 30))
        self.combo_listar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.combo_listar.setObjectName("combo_listar")
        self.combo_listar.addItem("")
        self.combo_listar.addItem("")
        self.combo_listar.addItem("")
        self.layout_lista.addWidget(self.combo_listar)

        self.retranslateUi(widget_principal)
        QtCore.QMetaObject.connectSlotsByName(widget_principal)

    def retranslateUi(self, widget_principal):
        _translate = QtCore.QCoreApplication.translate
        widget_principal.setWindowTitle(_translate("widget_principal", "Guia Telefonica"))
        self.box_listado.setTitle(_translate("widget_principal", "Listado"))
        item = self.tabla_listado.horizontalHeaderItem(0)
        item.setText(_translate("widget_principal", "Nombre"))
        item = self.tabla_listado.horizontalHeaderItem(1)
        item.setText(_translate("widget_principal", "Apellido"))
        item = self.tabla_listado.horizontalHeaderItem(2)
        item.setText(_translate("widget_principal", "Localidad"))
        item = self.tabla_listado.horizontalHeaderItem(3)
        item.setText(_translate("widget_principal", "Dirección"))
        item = self.tabla_listado.horizontalHeaderItem(4)
        item.setText(_translate("widget_principal", "Numero de Telefono"))
        self.box_operaciones.setTitle(_translate("widget_principal", "Operaciones"))
        self.combo_buscar.setItemText(0, _translate("widget_principal", "Nombre"))
        self.combo_buscar.setItemText(1, _translate("widget_principal", "Apellido"))
        self.combo_buscar.setItemText(2, _translate("widget_principal", "Telefono"))
        self.combo_buscar.setItemText(3, _translate("widget_principal", "DNI"))
        self.box_campos.setTitle(_translate("widget_principal", "Campos"))
        self.input_nombre.setPlaceholderText(_translate("widget_principal", "Nombre"))
        self.input_apellido.setPlaceholderText(_translate("widget_principal", "Apellido"))
        self.input_direccion.setPlaceholderText(_translate("widget_principal", "Dirección"))
        self.input_caracteristica.setPlaceholderText(_translate("widget_principal", "Caracteristica"))
        self.label_guion.setText(_translate("widget_principal", "-"))
        self.input_telefono.setPlaceholderText(_translate("widget_principal", "Numero"))
        self.input_localidad.setPlaceholderText(_translate("widget_principal", "Localidad"))
        self.box_avisos.setTitle(_translate("widget_principal", "Avisos"))
        self.box_operaciones_listado.setTitle(_translate("widget_principal", "Listado"))
        self.combo_listar.setItemText(0, _translate("widget_principal", "Caracteristica"))
        self.combo_listar.setItemText(1, _translate("widget_principal", "Apellido"))
        self.combo_listar.setItemText(2, _translate("widget_principal", "Localidad"))


from recursos import imagenes_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget_principal = QtWidgets.QWidget()
    ui = Ui_widget_principal()
    ui.setupUi(widget_principal)
    widget_principal.show()
    sys.exit(app.exec_())

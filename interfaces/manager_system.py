from interfaces.a.manager import Ui_Manager,QMainWindow,Qt,QTableWidget,QHeaderView,QTableWidgetItem
from modules.configs.config import error

class Manager_app(Ui_Manager,QMainWindow):
    def __init__(self,user,parent=None):
        self.user = user
        super().__init__(parent)
        super().setupUi(self)

        #Config interface

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(.9)
        self.sidebar.setFixedWidth(0)
        self.width_bar = 0
        self.QStackedWidget.setCurrentWidget(self.main_page)
        self.setFixedSize(860,450)
        self.EditText_welcome.setText(f'Seja Bem-Vindo, {self.user.conta[3]}!')

        #Init Values
        self.table_gastos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_gastos.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.Table_lucros.setEditTriggers(QTableWidget.NoEditTriggers)
        self.Table_lucros.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.EditText_current_salario_home.setText(self.convert(self.user.conta[5]))
        self.EditText_current_salario2.setText(self.convert(self.user.conta[5]))
        self.refresh_gastos()
        self.refresh_lucros()
        self.sum_all()

        # Buttons
        self.btn_refresh_page_home.clicked.connect(lambda:(self.refresh_gastos(),self.refresh_lucros(),self.sum_all()))
        self.btn_quit_main_home.clicked.connect(lambda: self.close())
        self.btn_add_page_gastos.clicked.connect(lambda: self.QStackedWidget.setCurrentWidget(self.page_edit_gastos))
        self.btn_add_page_lucros.clicked.connect(lambda: self.QStackedWidget.setCurrentWidget(self.page_edit_lucros))
        self.btn_return_page_editgasto.clicked.connect(self.goto_page_gastos)
        self.btn_return_page_editlucro.clicked.connect(self.goto_page_lucros)
        self.btn_return_page_editsalario.clicked.connect(lambda: self.QStackedWidget.setCurrentWidget(self.main_page))

        #Edit values
        self.btn_update_page_editsalario.clicked.connect(self.update_salario)
        self.btn_update_page_editlucro.clicked.connect(self.add_lucro)
        self.btn_remove_page_lucros.clicked.connect(self.remove_lucro)
        self.btn_update_page_editgasto.clicked.connect(self.add_gasto)
        self.btn_remove_page_gastos.clicked.connect(self.remove_gasto)

        #Sidebar
        self.pushButton.clicked.connect(self.sidebar_size)
        self.btn_home.clicked.connect(lambda: (self.QStackedWidget.setCurrentWidget(self.main_page)))
        self.btn_page_salario.clicked.connect(lambda: self.QStackedWidget.setCurrentWidget(self.page_edit_salario))
        self.btn_page_gastos.clicked.connect(self.goto_page_gastos)
        self.btn_page_lucros.clicked.connect(self.goto_page_lucros)
    def sidebar_size(self):
        if self.width_bar == 0:
            self.sidebar.setFixedWidth(100)
            self.width_bar = 1
        else:
            self.sidebar.setFixedWidth(0)
            self.width_bar = 0


    def sum_all(self):
        total_gastos = 0
        total_lucros = 0
        for gasto in self.list_gastos:
            total_gastos += gasto
        for lucro in self.list_lucros:
            total_lucros += lucro
        self.EditText_current_credit_home.setText(self.convert(self.user.conta[5] + total_lucros - total_gastos))



        #Gastos
    def goto_page_gastos(self):
        self.QStackedWidget.setCurrentWidget(self.page_gastos)
        self.refresh_gastos()
    def refresh_gastos(self):
        self.list_gastos = []
        self.gastos = self.user.list_gastos()
        self.table_gastos.setRowCount(len(self.gastos))
        if len(self.gastos) == 0:
            valor = 0
        for row , gasto in enumerate(self.gastos):
            self.table_gastos.setItem(row,0,QTableWidgetItem(gasto[1]))
            self.table_gastos.setItem(row,1,QTableWidgetItem(self.convert(gasto[2])))
            self.list_gastos.append(gasto[2])
            valor = 0
            for gasto in self.list_gastos:
                valor += gasto
        self.EditText_current_gasto_home.setText(self.convert(valor))
    def add_gasto(self):
        if self.EditText_value_editgasto.text() == '':
            self.EditText_info_gasto.setText("Preencha todos os campos!")
            return
        valor =  self.EditText_value_editgasto.text()
        valor = self.user.tofloat(valor)
        self.user.add_gasto(
            self.EditText_desc_editgasto.text(),
            valor,
            self.user.ID_user
        )
        self.EditText_info_gasto.setText(f"Adicionado gasto no valor de {self.convert(valor)}")
    def remove_gasto(self):
        try:
            self.gastos = self.user.list_gastos()
            number = self.table_gastos.currentIndex().row()
            if number == -1:
                return
            self.user.remove_gasto(self.gastos[number][0])
            self.refresh_gastos()
        except IndexError as erro:
            error(erro)
        except Exception as erro:
            error(erro)
      
    #Lucros
    def goto_page_lucros(self):
        self.QStackedWidget.setCurrentWidget(self.page_lucros)
        self.refresh_lucros()
    def refresh_lucros(self):
        
        self.list_lucros = []
        self.lucros = self.user.list_lucros()
        self.Table_lucros.setRowCount(len(self.lucros))
        if len(self.lucros) == 0:
            valor = 0
        for row , lucro in enumerate(self.lucros):
            self.Table_lucros.setItem(row,0,QTableWidgetItem(lucro[1]))
            self.Table_lucros.setItem(row,1,QTableWidgetItem(self.convert(lucro[2])))
            self.list_lucros.append(lucro[2])
            valor = 0
            for lucro in self.list_lucros:
                valor += lucro
        self.EditText_current_lucros_home.setText(self.convert(valor))
    def add_lucro(self):
        if self.EditText_value_editlucro.text() == '':
            self.EditText_info_lucro.setText("Preencha todos os campos!")
            return
        valor =  self.EditText_value_editlucro.text()
        valor = self.user.tofloat(valor)
        self.user.add_lucro(
            self.EditText_desc_editlucro.text(),
            valor,
            self.user.ID_user
        )
        self.EditText_info_lucro.setText(f"Adicionado lucro no valor de {self.convert(valor)}")
    def remove_lucro(self):
        try:
            self.lucros = self.user.list_lucros()
            number = self.Table_lucros.currentIndex().row()
            if number == -1:
                return
            self.user.remove_lucro(self.lucros[number][0])
            self.refresh_lucros()
        except IndexError as erro:
            error(erro)
        except Exception as erro:
            error(erro)
      
    
    #Functions
    @staticmethod
    def convert(valor):
        valor = float(valor)
        valor = f"R$ {valor:.2f}"
        return valor.replace('.',',')
    def update_salario(self):
        self.user.update_salario(self.user.tofloat(self.EditText_salario_update.text()))
        self.user.refresh_salario()
        self.EditText_current_salario2.setText(f"{self.convert(self.user.conta[5])}")
        self.EditText_current_salario_home.setText(f"{self.convert(self.user.conta[5])}")
        



    #Move Window
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except Exception:
            pass
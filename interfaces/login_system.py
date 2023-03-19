from interfaces.a.login_window import Ui_login_window,QMainWindow,Qt
from modules.system.main_system import Usuario
from interfaces.manager_system import Manager_app

user = Usuario()

class Login_panel(Ui_login_window,QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        #Config Window
        self.setFixedSize(493,351)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(.9)

        #Config Buttons
        self.btn_close.clicked.connect(self.close)
        self.btn_quit.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_login.clicked.connect(self.login)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except Exception:
            pass
    
    

    def login(self):

        user.login(self.Textinput_user.text(),self.Textinput_password.text())


        if user.ID_user != None and user.ID_user != '':
            self.interface = Manager_app(user=user)
            self.interface.show()
            self.close()

   
        else:
            self.Textinput_loginmessage.setText("Usuário Ou Senha Incorretos")
            self.Textinput_loginmessage.setStyleSheet("color: red;")
        
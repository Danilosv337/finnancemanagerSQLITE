from PySide6.QtWidgets import QApplication
from sys import argv 



qt = QApplication(argv)

from interfaces.login_system import Login_panel
login = Login_panel()
login.show()
qt.exec()
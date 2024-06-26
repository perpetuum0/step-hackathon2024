from PySide6.QtGui import QIcon, QAction, QMouseEvent,QPixmap,QPalette
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,QDialog,QLineEdit,QStackedWidget,QMessageBox,\
    QSizePolicy,QMainWindow, QHBoxLayout,QStackedWidget,QLabel
from PySide6.QtCore import Signal, QObject ,QSize,Qt
import db
from encryptor import encrypt
from log import log
class Authorization:
    def signup(username, password) -> bool:
        if not db.check_user(username):
            db.add_user(username, encrypt(password))
            log("User created with username: "+username)
            return True
        else:
            return False
    
    def login(username, password) -> bool:
        if encrypt(password)==db.get_user_password(username):
            log("Succesfull login on user '{}'".format(username))
            return True
        else:
            log("Log in attempt on user '{}'".format(username))
            return False

class HyperlinkLabel(QLabel):
    clicked = Signal()
    
    def __init__(self, text:str, parent:QWidget):
        super(HyperlinkLabel, self).__init__(parent)
        self.setText(f"<a href='nowhere.com'>{text}</a>")
    
    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked.emit()
        return super().mouseReleaseEvent(ev)

class AuthDialog(QWidget):
    done = Signal(str)
    
    def __init__(self):
        super(AuthDialog, self).__init__()
        self.setMaximumSize(330,370)
        self.setMinimumSize(250,330)
        self.resize(300,370)
        
        self.authForms = QStackedWidget(self)
        self.currentFormIndex = 0
        self.loginForm = LoginForm(self.authForms)
        self.loginForm.newAccountButton.clicked.connect(self.switchForm)
        self.signupForm = SignupForm(self.authForms)
        self.signupForm.newAccountButton.clicked.connect(self.switchForm)
        self.signupForm.done.connect(self.switchForm)
        self.loginForm.done.connect(self.loginDone)
        self.authForms.addWidget(self.loginForm)
        self.authForms.addWidget(self.signupForm)
        self.authForms.setCurrentWidget(self.loginForm)
        
        self.authForms.setMinimumSize(250,270)
        self.layout_ = QHBoxLayout(self)
        self.layout_.setContentsMargins(0,0,0,0)
        self.layout_.setSpacing(0)
        self.layout_.addWidget(self.authForms)
        self.layout_.setAlignment(self.authForms, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)
    
    def switchForm(self):
        self.currentFormIndex = self.currentFormIndex + (1 if self.currentFormIndex == 0 else -1)
        self.authForms.setCurrentIndex(self.currentFormIndex)
        
    def loginDone(self,str):
        self.hide()
        self.done.emit(str)
class SignupForm(QWidget):
    done = Signal()
    def __init__(self,parent:QWidget):
        super(SignupForm, self).__init__(parent)
        self.messageBox = QMessageBox(self)
        self.usernameInput = QLineEdit(self)
        self.usernameInput.setPlaceholderText("Введите имя пользователя")
        self.usernameLabel = QLabel("Имя пользователя",self)
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setPlaceholderText("Введите пароль")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLabel = QLabel("Пароль",self)
        self.passwordConfirmInput = QLineEdit(self)
        self.passwordConfirmInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordConfirmInput.setPlaceholderText("Снова введите пароль")
        self.passwordConfirmLabel = QLabel("Повторите пароль",self)
        self.signupButton = QPushButton("Зарегистрироваться", self)
        self.signupButton.clicked.connect(self.signupAttempt)
        self.signupButton.setMinimumSize(180,24)
        self.newAccountButton = HyperlinkLabel("Уже зарегистрированы?",self)
        self.signupButton.setMinimumHeight(24)
        
        self.layout_ = QVBoxLayout(self)
        self.layout_.setSpacing(5)
        self.layout_.addWidget(self.usernameLabel)
        self.layout_.addWidget(self.usernameInput)
        self.layout_.addSpacing(10)
        self.layout_.addWidget(self.passwordLabel)
        self.layout_.addWidget(self.passwordInput)
        self.layout_.addSpacing(10)
        self.layout_.addWidget(self.passwordConfirmLabel)
        self.layout_.addWidget(self.passwordConfirmInput)
        self.layout_.addSpacing(15)
        self.layout_.addWidget(self.signupButton)
        self.layout_.setAlignment(self.signupButton, Qt.AlignmentFlag.AlignCenter)
        self.layout_.addSpacing(5)
        self.layout_.addWidget(self.newAccountButton)
        self.layout_.setAlignment(self.newAccountButton, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)
        
    def signupAttempt(self):
        if not self.usernameInput.text():
            self.messageBox.warning(self,"Ошибка", "Введите имя пользователя!")
        elif not self.passwordInput.text():
            self.messageBox.warning(self,"Ошибка", "Введите пароль!")
        elif self.passwordInput.text() != self.passwordConfirmInput.text():
            self.messageBox.warning(self,"Ошибка", "Пароли не совпадают.",QMessageBox.StandardButton.Ok)
        else:
            if Authorization.signup(
                self.usernameInput.text(),
                self.passwordInput.text()
            ):
                self.messageBox.information(self, "Регистрация", "Вы успешно зарегистрировались!", QMessageBox.StandardButton.Ok)
                self.done.emit()
                self.usernameInput.setText("")
                self.passwordInput.setText("")
                self.passwordConfirmInput.setText("")
            else:
                self.messageBox.warning(self,"Ошибка", "Аккаунт с таким именем пользователя уже существует.",QMessageBox.StandardButton.Ok)
class LoginForm(QWidget):
    done=Signal(str)
    
    def __init__(self,parent:QWidget):
        super(LoginForm, self).__init__(parent)
        
        self.messageBox = QMessageBox(self)
        self.usernameInput = QLineEdit(self)
        self.usernameInput.setPlaceholderText("Введите имя пользователя")
        self.usernameLabel = QLabel("Имя пользователя",self)
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordInput.setPlaceholderText("Введите пароль")
        self.passwordLabel = QLabel("Пароль",self)
        self.loginButton = QPushButton("Войти",self)
        self.loginButton.setMinimumSize(100,24)
        self.loginButton.clicked.connect(self.loginAttempt)
        self.newAccountButton = HyperlinkLabel("Нет аккаунта?",self)
        self.layout_ = QVBoxLayout(self)
        self.layout_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_.setSpacing(5)
        self.layout_.addWidget(self.usernameLabel)
        self.layout_.addWidget(self.usernameInput)
        self.layout_.addSpacing(10)
        self.layout_.addWidget(self.passwordLabel)
        self.layout_.addWidget(self.passwordInput)
        self.layout_.addSpacing(15)
        self.layout_.addWidget(self.loginButton)
        self.layout_.setAlignment(self.loginButton, Qt.AlignmentFlag.AlignCenter)
        self.layout_.addSpacing(5)
        self.layout_.addWidget(self.newAccountButton)
        self.layout_.setAlignment(self.newAccountButton, Qt.AlignmentFlag.AlignCenter)
        
        
        self.setLayout(self.layout_)
        
    def loginAttempt(self):
        if not self.usernameInput.text():
            self.messageBox.warning(self,"Ошибка", "Введите имя пользователя!")
        elif not self.passwordInput.text():
            self.messageBox.warning(self,"Ошибка", "Введите пароль!")
        else:
            if Authorization.login(
                self.usernameInput.text(),
                self.passwordInput.text()
            ):
                self.messageBox.information(self, "Вход в аккаунт", "Вы успешно вошли в аккаунт!", QMessageBox.StandardButton.Ok)
                self.done.emit(self.usernameInput.text())
                self.usernameInput.setText("")
                self.passwordInput.setText("")
            else:
                self.messageBox.warning(self,"Ошибка", "Вы ввели неверные данные для входа.",QMessageBox.StandardButton.Ok)
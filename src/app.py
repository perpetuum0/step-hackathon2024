from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,\
    QSizePolicy,QMainWindow, QHBoxLayout,QStackedWidget,QLabel
from PySide6.QtCore import Signal, QObject ,QSize,Qt

from encryptor import EncryptorTab
from keygen import KeygenTab
from user_guide import InfoTab
from authorization import AuthDialog
from typings import *

class KeyManager(QMainWindow):
    def __init__(self) -> None:
        super(KeyManager, self).__init__()
        self.setFont("Helvetica")
        self.setWindowTitle("Steps with a Shield")
        self.setMinimumSize(QSize(650, 350))
        self.resize(QSize(810,490))
        
        
        #Widgets
        self.authDialog = AuthDialog()
        self.centralWidget_ = QWidget()
        self.centralWidget_.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)
        self.contentsWidget = QStackedWidget()
        
        self.sidebar = QLabel(self.centralWidget_)
        self.sidebar.setStyleSheet("background-color: #26467D")
        self.sidebar.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)
        self.sidebar.setMaximumWidth(250)
        self.sidebarItemsBox = QWidget(self.sidebar)
        
        self.infoButton = SidebarButton(SidebarButtons.Info, self.sidebarItemsBox)
        self.infoButton.setChecked(True)
        self.keygenButton = SidebarButton(SidebarButtons.Keygen, self.sidebarItemsBox)
        self.encryptorButton = SidebarButton(SidebarButtons.Encryptor, self.sidebarItemsBox)
        self.infoButton.clicked.connect(
            lambda: self.sidebarButtonClicked(self.infoButton)
        )
        self.keygenButton.clicked.connect(
            lambda: self.sidebarButtonClicked(self.keygenButton)
        )
        self.encryptorButton.clicked.connect(
            lambda: self.sidebarButtonClicked(self.encryptorButton)
        )
        self.authButton = SidebarButton(SidebarButtons.Authorization, self.sidebar)
        self.authButton.clicked.connect(self.authButtonClicked)
        
        self.infoTab = InfoTab(self.contentsWidget)
        self.encryptorTab = EncryptorTab(self.contentsWidget)
        self.keygenTab = KeygenTab(self.contentsWidget)
        self.contentsWidget.addWidget(self.infoTab)
        self.contentsWidget.addWidget(self.encryptorTab)
        self.contentsWidget.addWidget(self.keygenTab)
        #Sidebar
        self.sidebarItemsLayout = QVBoxLayout(self.sidebarItemsBox)
        self.sidebarItemsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sidebarItemsLayout.setSpacing(5)
        self.sidebarItemsLayout.setContentsMargins(0,0,0,0)
        self.sidebarItemsLayout.addWidget(self.infoButton)
        self.sidebarItemsLayout.addWidget(self.encryptorButton)
        self.sidebarItemsLayout.addWidget(self.keygenButton)
        
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.addWidget(self.sidebarItemsBox)
        self.sidebarLayout.addWidget(self.authButton)
        self.sidebarLayout.setAlignment(self.authButton, Qt.AlignmentFlag.AlignBottom)
        self.sidebarLayout.setContentsMargins(8,8,8,8)
        self.sidebarLayout.setSpacing(0)
        self.sidebar.setLayout(self.sidebarLayout)

        
        #Central 
        self.windowLayout = QHBoxLayout(self.centralWidget_)
        self.windowLayout.addWidget(self.sidebar)
        self.windowLayout.setStretch(0,1)
        self.windowLayout.addWidget(self.contentsWidget)
        self.windowLayout.setStretch(1,2)
        self.windowLayout.setContentsMargins(0,0,0,0)
        self.windowLayout.setSpacing(0)
        self.centralWidget_.setLayout(self.windowLayout)
        self.setCentralWidget(self.centralWidget_)
        
        self.show()
        
    def authButtonClicked(self):
        self.authDialog.show()
        self.authDialog.raise_()
        
    def sidebarButtonClicked(self, button:QPushButton):
        button.setEnabled(False)
        for btn in self.sidebarItemsBox.findChildren(QPushButton):
            if btn!=button:
                btn.setEnabled(True)
                btn.setChecked(False)
        
        buttonTab: Tabs
        match button:
            case self.infoButton:
                buttonTab = Tabs.Info
            case self.keygenButton:
                buttonTab = Tabs.Keygen
            case self.encryptorButton:
                buttonTab = Tabs.Encryptor
        self.switchToTab(button.buttonType.value)

    def switchToTab(self, tab: Tabs):
        match tab:
            case Tabs.Info:
                self.contentsWidget.setCurrentWidget(self.infoTab)
            case Tabs.Keygen:
                self.contentsWidget.setCurrentWidget(self.keygenTab)
            case Tabs.Encryptor:
                self.contentsWidget.setCurrentWidget(self.encryptorTab)
        pass
    


class SidebarButton(QPushButton):
    buttonType: SidebarButtons
    style = """
    QPushButton {
        color: white;
        border-radius:5px;
        border:none;
        font-weight:600;
        font-size:14px;
        text-align:left;
        height:100px;
    }
    QPushButton:hover { background-color:#2B5091 }
    QPushButton:checked { background-color:#3464B6; border:none }
    QPushButton:pressed {background-color:#3464B6; border:none }
            """
    
    def __init__(self,btnType: SidebarButtons,parent:QWidget):
        super(SidebarButton, self).__init__(parent)
        self.buttonType = btnType
        self.setFixedHeight(50)
        self.setFlat(True)
        self.setStyleSheet(self.style)
        self.setCheckable(True)
        self.setIconSize(QSize(25,25))
        # self.layout().setContentsMargins(10,0,0,0)
        match btnType:
            case SidebarButtons.Info:
                self.setText("Информация")
                self.setIcon(QIcon("resources/infoIcon.png"))
            case SidebarButtons.Keygen:
                self.setText("Генератор паролей")
                self.setIcon(QIcon("resources/keygenIcon.png"))
            case SidebarButtons.Encryptor:
                self.setIcon(QIcon("resources/encryptIcon.png"))
                self.setText("Шифратор")
            case SidebarButtons.Authorization:
                self.setIcon(QIcon("resources/loginIcon.png"))
                self.setText("Войти в аккаунт")
                # self.setStyleSheet("""color:white;
                #                     QPushButton:checked { background-color:#3464B6; border:none}""")
                self.setCheckable(False)
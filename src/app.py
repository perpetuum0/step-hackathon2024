from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,\
    QSizePolicy,QMainWindow, QHBoxLayout,QStackedWidget,QLabel
from PySide6.QtCore import Signal, QObject ,QSize,Qt

from encryptor import EncryptorTab
from keygen import KeygenTab
from user_guide import InfoTab
from typings import *

class KeyManager(QMainWindow):
    def __init__(self) -> None:
        super(KeyManager, self).__init__()
        self.setWindowTitle("Steps with a Shield")
        self.setMinimumSize(QSize(650, 350))
        self.resize(QSize(730,440))
        
        
        #Widgets
        self.centralWidget_ = QWidget()
        self.centralWidget_.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)
        self.contentsWidget = QStackedWidget()
        
        self.sidebar = QLabel(self.centralWidget_)
        self.sidebar.setStyleSheet("background-color: #1f3a68")
        self.sidebar.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)
        self.sidebar.setMaximumWidth(250)
        self.infoButton = QPushButton("Информация", self.sidebar)
        self.keygenButton = QPushButton("Генератор", self.sidebar) 
        self.encryptorButton = QPushButton("Шифратор", self.sidebar)
        self.infoButton.clicked.connect(lambda: self.switchToTab(Tabs.Info))
        self.keygenButton.clicked.connect(lambda: self.switchToTab(Tabs.Keygen))
        self.encryptorButton.clicked.connect(lambda: self.switchToTab(Tabs.Encryptor))
        self.logoutButton = QPushButton("Выйти из аккаунта", self.sidebar)
        
        self.infoTab = InfoTab(self.contentsWidget)
        self.encryptorTab = EncryptorTab(self.contentsWidget)
        self.keygenTab = KeygenTab(self.contentsWidget)
        self.contentsWidget.addWidget(self.infoTab)
        self.contentsWidget.addWidget(self.encryptorTab)
        self.contentsWidget.addWidget(self.keygenTab)
        #Sidebar
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sidebarLayout.addWidget(self.infoButton)
        self.sidebarLayout.addWidget(self.keygenButton)
        self.sidebarLayout.addWidget(self.encryptorButton)
        self.sidebarLayout.addWidget(self.logoutButton, alignment=Qt.AlignmentFlag.AlignBottom)
        self.sidebarLayout.setContentsMargins(25,25,25,20)
        self.sidebarLayout.setSpacing(25)
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
        
    def switchToTab(self, tab: Tabs):
        match tab:
            case Tabs.Info:
                self.contentsWidget.setCurrentWidget(self.infoTab)
            case Tabs.Keygen:
                self.contentsWidget.setCurrentWidget(self.keygenTab)
            case Tabs.Encryptor:
                self.contentsWidget.setCurrentWidget(self.encryptorTab)
        pass
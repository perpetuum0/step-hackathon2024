from PySide6.QtGui import QIcon, QAction,QPixmap,QIntValidator,QClipboard
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,QSizePolicy,QMainWindow, \
QHBoxLayout, QLabel, QButtonGroup,QRadioButton, QGridLayout,QLineEdit,QScrollArea,QCheckBox,QSpinBox
from PySide6.QtCore import Signal, QObject ,QSize, Qt
from log import log

class InfoTab(QWidget):
    article_path = "./resources/article.html"
    
    def __init__(self,parent) -> None:
        super(InfoTab, self).__init__(parent)
        self.infoTextArea = QScrollArea(self)
        self.infoBox = QWidget(self.infoTextArea)
        self.infoText = QLabel(self.infoBox)
        self.infoText.setStyleSheet("font-size:14px")
        # self.infoText.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.infoText.setWordWrap(True)
        self.infoText.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.infoTextArea.setWidget(self.infoBox)
        self.infoTextArea.setStyleSheet("border:none")
        self.infoTextArea.setWidgetResizable(True)
        
        try:
            with open(self.article_path, "r") as article:
                self.infoText.setText(article.read())
        except FileNotFoundError:
            log("user_guide.py: article file not found at", self.article_path)
        #Layouts
        infoBoxLayout = QVBoxLayout(self.infoBox)
        infoBoxLayout.addWidget(self.infoText)
        
        self.layout_ = QVBoxLayout()
        self.layout_.addWidget(self.infoTextArea, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)

class GuideDialog(QWidget):
    article_path = "./resources/user_guide.html"
    
    def __init__(self) -> None:
        super(GuideDialog, self).__init__()
        self.setMinimumSize(260,285)
        self.infoTextArea = QScrollArea(self)
        self.infoTextArea.setStyleSheet("border:none")
        self.infoTextArea.setWidgetResizable(True)
        
        self.infoText = QLabel(self.infoTextArea)
        self.infoText.setWordWrap(True)
        self.infoText.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.infoTextArea.setWidget(self.infoText)
        
        
        self.layout_ = QVBoxLayout()
        self.layout_.addWidget(self.infoTextArea, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)
        
        try:
            with open(self.article_path, "r") as article:
                self.infoText.setText(article.read())
        except FileNotFoundError:
            log("user_guide.py: article file not found at", self.article_path)
        # self.infoBox = QWidget(self.infoTextArea)
        # self.infoText = QLabel(self.infoBox)
        # self.infoText.setStyleSheet("font-size:14px")
        
        # self.infoTextArea.setWidget(self.infoBox)
        # self.infoTextArea.setStyleSheet("border:none")
        # self.infoTextArea.setWidgetResizable(True)
        
        # try:
        #     with open(self.article_path, "r") as article:
        #         self.infoText.setText(article.read())
        # except FileNotFoundError:
        #     log("user_guide.py: article file not found at", self.article_path)
        # #Layouts
        # infoBoxLayout = QVBoxLayout(self.infoBox)
        # infoBoxLayout.addWidget(self.infoText)
        
        
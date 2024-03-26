from PySide6.QtGui import QIcon, QAction,QPixmap,QIntValidator,QClipboard
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,QSizePolicy,QMainWindow, \
QHBoxLayout, QLabel, QButtonGroup,QRadioButton, QGridLayout,QLineEdit,QScrollArea,QCheckBox,QSpinBox
from PySide6.QtCore import Signal, QObject ,QSize, Qt

class InfoTab(QWidget):
    def __init__(self,parent) -> None:
        super(InfoTab, self).__init__(parent)
        self.infoTextArea = QScrollArea(self)
        self.infoBox = QWidget(self.infoTextArea)
        
        self.infoText = QLabel(self.infoBox)
        self.infoText.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.infoText.setWordWrap(True)
        
        self.infoTextArea.setWidget(self.infoBox)
        self.infoTextArea.setStyleSheet("border:none")
        self.infoTextArea.setWidgetResizable(True)
        
        #TODO error handling
        with open("./resources/info.txt", "r") as article:
            self.infoText.setText(article.read())
            
        #Layouts
        infoBoxLayout = QVBoxLayout(self.infoBox)
        infoBoxLayout.addWidget(self.infoText)
        
        self.layout_ = QVBoxLayout()
        self.layout_.addWidget(self.infoTextArea, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_)



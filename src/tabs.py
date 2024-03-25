from PySide6.QtGui import QIcon, QAction,QPixmap,QIntValidator
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget,QPushButton,QSizePolicy,QMainWindow, \
QHBoxLayout, QLabel, QButtonGroup,QRadioButton, QGridLayout,QLineEdit,QScrollArea,QCheckBox,QSpinBox
from PySide6.QtCore import Signal, QObject ,QSize, Qt

class InformationTab(QWidget):
    def __init__(self,parent) -> None:
        super(InformationTab, self).__init__(parent)
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

class EncryptorTab(QWidget):
    def __init__(self,parent) -> None:
        super(EncryptorTab, self).__init__(parent)
        # self.setStyleSheet("background-color: blue")
        self.infoText = QLabel(self)
        self.infoText.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tristique lobortis dui, venenatis scelerisque dolor sagittis at. Vivamus lacus massa, pharetra id mollis sed, mattis venenatis ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eros metus, condimentum ac pellentesque quis, dapibus eget lorem. Aenean ut aliquet libero, non efficitur odio.")
        self.infoText.setWordWrap(True)
        # self.infoText.setMinimumHeight(100)
        
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Введите текст для шифровки")
        
        self.inputButton = QPushButton("Зашифровать", self)
        self.inputButton.setFixedWidth(200)
        
        self.encryptionSelectBox = QWidget(self)
        self.sha256Button = QRadioButton("sha-256", self.encryptionSelectBox)
        self.sha256Button.setChecked(True)
        self.sha512Button = QRadioButton("sha-512",self.encryptionSelectBox)
        self.TupleHash128Button = QRadioButton("TupleHash128", self.encryptionSelectBox)
        self.TupleHash256Button = QRadioButton("TupleHash256", self.encryptionSelectBox)
        self.BLAKE2sButton = QRadioButton("BLAKE2s", self.encryptionSelectBox)
        self.BLAKE2bButton = QRadioButton("BLAKE2b", self.encryptionSelectBox)
        
        self.buttonGroup = QButtonGroup(self.encryptionSelectBox)
        self.buttonGroup.addButton(self.sha256Button)
        self.buttonGroup.addButton(self.sha512Button)
        self.buttonGroup.addButton(self.TupleHash128Button)
        self.buttonGroup.addButton(self.TupleHash256Button)
        self.buttonGroup.addButton(self.BLAKE2bButton)
        self.buttonGroup.addButton(self.BLAKE2sButton)
        
        self.resultBox = QWidget(self)
        self.resultLabelBox = QWidget(self.resultBox)
        self.resultLabel = QLabel("Результат:", self.resultLabelBox)
        self.resultCopyButton = QPushButton("Скопировать",self.resultLabelBox)
        self.resultTextField = QTextEdit("Здесь появится зашифрованный текст...")
        self.resultTextField.setReadOnly(True)
        
        self.resultLabelBoxLayout = QVBoxLayout(self.resultLabelBox)
        self.resultLabelBoxLayout.addWidget(self.resultLabel)
        self.resultLabelBoxLayout.setAlignment(self.resultLabel, Qt.AlignmentFlag.AlignCenter)
        self.resultLabelBoxLayout.addWidget(self.resultCopyButton)
        self.resultBoxLayout = QHBoxLayout(self.resultBox)
        self.resultBoxLayout.addWidget(self.resultLabelBox)
        self.resultBoxLayout.addWidget(self.resultTextField)
        
        self.selectBoxLayout = QGridLayout(self.encryptionSelectBox)
        # self.encryptionSelectBoxLayout = QHBoxLayout(self.encryptionSelectBox)
        self.selectBoxLayout.addWidget(self.sha256Button, 0,1)
        self.selectBoxLayout.addWidget(self.sha512Button, 1,1)
        self.selectBoxLayout.addWidget(self.TupleHash128Button, 0,2)
        self.selectBoxLayout.addWidget(self.TupleHash256Button,1,2)
        self.selectBoxLayout.addWidget(self.BLAKE2bButton,0,3)
        self.selectBoxLayout.addWidget(self.BLAKE2sButton,1,3)
        
        self.layout_ = QVBoxLayout(self)
        self.layout_.addWidget(self.infoText)
        # self.layout_.setStretch(0,1.5)
        self.layout_.addWidget(self.inputField)
        # self.layout_.setStretch(1,1)
        self.layout_.addWidget(self.inputButton)
        self.layout_.setAlignment(self.inputButton, Qt.AlignmentFlag.AlignCenter)
        # self.layout_.setStretch(2,1)
        self.layout_.addWidget(self.encryptionSelectBox)
        # self.layout_.setStretch(3,0.5)
        self.layout_.addWidget(self.resultBox)
        # self.layout_.setStretch(4,1)
        
        self.setLayout(self.layout_)

class KeygenTab(QWidget):
    def __init__(self,parent) -> None:
        super(KeygenTab, self).__init__(parent)
        self.infoText = QLabel(self)
        self.infoText.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tristique lobortis dui, venenatis scelerisque dolor sagittis at. Vivamus lacus massa, pharetra id mollis sed, mattis venenatis ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eros metus, condimentum ac pellentesque quis, dapibus eget lorem. Aenean ut aliquet libero, non efficitur odio.")
        self.infoText.setWordWrap(True)
        
        self.lengthBox = QWidget(self)
        self.lengthLabel = QLabel(self.lengthBox)
        self.lengthLabel.setText("Длина пароля")
        self.lengthInput = QSpinBox(self.lengthBox)
        self.lengthInput.setValue(12)
        # self.lengthSlider TODO:
        
        self.optionsBox = QWidget(self)
        self.uppercaseCheckbox = QCheckBox("Верхний регистр",self.optionsBox)
        self.lowercaseCheckbox = QCheckBox("Нижний регистр",self.optionsBox)
        self.digitsCheckbox = QCheckBox("Цифры", self.optionsBox)
        self.symbolsCheckbox = QCheckBox("Специальные символы",self.optionsBox)
        
        self.generatorBox=QWidget(self)
        self.generateButton=QPushButton("Сгенерировать", self.generatorBox)
        self.generateField=QLineEdit(self.generatorBox)
        self.generateField.setPlaceholderText("Здесь будет ваш сгенерированный пароль...")
        self.generateField.setReadOnly(True)
        self.copyButton=QPushButton("КП",self.generatorBox)

        ##Layouts
        self.lengthBoxLayout = QHBoxLayout(self.lengthBox)
        self.lengthBoxLayout.addWidget(self.lengthLabel)
        self.lengthBoxLayout.addWidget(self.lengthInput)
        # TODO self.lengthBoxLayout.addWidget(self.lenghtSlider)
        
        self.optionsBoxLayout = QGridLayout(self.optionsBox)
        self.optionsBoxLayout.setSpacing(10)
        self.optionsBoxLayout.addWidget(self.lowercaseCheckbox)
        self.optionsBoxLayout.addWidget(self.uppercaseCheckbox)
        self.optionsBoxLayout.addWidget(self.digitsCheckbox,0,2)
        self.optionsBoxLayout.addWidget(self.symbolsCheckbox,1,2)
        
        self.generatorBoxLayout = QHBoxLayout(self.generatorBox)
        self.generatorBoxLayout.addWidget(self.generateButton)
        self.generatorBoxLayout.addWidget(self.generateField)
        self.generatorBoxLayout.addWidget(self.copyButton)
        
        
        self.infoText.setMinimumHeight(100)
        self.layout_ = QVBoxLayout(self)
        self.layout_.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.layout_.setContentsMargins(15,15,15,100)
        # self.layout_.setContentsMargins()
        self.layout_.addWidget(self.infoText)
        # self.layout_.setStretch(0, 2)
        self.layout_.setSpacing(12)
        self.layout_.addWidget(self.lengthBox)
        self.layout_.addWidget(self.optionsBox)
        self.layout_.addWidget(self.generatorBox)
        self.setLayout(self.layout_)
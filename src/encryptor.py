from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QWidget,QPushButton,\
QHBoxLayout, QLabel, QButtonGroup,QRadioButton, QGridLayout,QLineEdit
from PySide6.QtCore import Qt

from Crypto.Hash import SHA256, SHA512, TupleHash128,TupleHash256,BLAKE2b,BLAKE2s
from typings import EncryptionAlgo
from log import log
class Encryptor:
    def __init__(self):
        self.hashObject = SHA256.new()
    
    def setAlgo(self, newAlgo: EncryptionAlgo):
        match newAlgo:
            case EncryptionAlgo.sha256:
                self.hashObject = SHA256.new()
            case EncryptionAlgo.sha512:
                self.hashObject = SHA512.new()
            case EncryptionAlgo.TupleHash128:
                self.hashObject = TupleHash128.new()
            case EncryptionAlgo.TupleHash256:
                self.hashObject = TupleHash256.new()
            case EncryptionAlgo.BLAKE2s:
                self.hashObject = BLAKE2s.new()
            case EncryptionAlgo.BLAKE2b:
                self.hashObject = BLAKE2b.new()
            case _:
                log(f"encryptor.py: unexpected hash algrorithm provided ({newAlgo})")
    
    def encrypt(self, data:str):
        self.hashObject.update(data.encode())
        hash = self.hashObject.hexdigest()
        self.hashObject = self.hashObject.new()
        return hash
    
class EncryptorTab(QWidget):
    def __init__(self,parent) -> None:
        super(EncryptorTab, self).__init__(parent)
        self.encryptor = Encryptor()
        self.clipboard = QClipboard(self)
        self.infoText = QLabel(self)
        self.infoText.setMinimumHeight(140)
        self.infoText.setText("\
Шифрование - это процесс преобразования информации таким образом, \
чтобы она стала неразборчивой для посторонних лиц, но при этом могла \
быть восстановлена получателем с помощью специального ключа. \
Шифрование применяется повсеместно в сфере информационной \
безопасности, включая защиту личных данных, банковских транзакций, \
обмена электронными сообщениями и многое другое. \
На этой странице вы можете опробовать различные алгоритмы шифрования.\
")
        self.infoText.setWordWrap(True)
        self.infoText.setStyleSheet("font-size:13.5px")
        
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Введите текст для шифровки")
        
        self.encryptButton = QPushButton("Зашифровать", self)
        self.encryptButton.setMinimumSize(180,24)
        self.encryptButton.clicked.connect(self.encrypt)
        
        self.encryptionSelectBox = QWidget(self)
        self.sha256Button = QRadioButton("sha-256", self.encryptionSelectBox)
        self.sha256Button.setChecked(True)
        self.sha512Button = QRadioButton("sha-512",self.encryptionSelectBox)
        self.TupleHash128Button = QRadioButton("TupleHash128", self.encryptionSelectBox)
        self.TupleHash256Button = QRadioButton("TupleHash256", self.encryptionSelectBox)
        self.BLAKE2sButton = QRadioButton("BLAKE2s", self.encryptionSelectBox)
        self.BLAKE2bButton = QRadioButton("BLAKE2b", self.encryptionSelectBox)
        
        self.buttonGroup = QButtonGroup(self.encryptionSelectBox)
        self.buttonGroup.buttonClicked.connect(self.encryptAlgoChanged)
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
        self.resultCopyButton.setMinimumSize(95,24)
        self.resultCopyButton.clicked.connect(self.copyToClipboard)
        self.resultTextField = QTextEdit("Здесь появится зашифрованный текст...")
        self.resultTextField.setFont("Courier New")
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
        self.layout_.setContentsMargins(10,10,10,10)
        self.layout_.addWidget(self.infoText)
        self.layout_.addWidget(self.inputField)
        self.layout_.addWidget(self.encryptButton)
        self.layout_.setAlignment(self.encryptButton, Qt.AlignmentFlag.AlignCenter)
        self.layout_.addWidget(self.encryptionSelectBox)
        self.layout_.addWidget(self.resultBox)
        
        self.setLayout(self.layout_)
    
    def encrypt(self):
        self.resultTextField.setText(
            self.encryptor.encrypt(
                self.inputField.text()
            )
        )
    
    def encryptAlgoChanged(self, button):
        newAlgo: EncryptionAlgo
        match button:
            case self.sha256Button:
                newAlgo=EncryptionAlgo.sha256
            case self.sha512Button:
                newAlgo=EncryptionAlgo.sha512
            case self.TupleHash128Button:
                newAlgo=EncryptionAlgo.TupleHash128
            case self.TupleHash256Button:
                newAlgo=EncryptionAlgo.TupleHash256
            case self.BLAKE2sButton:
                newAlgo=EncryptionAlgo.BLAKE2s
            case self.BLAKE2bButton:
                newAlgo=EncryptionAlgo.BLAKE2b
            case _:
                log(f"encryptor.py: button doesn't match any of the algorithms ({button})")
        self.encryptor.setAlgo(newAlgo)
    
    def copyToClipboard(self):
        self.clipboard.setText(
            self.resultTextField.toPlainText()
        )

def encrypt(data:str)->str:
    return Encryptor().encrypt(data)
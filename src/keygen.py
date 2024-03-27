from PySide6.QtGui import QClipboard,QFont,QImage,QIcon,QPixmap
from PySide6.QtWidgets import QVBoxLayout, QWidget,QPushButton, \
QHBoxLayout, QLabel,QGridLayout,QLineEdit,QCheckBox,QSpinBox
from PySide6.QtCore import Qt
import secrets
import string

class Keygen:
    def generate(
        length: int,
        lowercase=True,
        uppercase=True,
        digits=True,
        symbols=True
    ):
        chars='' \
            + (string.ascii_lowercase if lowercase else '' )\
            + (string.ascii_uppercase if uppercase else '' )\
            + (string.digits if digits else '' )\
            + ("~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/" if symbols else '')
        return ''.join(secrets.choice(chars) for i in range(length))

class KeygenTab(QWidget):
    def __init__(self,parent) -> None:
        super(KeygenTab, self).__init__(parent)
        self.clipboard = QClipboard(self)
        self.infoText = QLabel(self)
        self.infoText.setText("\
Иметь надежные пароли - это ключевой аспект обеспечения безопасности \
в Интернете. Слабые пароли могут быть легко взломаны хакерами, что \
может привести к утере доступа к аккаунтам и краже личной информации. \
Хакеры могут использовать различные методы, такие как словарные \
атаки, перебор паролей или использование уязвимостей в системе, чтобы \
получить доступ к учетной записи. Поэтому важно использовать \
уникальные, сложные пароли и регулярно их обновлять, чтобы защитить \
свои аккаунты от взлома. Здесь вы можете сгенерировать надежный пароль, \
выбрав длину и разрешённые символы.\
")
        self.infoText.setWordWrap(True)
        self.infoText.setStyleSheet("font-size:13.5px")
        
        self.lengthBox = QWidget(self)
        self.lengthLabel = QLabel(self.lengthBox)
        self.lengthLabel.setText("Длина пароля:")
        self.lengthInput = QSpinBox(self.lengthBox)
        self.lengthInput.setMinimumSize(100,24)
        self.lengthInput.setMinimum(1)
        self.lengthInput.setMaximum(128)
        self.lengthInput.setValue(16)
        # self.lengthSlider TODO
        
        self.optionsBox = QWidget(self)
        self.checked=3
        self.uppercaseCheckbox = QCheckBox("Верхний регистр",self.optionsBox)
        self.uppercaseCheckbox.setChecked(True)
        self.uppercaseCheckbox.clicked.connect(self.optionsChanged)
        self.lowercaseCheckbox = QCheckBox("Нижний регистр",self.optionsBox)
        self.lowercaseCheckbox.setChecked(True)
        self.lowercaseCheckbox.clicked.connect(self.optionsChanged)
        self.digitsCheckbox = QCheckBox("Цифры", self.optionsBox)
        self.digitsCheckbox.setChecked(True)
        self.digitsCheckbox.clicked.connect(self.optionsChanged)
        self.symbolsCheckbox = QCheckBox("Специальные символы",self.optionsBox)
        self.symbolsCheckbox.clicked.connect(self.optionsChanged)
        
        self.generatorBox=QWidget(self)
        self.generateButton=QPushButton("Сгенерировать", self.generatorBox)
        self.generateButton.setMinimumSize(110,24)
        self.generateButton.clicked.connect(self.generate)
        self.generateField=QLineEdit(self.generatorBox)
        self.generateField.setFont("Courier New")
        self.generateField.setPlaceholderText("Здесь будет ваш сгенерированный пароль...")
        self.generateField.setReadOnly(True)
        self.copyButton=QPushButton(self.generatorBox)
        self.copyButton.setMinimumSize(24,24)
        icon = QImage("resources/copyIcon.png")
        icon.invertPixels(QImage.InvertMode.InvertRgb)
        self.copyButton.setIcon(QIcon(QPixmap(icon)))
        # self.copyButton.set
        self.copyButton.clicked.connect(self.copyToClipboard)

        ##Layouts
        self.lengthBoxLayout = QHBoxLayout(self.lengthBox)
        self.lengthBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lengthBoxLayout.addWidget(self.lengthLabel)
        self.lengthBoxLayout.addWidget(self.lengthInput)
        
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
        
        
        self.infoText.setMinimumHeight(143)
        self.layout_ = QVBoxLayout(self)
        self.layout_.setContentsMargins(10,10,10,10)
        self.layout_.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_.setSpacing(0)
        self.layout_.addWidget(self.infoText)
        self.layout_.addWidget(self.lengthBox)
        self.layout_.addWidget(self.optionsBox)
        self.layout_.addSpacing(9)
        self.layout_.addWidget(self.generatorBox)
        self.setLayout(self.layout_)
    
    def optionsChanged(self, newState):
        if newState==True:
            if self.checked==1:
                for checkBox in self.optionsBox.findChildren(QCheckBox):
                    if checkBox.focusPolicy() is Qt.FocusPolicy.NoFocus:
                        checkBox.setAttribute(
                            Qt.WidgetAttribute.WA_TransparentForMouseEvents,
                            False
                        )
                        checkBox.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            self.checked+=1
        else:
            self.checked-=1
            if self.checked==1:
                for checkBox in self.optionsBox.findChildren(QCheckBox):
                    if checkBox.isChecked():
                        checkBox.setAttribute(
                            Qt.WidgetAttribute.WA_TransparentForMouseEvents,
                            True
                        )
                        checkBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    
    def generate(self):
        self.generateField.setText(
            Keygen.generate(
                length=self.lengthInput.value(),
                lowercase=self.lowercaseCheckbox.isChecked(),
                uppercase=self.uppercaseCheckbox.isChecked(),
                digits=self.digitsCheckbox.isChecked(),
                symbols=self.symbolsCheckbox.isChecked()
            )
        )
    
    def copyToClipboard(self):
        self.clipboard.setText(
            self.generateField.text()
        )
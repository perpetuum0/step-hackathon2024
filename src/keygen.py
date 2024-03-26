from PySide6.QtWidgets import QVBoxLayout, QWidget,QPushButton, \
QHBoxLayout, QLabel,QGridLayout,QLineEdit,QCheckBox,QSpinBox
from PySide6.QtCore import Qt

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
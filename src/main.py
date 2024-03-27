if __name__ == "__main__":
    import sys
    from app import KeyManager
    import db
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    app.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        background-color:#26467D;    
        color:white;
        font-size:13px;
        font-weight:550;
    }
    QPushButton:hover { background-color:#2B5091 }
    QPushButton:checked { background-color:#3464B6; border:none }
    QPushButton:pressed { background-color:#3464B6; border:none }
    """)
    keyManager = KeyManager()
    app.exec()
    db.close()
    sys.exit()
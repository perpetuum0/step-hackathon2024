if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    from app import KeyManager
    from log import log_open, log_close
    import db
    log_open()
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
    log_close()
    sys.exit()
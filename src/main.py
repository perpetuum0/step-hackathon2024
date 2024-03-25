if __name__ == "__main__":
    import sys
    from app import KeyManager
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    keyManager = KeyManager()
    sys.exit(app.exec())
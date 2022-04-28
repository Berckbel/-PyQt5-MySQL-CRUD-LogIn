import sys

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(QUrl("views/login.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import QMainWindow


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.label = None
        self.setWindowTitle('Joc')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('GameWindow')
        self.mesaj = None
        stylesheet = '''
            #GameWindow {
                background-image: url(pexels-chokniti-khongchum-2280549.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        '''
        self.setStyleSheet(stylesheet)

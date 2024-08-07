import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from cx_Freeze import setup, Executable
import os


class LoveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Quer namorar comigo?')
        self.setGeometry(100, 100, 800, 600)
        
        # Inicializa a imagem de fundo
        self.background_image = QPixmap("Beecrowd\Python\eueela.jpg")  # Substitua "background.jpg" pelo nome da sua imagem
        self.label = QLabel('Quer namorar comigo?', self)
        self.label.move(280, 200)
        self.label.setStyleSheet('color: white; font-size: 24px; font: bold;')

        self.yes_button = QPushButton('Sim', self)
        self.yes_button.move(250, 400)
        self.yes_button.setStyleSheet('font-size: 20px; font: bold; color: blue;')
        self.yes_button.clicked.connect(self.on_yes_click)
        
        self.no_button = QPushButton('Não', self)
        self.no_button.move(450, 400)
        self.no_button.setStyleSheet('font-size: 20px; font: bold; color: red;')
        self.no_button.installEventFilter(self)
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter and source is self.no_button:
            self.no_button.move(random.randint(0, self.width() - self.no_button.width()), 
                                random.randint(0, self.height() - self.no_button.height()))
        return super(LoveWindow, self).eventFilter(source, event)
    
    def on_yes_click(self):
        QMessageBox.information(self, 'Resposta', 'Que bom! Eu também te amo!')
    
    def resizeEvent(self, event):
        super(LoveWindow, self).resizeEvent(event)
        self.update_background()

    def update_background(self):
        # Redimensiona a imagem para o tamanho da janela
        if not self.background_image.isNull():
            self.background_pixmap = self.background_image.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.setAutoFillBackground(True)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(self.background_pixmap))
            self.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    ex = LoveWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
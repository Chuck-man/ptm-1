import re
import sys
from create_csv import creating_csv
from random_copying import random_copying
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QDesktopWidget,
    QLineEdit,
    QInputDialog,
    QLabel,
    QMainWindow,
    QFileDialog
)
from PyQt5.QtGui import QPixmap
from iterator import Iterator
from copying_dataset import copying_dataset


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.btn_1 = QPushButton("Создать файл анотацию исходного датасета", self)
        self.btn_1.move(50, 20)
        self.btn_1.resize(300, 30)
        self.btn_1.clicked.connect(self.showDialog_1)
        self.btn_2 = QPushButton("Создание датасета с другой организацией файлов", self)
        self.btn_2.move(50, 60)
        self.btn_2.resize(300, 30)
        self.btn_2.clicked.connect(self.showDialog_2)
        self.btn_3 = QPushButton("Создание копии датасета", self)
        self.btn_3.move(50, 100)
        self.btn_3.resize(300, 30)
        self.btn_3.clicked.connect(self.showDialog_3)
        self.btn_4 = QPushButton("Просмотр изображений", self)
        self.btn_4.move(50, 140)
        self.btn_4.resize(300, 30)
        self.btn_4.clicked.connect(self.showDialog_4)
        self.label = QLabel(self)
        self.btn_6 = QPushButton("Далее", self)
        self.btn_6.move(200, 550)
        self.btn_6.clicked.connect(self.showDialog_6)
        self.label.move(50, 220)
        self.btn_6.resize(300, 30)

        self.resize(800, 600)
        self.setWindowTitle("lab3")
        self.show()
        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
    
    def showDialog_1(self):

        text_2, _ =(QFileDialog.getSaveFileName(self, "Напишите название файла", filter=".csv"))
        self.create_file = creating_csv(str(self.folderpath),str(text_2))

    def showDialog_2(self):

        text_2, _ =(QFileDialog.getSaveFileName(self, "Напишите название файла", filter=".csv"))
        self.create_file = random_copying(str(self.folderpath),str(text_2))

    def showDialog_3(self):

       text_2, _ =(QFileDialog.getSaveFileName(self, "Напишите название файла", filter=".csv"))
       self.create_file = copying_dataset(str(self.folderpath),str(text_2))

    def showDialog_4(self):

        text_1, _ =(QFileDialog.getOpenFileName(self, "выберите файл?"))
        text_2, ok = QInputDialog.getText(self, "Input Dialog", "Введите метку:")
        
        if ok and _:

            self.create_iterator = Iterator(str(text_2), str(text_1))
            self.pixmap = QPixmap(next(self.create_iterator))
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(), self.pixmap.height())

    def showDialog_6(self):
        self.pixmap = QPixmap(next(self.create_iterator))
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
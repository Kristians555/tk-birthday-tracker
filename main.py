from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize

class BirthdayTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BDay tracker")
        self.setMinimumSize(QSize(300,200))
        
        display_tab = QWidget()
        insert_tab = QWidget()

        tab_control = QTabWidget()
        tab_control.addTab(display_tab, "Display")
        tab_control.addTab(insert_tab, "Insert")

        self.setCentralWidget(tab_control)
        

    def pushed_button(self):
        print("button clicked")

app = QApplication()

win = BirthdayTracker()
win.show()

app.exec()
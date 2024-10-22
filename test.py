import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class ButtonDemo(QWidget):
    def __init__(self):
        super().__init__()

        # Метка для отображения состояния кнопок
        self.label = QLabel("Нажмите на кнопку", self)

        # Обычная кнопка
        self.normal_button = QPushButton("Обычная кнопка", self)
        self.normal_button.clicked.connect(self.on_normal_button_click)

        # Кнопка-переключатель
        self.toggle_button = QPushButton("Кнопка-переключатель", self)
        self.toggle_button.setCheckable(True)
        self.toggle_button.clicked.connect(self.on_toggle_button_click)

        # Кнопка с иконкой
        self.icon_button = QPushButton("", self)
        self.icon_button.setIcon(QIcon("folder-download.png"))  # Путь к вашей иконке
        self.icon_button.setIconSize(QSize(24, 24))
        self.icon_button.clicked.connect(self.on_icon_button_click)

        # Кнопка с шорткатом
        self.shortcut_button = QPushButton("Кнопка с шорткатом (Alt+S)", self)
        self.shortcut_button.setShortcut("Alt+S")
        self.shortcut_button.clicked.connect(self.on_shortcut_button_click)

        # Заблокированная кнопка
        self.disabled_button = QPushButton("Неактивная кнопка", self)
        self.disabled_button.setEnabled(False)  # Кнопка заблокирована

        # Группа кнопок для вертикального макета
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.normal_button)
        vbox.addWidget(self.toggle_button)
        vbox.addWidget(self.icon_button)
        vbox.addWidget(self.shortcut_button)
        vbox.addWidget(self.disabled_button)

        # Устанавливаем вертикальный макет
        self.setLayout(vbox)
        self.setWindowTitle("Пример работы с кнопками в PyQt5")
        self.setGeometry(100, 100, 400, 300)

    # Функции для обработки нажатий кнопок

    def on_normal_button_click(self):
        self.label.setText("Нажата обычная кнопка")

    def on_toggle_button_click(self):
        if self.toggle_button.isChecked():
            self.label.setText("Кнопка-переключатель: Включено")
        else:
            self.label.setText("Кнопка-переключатель: Выключено")

    def on_icon_button_click(self):
        self.label.setText("Нажата кнопка с иконкой")

    def on_shortcut_button_click(self):
        self.label.setText("Нажата кнопка с шорткатом")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ButtonDemo()
    demo.show()
    sys.exit(app.exec_())

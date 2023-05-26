import sys
from typing import Union, Optional
from operator import add, mul, sub, truediv

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

operations = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        # соединения кнопок с цифрами использую метод add_digit()
        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        # self.ui.btn_backspace.clicked.connect(self.backspace)

        # соединение кнопок с методом calculate
        self.ui.btn_res.clicked.connect(self.calculate)
        # self.ui.btn_plus.clicked.connect(lambda : self.add_temp('+'))

        self.ui.btn_plus.clicked.connect(self.add_temp)

        self.ui.btn_plus.clicked.connect(self.math_operation)
        self.ui.btn_minus.clicked.connect(self.math_operation)
        self.ui.btn_mul.clicked.connect(self.math_operation)
        self.ui.btn_div.clicked.connect(self.math_operation)

    def add_digit(self):
        btn = self.sender()

        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')

        if btn.objectName() in digit_buttons:
            if self.ui.le_entry.text() == '0':
                self.ui.le_entry.setText(btn.text())
            else:
                self.ui.le_entry.setText(self.ui.le_entry.text() + btn.text())

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')

    def add_point(self) -> None:
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.le_entry.text())

        if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
            self.ui.lbl_temp.setText(entry + f' {btn.text()} ')
            self.ui.le_entry.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').strip()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lbl_temp.text():

            return self.ui.lbl_temp.text().strip('.')[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        sign = self.ui.lbl_temp.text().strip()[-1]
        temp = self.ui.lbl_temp.text()
        temp_num = self.ui.lbl_temp.text().split()[0]
        print('temp_num:', temp_num)
        print('entry:', entry)
        # print('temp=',temp)
        print('sign:', sign)
        if temp_num:
            result = self.remove_trailing_zeros(
                str(operations[sign](float(temp_num), self.get_entry_num())))
            self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.le_entry.setText(result)
            return result
    #
    # @staticmethod
    # def remove_trialling_zeros(num: str) -> str:
    #     n = str(float(num))
    #     return n[:-2] if n[-2:] == '.0' else n
    #
    # def add_point(self) -> None:
    #     if '.' not in self.ui.le_entry.text():
    #         self.ui.le_entry.setText(self.ui.le_entry.text() + '.')
    #
    # # метод очищения поля ввода
    # def clear_all(self):
    #     self.ui.le_entry.setText('0')
    #     self.ui.lbl_temp.setText('0')
    #
    # # метод очищения поля ввода
    # def clear_entry(self):
    #     self.ui.le_entry.setText('0')
    #
    # def backspace(self):
    #     entry = self.ui.le_entry.text()
    #     if entry and entry != '0':
    #         self.ui.le_entry.setText(entry[0:len(entry)-1])
    #     else:
    #         self.ui.le_entry.setText('0')
    #
    # # метод добавления записи в память калькулятора
    # # 1 тип записи в память это число и математический знак типа 52+
    # # 2 тип это равенство 52+3=
    # def add_temp(self, math_sign: str):
    #     if self.ui.le_entry.text() or self.get_math_sign() == '=':
    #         self.ui.lbl_temp.setText(self.remove_trialling_zeros(self.ui.le_entry.text()) + f' {math_sign}')
    #         self.ui.le_entry.setText('0')
    #
    # def get_entry_num(self) -> Union[int, float]:
    #     entry = self.ui.le_entry.text().strip('.')
    #     return float(entry) if '.' in entry else int(entry)
    #
    # def get_temp_num(self) -> Union[int, float, None]:
    #     temp = self.ui.le_entry.text().strip('.')
    #     temp_num = float(temp) if '.' in temp else int(temp)
    #     print('get_temp_num',temp_num)
    #     return temp_num
    #
    # def get_math_sign(self) -> Optional[str]:
    #     if self.ui.lbl_temp.text():
    #         # print('get_math_sign', self.ui.lbl_temp.text().strip('.').split()[-1])
    #         sign = self.ui.lbl_temp.text()[-1]
    #         print('get_math_sign',sign)
    #         return sign
    #
    # def calculate(self) -> Optional[str]:
    #     entry = self.ui.le_entry.text()
    #     temp = self.ui.lbl_temp.text()
    #
    #     if temp:
    #         result = self.remove_trialling_zeros(
    #             str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
    #         )
    #         self.ui.lbl_temp.setText(temp + ' '+self.remove_trialling_zeros(entry) + ' =')
    #         self.ui.le_entry.setText(result)
    #         return result
    #
    # def math_operation(self, math_sign: str):
    #     temp = self.ui.lbl_temp.text()
    #     if not temp:
    #         self.add_temp(math_sign)
    #     else:
    #         if self.get_math_sign() != math_sign:
    #             if self.get_math_sign() == '=':
    #                 self.add_temp(math_sign)
    #             else:
    #                 self.ui.lbl_temp.setText(temp[:-2] + f' {math_sign}')
    #         else:
    #             self.ui.lbl_temp.setText(self.calculate() + f' {math_sign}')

    def math_operation(self):
        temp = self.ui.lbl_temp.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{btn.text()} ')


from design import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()

    sys.exit(app.exec())



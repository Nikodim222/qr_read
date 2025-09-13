"""
* Чтение QR-кода
* *************************
* Программа для чтения картинки с QR-кодом и получения из неё информации.
* Для работы программы требуется Python 3. Предварительно
* требуется установить необходимые библиотеки:
* $ pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
* $ pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencv-python pyzbar
* Из-под Linux можно выполнить вот такую установку библиотек:
* $ sudo apt-get install python3-opencv python-zbar libzbar0 && sudo apt-get clean
* Программа является кроссплатформенной. Она должна работать
* под Microsoft Windows, Linux, macOS и т.д.
*
* @author Ефремов А. В., 12.09.2025
"""

import sys, os
import re
from argparse import ArgumentParser
import cv2
from pyzbar.pyzbar import decode

from miscellaneous import Miscellaneous

app_parser: ArgumentParser = ArgumentParser(description = "Аргументы программы")
app_parser.add_argument(
    "-f",
    type = str,
    help = "Файл изображения с QR-кодом",
    required = True,
    dest = "qr_file"
)
app_args = app_parser.parse_args(sys.argv[1:])

def parse_qr(p_qr_file: str) -> None:
    """
    * Получение информации по QR-коду из файла
    *
    * @param p_qr_file Имя исходного файла с изображением QR-кода
    """
    if not "".__eq__(p_qr_file):
        cnt: int = 0
        decoded_objects = decode(cv2.imread(p_qr_file)) # декодируем QR-код
        for obj in decoded_objects: # выводим результаты
            qr_line: str = ""
            for obj2 in obj.data.decode('utf-8'):
                qr_line += obj2
            if not "".__eq__(qr_line):
                cnt += 1
                for line in qr_line.split(os.linesep):
                    cleaned_line: str = re.sub(r'[\x00-\x1F\x7F]', '', line) # удаляем непечатаемые символы с помощью регулярного выражения
                    Miscellaneous.print_message(f"Строка из QR-кода: {chr(34)}{cleaned_line}{chr(34)}.")
        if cnt < 1:
            Miscellaneous.print_message(f"Ничего не найдено в файле {chr(34)}{p_qr_file}{chr(34)}.")

def main() -> None:
    global app_args
    print("************")
    print("ЧТЕНИЕ QR-КОДА")
    print("************")
    if Miscellaneous.is_file_readable(app_args.qr_file):
        Miscellaneous.print_message(f"Доступность файла {chr(34)}{app_args.qr_file}{chr(34)} для чтения: ok.")
        parse_qr(app_args.qr_file)
    else:
        Miscellaneous.print_message(f"Файл {chr(34)}{app_args.qr_file}{chr(34)} невозможно прочитать.")
    Miscellaneous.print_message("Работа программы завершена.")

# Точка запуска программы
if __name__ == "__main__":
    main()

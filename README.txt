О ПРОГРАММЕ

Данная программа читает текстовую информации с изображения, которое хранится в файле,
будь то файл GIF, PNG, JPEG или какой-либо другой. Получая на вход подобный файл,
приложение производит его разбор и поиск текстовой информации. Если какой-либо текст
будет найден, то он будет выведен на экран в консоль.
Сгенерировать пробный файл с QR-кодом можно на любом online-сервисе, коих много в
Интернете: например, можно воспользоваться сайтом http://qrcoder.ru



УСТАНОВКА НЕОБХОДИМЫХ БИБЛИОТЕК ПОД PYTHON 3

Нужны будут две основные библиотеки:
1. "OpenCV" - библиотека для работы с изображениями;
2. "pyzbar" - библиотека для чтения QR-кодов.
В общем случае обе библиотеки можно установить средствами Python 3 через следующую
команду:

$ pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencv-python pyzbar

Если у вас Linux, то можно установить специальные пакеты для этого, используя команду:

$ sudo apt-get install python3-opencv python-zbar libzbar0 && sudo apt-get clean



ИЗВЕСТНЫЕ ПРОБЛЕМЫ

Библиотека "pyzbar" может не работать корректно под Microsoft Windows. И такая проблема
обсуждалась на странице https://github.com/NaturalHistoryMuseum/pyzbar/issues/93
Если кратко, то решить её можно следующим образом (ниже говорится о 64-битной версии
операционной системы Microsoft Windows; для своей же версии выбирайте соответствующие
установочные файлы):
1. Скачать и установить файл "VC_redist.x64.exe".
2. Перезагрузить компьютер.
3. Скачать и установить файл "vcredist_x64.exe".
Файлы берутся из официальных источников, а именно:
1. "VC_redist.x64.exe" at https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
2. "vcredist_x64.exe" at https://www.microsoft.com/en-gb/download/details.aspx?id=40784
Оба файла - это Visual C++ Redistributable Packages for Visual Studio.



ПРИМЕР ЗАПУСКА ПРОГРАММЫ

.\qr_read.bat -f .\qr-code.gif

-- EOF

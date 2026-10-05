    __  ______   _     ___  _____  
   // \\  ||    /\\   || \\  ||
   \\	  ||   // \\  || //  ||
    \\    ||  //___\\ ||\\   ||
 \\_//    || //     \\|| \\  ||  xpy

<div align="center">
<h1>STARTXPY-LITE</h1>
</div>

Starting X on linux in python

* Debian-package startxpy-lite v0.7.4-1
Готовый .deb для Debian/Ubuntu.

* Установка:
```shell
wget https://github.com/levikabd/startxpy-lite/releases/download/master/startxpy_*_all.deb
sudo dpkg -i startxpy_*_all.deb
sudo apt-get install -f
```

* For the normal operation of all 
the functions of this application, 
the following components must be installed:

* Enter as root:
```shell
sudo apt update
sudo apt install \
  xinit xserver-xorg python3 nano \ 
  fluxbox \
  libreoffice xfe \
  thunderbird galculator geany\
  ktimer
```

* Yandex Browser is for working on the Internet. 
It is not installed from the main repository, 
only from the Yandex repository:
```shell
sudo apt install -y curl
curl -s https://repo.yandex.ru/yandex-browser/YANDEX-BROWSER-KEY.GPG | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/yandex-browser.gpg
sudo add-apt-repository "deb [arch=amd64] https://repo.yandex.ru/yandex-browser/deb stable main"
sudo apt update
sudo apt install yandex-browser-stable
```

* After installation, run the following command:
```shell
nano ~/.xinitrc
```

Enter the following text:
```shell
#!/bin/sh
fluxbox &
exec startxpy-lite
```

* To develop, install the following components:
pycharm, vscode, cursor, qtcreator
See the instructions on the developer's website.

* To run the application, run the following command:
```shell
startxpy
```

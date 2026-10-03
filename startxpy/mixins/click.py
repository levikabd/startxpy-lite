import subprocess

class ClickMixin:
    def button_click(self, button_name):
        # print(f"Button clicked: {button_name}")
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('libreoffice')
        elif button_name == "dev":
            # print('open dev')
            # subprocess.Popen('/usr/bin/dev')
            pass
        elif button_name == "ktimer":
            # print('open ktimer')
            # subprocess.Popen('/usr/bin/ktimer')
            subprocess.Popen('ktimer')
            pass
        elif button_name == "mail":
            # print('open mail')
            # subprocess.Popen('/usr/bin/thunderbird')
            subprocess.Popen('thunderbird')
        elif button_name == "poweroff":
            # print('open poweroff')
            subprocess.Popen('sudo /usr/bin/poweroff')
            #subprocess.Popen('sudo poweroff')
        elif button_name == "run":
            print('open run')
            # self.run()
            # subprocess.Popen('/usr/bin/run')
        elif button_name == "web":
            # print('open web')
            subprocess.Popen('/opt/yandex/browser/yandex_browser')
        elif button_name == "xfe":
            # print('open xfe')
            subprocess.Popen('xfe')
            # subprocess.Popen('/usr/bin/xfe')

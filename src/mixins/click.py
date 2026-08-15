import subprocess

class ClickMixin:
    def button_click(self, button_name):
        # ("ai", "ai.gif"),
        # ("calc", "calc.gif"),
        # ("ded", "ded.gif"),
        # ("dev", "dev.gif"),
        # ("doc", "doc.gif"),
        # ("exit", "exit.gif"),
        # ("ktimer", "ktimer.gif"),
        # ("mail", "mail.gif"),
        # ("poweroff", "poweroff.gif"),
        # ("run", "run.gif"),
        # ("web", "web.gif"),
        # ("settings", "settings.gif"),
        # ("fullscreen", "fullscreen.gif"),
        # ("xfe", "xfe.gif")

        # print(f"Нажата кнопка: {button_name}")
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('libreoffice')
        elif button_name == "ai":
            print('open ai')
            # subprocess.Popen('/usr/bin/ai')
        elif button_name == "ded":
            print('open ded')
            # subprocess.Popen('/usr/bin/ded')
        elif button_name == "dev":
            print('open dev')
            # subprocess.Popen('/usr/bin/dev')
        elif button_name == "ktimer":
            # print('open ktimer')
            # subprocess.Popen('/usr/bin/ktimer')
            subprocess.Popen('ktimer')
        elif button_name == "mail":
            # print('open mail')
            # subprocess.Popen('/usr/bin/thunderbird')
            subprocess.Popen('thunderbird')
        elif button_name == "poweroff":
            # print('open poweroff')
            # subprocess.Popen('/usr/bin/poweroff')
            subprocess.Popen('sudo poweroff')
        elif button_name == "run":
            print('open run')
            # self.run()
            # subprocess.Popen('/usr/bin/run')
        elif button_name == "web":
            # print('open web')
            subprocess.Popen('/opt/yandex/browser/yandex_browser')
        elif button_name == "settings":
            print('open settings')
            # subprocess.Popen('/usr/bin/settings')
        elif button_name == "xfe":
            # print('open xfe')
            subprocess.Popen('xfe')
            # subprocess.Popen('/usr/bin/xfe')

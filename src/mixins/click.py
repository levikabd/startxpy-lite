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
        # ("fullscreen", "fullscreen.gif"),
        # ("xfe", "xfe.gif")

        # print(f"Нажата кнопка: {button_name}")
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('libreoffice')


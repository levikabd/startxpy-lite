import tkinter as tk
import subprocess
# from typing import Optional

def run_command(cmd_text, shell=True):
    """Обёртка для запуска команды через subprocess."""
    try:
        proc = subprocess.Popen(
            cmd_text,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,  # полезно добавить и stderr
            text=True                # удобно: сразу строки, а не байты
        )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr
    except Exception as e:
        # тут можно логировать ошибку
        return None, None, str(e)


class CommandRunnerMixin:
    """Миксин для запуска произвольных команд через диалоговое окно."""

    def setup_run_button(self) -> None:
    #     # Кнопка RUN на твоей панели инструментов
    #     btn = tk.Button(parent, text="RUN", command=self._on_run_click)
    #     btn.pack(side=tk.LEFT, padx=4, pady=2)
    #     self.btn_run = btn  # сохраняем ссылку, если понадобится менять состояние
        self.btn_run.config(command=self._on_run_click)

    def _on_run_click(self) -> None:
        dialog = tk.Toplevel(self)
        dialog.title("Run Command")
        dialog.geometry("500x150")
        dialog.resizable(False, False)

        # Заголовок
        lbl = tk.Label(dialog, text="Введите команду для выполнения:")
        lbl.pack(padx=10, pady=(10, 5), anchor="w")

        # Поле ввода
        entry = tk.Entry(dialog, font=("DejaVu Sans Mono", 11))
        entry.pack(fill=tk.X, padx=10, pady=5)
        entry.focus_set()

        # Привязка Enter
        # entry.bind("<Return>", lambda e: self._execute_command(entry, dialog))
        entry.bind("<Return>", lambda e: self._execute_command_with_output(entry, dialog))

        # Кнопки
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=10)

        run_btn = tk.Button(
            btn_frame,
            text="Выполнить",
            command=lambda: self._execute_command_with_output(entry, dialog),
        )
        run_btn.pack(side=tk.LEFT, padx=5)

        cancel_btn = tk.Button(
            btn_frame,
            text="Отмена",
            command=dialog.destroy,
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)

    def _execute_command(self, entry: tk.Entry, dialog: tk.Toplevel) -> None:
        cmd_text = entry.get().strip()
        if not cmd_text:
            return

        dialog.destroy()  # закрываем сразу после нажатия
        returncode, out, err = run_command(cmd_text)

    def _show_command_result(
        self,
        cmd: str,
        out: str,
        err: str,
        exit_code: int,
    ) -> None:
        """Покажи результат, например, в статусбаре (у тебя уже есть статусбар)."""
        status_msg = f"Команда завершена (код: {exit_code})"
        if hasattr(self, "statusbar_frame"):
            # Если у тебя есть виджет для текста статуса — используй его
            pass
        # Или просто выведи в консоль для начала
        print("--- Command ---")
        print(cmd)
        if out:
            print("STDOUT:\n", out)
        if err:
            print("STDERR:\n", err)
        print("---------------")

    def _show_error(self, msg: str) -> None:
        import tkinter.messagebox as mb
        mb.showerror("Ошибка", msg)

    def _execute_command_with_output(self, entry: tk.Entry, dialog: tk.Toplevel) -> None:
        cmd_text = entry.get().strip()
        if not cmd_text:
            return
        dialog.destroy()

        out_win = tk.Toplevel(self)
        out_win.title(f"Output: {cmd_text[:40]}")
        out_win.geometry("700x400")

        txt = tk.Text(out_win, wrap="word", font=("DejaVu Sans Mono", 10))
        txt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        returncode, out, err = run_command(cmd_text)

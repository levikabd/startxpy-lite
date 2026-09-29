import tkinter as tk
import subprocess
import tkinter.messagebox as mb

def _log_command_result(self, cmd, out, err, exit_code):
    status_msg = f"The command has been completed (code: {exit_code})"
    print("--- Command ---")
    print(cmd)
    if out:
        print("STDOUT:\n", out)
    if err:
        print("STDERR:\n", err)
    print("---------------")
    return status_msg

def run_command(cmd_text, shell=True):
    try:
        proc = subprocess.Popen(
            cmd_text,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr
    except Exception as e:
        return None, None, str(e)


class CommandRunnerMixin:

    def setup_run_button(self) -> None:
        self.btn_run.config(command=self._on_run_click)

    def _on_run_click(self) -> None:
        dialog = tk.Toplevel(self)
        dialog.title("Run Command")
        dialog.geometry("500x150")
        dialog.resizable(False, False)

        lbl = tk.Label(dialog, text="Enter the command to execute:")
        lbl.pack(padx=10, pady=(10, 5), anchor="w")

        entry = tk.Entry(dialog, font=("DejaVu Sans Mono", 11))
        entry.pack(fill=tk.X, padx=10, pady=5)
        entry.focus_set()

        entry.bind("<Return>", lambda e: self._execute_command_with_output(entry, dialog))

        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=10)

        run_btn = tk.Button(
            btn_frame,
            text="To perform:",
            command=lambda: self._execute_command_with_output(entry, dialog),
        )
        run_btn.pack(side=tk.LEFT, padx=5)

        cancel_btn = tk.Button(
            btn_frame,
            text="Cancel",
            command=dialog.destroy,
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)

    def _execute_command_with_output(self, entry: tk.Entry, dialog: tk.Toplevel) -> None:
        cmd_text = entry.get().strip()
        if not cmd_text:
            return
        dialog.destroy()
        if not self.run_with_output:
            out_win = tk.Toplevel(self)
            out_win.title(f"Output: {cmd_text[:40]}")
            out_win.geometry("700x400")
            txt = tk.Text(out_win, wrap="word", font=("DejaVu Sans Mono", 10))
            txt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        returncode, out, err = run_command(cmd_text)

    def _show_command_result(
        self,
        cmd: str,
        out: str,
        err: str,
        exit_code: int,
    ) -> None:
        status_msg = f"The command has been completed (code: {exit_code})"
        if hasattr(self, "statusbar_frame"):
            pass

        status_msg = self._log_command_result(cmd, out, err, exit_code)

    def _show_error(self, msg: str) -> None:
        mb.showerror("Error", msg)


import subprocess
import shutil
from tkinter import messagebox

class CommandShutdownMixin:
    # def setup_pwr_button(self) -> None:
    #     self.btn_pwr.config(command=self.on_poweroff)
    def get_shutdown_command(self):
        candidates = [
            ["lxsession-logout"],              # LXDE
            ["xfce4-session-logout"],          # XFCE
            ["gnome-session-quit", "--power-off"],  # GNOME
        ]

        for cmd in candidates:
            if shutil.which(cmd[0]):
                return cmd

        if shutil.which("systemctl"):
            return ["systemctl", "poweroff"]

        return None

    def on_poweroff(self):
        if not messagebox.askyesno("Shutting down the system", "Do you really want to turn off your computer?"):
            return

        cmd = get_poweroff_command()
        if cmd is None:
            messagebox.showerror("Error", "No suitable shutdown command was found.")
            return

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=15
            )
            if result.returncode != 0:
                messagebox.showerror(
                    "Error",
                    f"Operation canceled.\n\n{result.stderr.strip()}"
                )
        except subprocess.TimeoutExpired:
            messagebox.showerror("Error", "Command shutting down the system timed out.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error has occurred: {e}")

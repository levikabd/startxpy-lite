import subprocess
import shutil
from typing import Optional

IDE_COMMANDS = {
    "pycharm": "pycharm",
    "geany": "geany",
    "qtcreator": "qtcreator",
    "vscode": "code",
    "cursor": "cursor",
}

def get_ide_command(ide_name: str) -> Optional[str]:
    return IDE_COMMANDS.get(ide_name.lower())

def launch_ide(ide_name: str, project_path: Optional[str] = None) -> bool:
    cmd = get_ide_command(ide_name)
    if not cmd:
        print(f"[Launcher] Unknown IDE: {ide_name}")
        return False

    if not shutil.which(cmd):
        print(f"[Launcher] The command '{cmd}' was not found. Check the IDE installation.")
        return False

    args = [cmd]
    if project_path and isinstance(project_path, str) and len(project_path) > 0:
        args.append(project_path)
    try:
        subprocess.Popen(args, start_new_session=True)
        print(f"[Launcher] Running: {cmd} {'with the project: ' + project_path if project_path else ''}")
        return True
    except Exception as e:
        print(f"[Launcher] Launch error {cmd}: {e}")
        return False

import subprocess
import shutil
from typing import Optional

# Маппинг «понятного имени» → команда в Debian
IDE_COMMANDS = {
    "pycharm": "pycharm",
    "vscode": "code",
    "cursor": "cursor",
    "geany": "geany",
    "qtcreator": "qtcreator",
}

def get_ide_command(ide_name: str) -> Optional[str]:
    """Возвращает команду для IDE или None, если не найдено."""
    return IDE_COMMANDS.get(ide_name.lower())

def launch_ide(ide_name: str, project_path: Optional[str] = None) -> bool:
    """
    Запускает IDE.
    
    - project_path: путь к папке проекта (многие IDE принимают его как аргумент).
    - Возвращает True, если запуск инициирован, иначе False.
    """
    cmd = get_ide_command(ide_name)
    if not cmd:
        print(f"[Launcher] Неизвестная IDE: {ide_name}")
        return False

    # Проверяем, есть ли команда в PATH (чтобы не стартовать «пустую» ошибку)
    if not shutil.which(cmd):
        print(f"[Launcher] Команда '{cmd}' не найдена. Проверьте установку IDE.")
        return False

    args = [cmd]
    if project_path and isinstance(project_path, str) and len(project_path) > 0:
        args.append(project_path)

    try:
        # start_new_session=True — чтобы процесс не зависел от GUI (важно на сервере)
        subprocess.Popen(args, start_new_session=True)
        print(f"[Launcher] Запущено: {cmd} {'с проектом: ' + project_path if project_path else ''}")
        return True
    except Exception as e:
        print(f"[Launcher] Ошибка запуска {cmd}: {e}")
        return False


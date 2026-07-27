import sys
from pathlib import Path

root = Path(__file__).resolve().parent
src_dir = root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from startxpy import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

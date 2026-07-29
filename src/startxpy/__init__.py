"""StartXPy package initialization."""

__version__ = "0.1.0"
__author__ = "lev"

# Экспортируем основные классы, чтобы можно было делать:
#   from startxpy import MainWindow
from .main_window import MainWindow

__all__ = ["MainWindow"]

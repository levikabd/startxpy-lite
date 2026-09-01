from setuptools import setup, find_packages

setup(
    name="startxpy",
    version="0.6.1",
    packages=find_packages(),
    package_data={
        "startxpy": ["assets/icons/*"],
    },
    entry_points={
        "console_scripts": [
            "startxpy = startxpy.launcher:main",
        ],
    },
)

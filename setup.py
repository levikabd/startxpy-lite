from setuptools import setup, find_packages

setup(
    name="startxpy",
    version="0.6.8-2",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "startxpy": ["assets/icons/*.gif"],
    },
    entry_points={
        "console_scripts": [
            "startxpy = startxpy.main:main",
        ],
    },
)

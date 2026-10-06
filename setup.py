from setuptools import setup, find_packages

setup(
    name="startxpy-lite",
    version="0.7.4",
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

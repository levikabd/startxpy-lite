from setuptools import setup, find_packages

setup(
    name="startxpy-lite",
    version="0.6.8-1",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "startxpy-lite": ["assets/icons/*.gif"],
    },
    entry_points={
        "console_scripts": [
            "startxpy-lite = startxpy-lite.main:main",
        ],
    },
)

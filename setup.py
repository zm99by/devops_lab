from setuptools import setup, find_packages

setup(
    name="task3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = task3.snapshot:main",
        ],
    },
    install_requires=[
        'psutil',
        'argparse',
        'schedule',
        'datetime'
    ],
    version="1",
    author="Vladimir Sakhonchik",
    author_email="zm99@gmail.com",
    description="some description",
    license="MIT",
)
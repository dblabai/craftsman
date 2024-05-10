from io import open

from setuptools import setup

from craftsman import __version__ as version

setup(
    name="craftsman",
    version=version,
    url="https://github.com/dblabai/craftsman",
    license="MIT",
    author="Jack",
    author_email="dblab@dblab.top",
    description="Python visual one-click packaging tool.",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    keywords=["gui", "executable", "nuitka"],
    packages=["craftsman"],
    include_package_data=True,
    install_requires=["PySide6>=6.6.0", "toml>=0.10.2"],
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
)

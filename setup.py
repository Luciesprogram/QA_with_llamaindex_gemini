from setuptools import setup, find_packages

setup(
    name = "QA_system",
    version = "0.0.1",
    author = "Vikant Singh",
    author_email = "vikrantsingh8709@gmail.com",
    packages = find_packages(),
    py_modules = ["exception","logger"],
)
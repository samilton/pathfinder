from setuptools import setup, find_packages

setup(
    name="pathfinder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "openai",
    ],
)

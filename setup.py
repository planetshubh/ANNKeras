from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="1.0.0",
    author="shubhscode",
    description="ANN implementaion Ist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhscode/ANNKeras",
    author_email="shubh_er@hotmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
    "tensorflow",
    "matplotlib",
    "pandas",
    "numpy",
    "seaborn"
    ]
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timborafa_template", # Replace package name
    version="0.0.1",
    author="Rafael",
    author_email="timbo.rafa@gmail.com",
    description="A template package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timbo-rafa/python-template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

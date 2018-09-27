from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="shisell",
    version="1.0.0",
    author="Soluto",
    author_email="it@soluto.com",
    description="Shisell is a service agnostic abstraction for analytic dispatchers.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Soluto/shisell-python",
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

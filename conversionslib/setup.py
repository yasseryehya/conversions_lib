from setuptools import setup, find_packages


setup(
    name="conversionslib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    author="Yasser Yahia",
    author_email="yasso.soly@gmail.com",
    description=("A library for converting between different data types "
                 "and file formats"),
    long_description=("A library for converting between different data "
                      "types and file formats, incloading..."),
    long_description_content_type="text/markdown",
    url="https://github.com/yasseryehya/conversions_lib",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="numpy csv conversion npz",
    project_urls={
        "Bug Tracker": "https://github.com/yasseryehya/conversions_lib/issues",
        "Source Code": "https://github.com/yasseryehya/conversions_lib",
    },
)

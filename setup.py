from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="disk_detective",            
    version="0.2.0",
    author="5f0",
    url="https://github.com/5f0ne/disk-detective",
    description="Provides tools to analyze disks on byte level",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[
        "hash_calc==1.1.0",
        "partitiontypes==1.0.1",
        "cnvrtr==1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "disk_detective = disk_detective.__main__:main"
        ]
    }
)
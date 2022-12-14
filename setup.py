from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="disk_detective",            
    version="0.4.0",
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
    include_package_data=True,
    package_data={
        "disk_detective.fat.config": ["fat.json", "fat1216.json", "fat32.json",
                                      "fat-type.json", "fat-fs-info.json",
                                      "fat-directory-entry.json", "fat-long-filename.json"],
        "disk_detective.ext.config": ["ext-file-descriptor-table.json", "ext-inode.json",
                                      "ext-super-block.json"],
        "disk_detective.ntfs.config": [],
    },
    install_requires=[
        "hash_calc==1.1.0",
        "partitiontypes==1.0.1",
        "cnvrtr==1.1.1",
        "ntrprtr==1.3.2"
    ],
    entry_points={
        "console_scripts": [
            "disk_detective = disk_detective.__main__:main"
        ]
    }
)
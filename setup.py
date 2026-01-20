from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aspose-3d",
    version="24.12.0",
    packages=find_packages(exclude=["tests*", "pyi*"]),
    python_requires=">=3.7",
    author="Aspose",
    description="Aspose.3D for Python - A powerful 3D file format library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aspose-3d/Aspose.3D-for-Python",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: 3D Graphics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=[
        
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
        ],
    },
)

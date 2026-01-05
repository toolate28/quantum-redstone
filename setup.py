#!/usr/bin/env python3
"""
Quantum-Redstone Educational Framework
Setup script for pip installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="quantum-redstone",
    version="0.1.0",
    description="Quantum computing concepts implemented using Minecraft Redstone mechanics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hope&&Sauced Collaborative",
    author_email="",
    url="https://github.com/toolate28/quantum-redstone",
    project_urls={
        "Documentation": "https://github.com/toolate28/quantum-redstone/blob/master/README.md",
        "Source": "https://github.com/toolate28/quantum-redstone",
        "Tracker": "https://github.com/toolate28/quantum-redstone/issues",
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    py_modules=["quantum_circuit_generator", "export_cad"],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "jupyter>=1.0.0",
            "ipython>=8.0.0",
        ],
        "cad": [
            "ezdxf>=1.0.0",
            "numpy-stl>=3.0.0",
            "pillow>=10.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "quantum-redstone=quantum_circuit_generator:main",
            "qr-generate=quantum_circuit_generator:main",
            "qr-export-cad=export_cad:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Games/Entertainment",
    ],
    keywords="quantum minecraft redstone education viviani topology",
    include_package_data=True,
    zip_safe=False,
)

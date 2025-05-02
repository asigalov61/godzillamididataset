from setuptools import setup, find_packages
import os

with open("godzillamididataset/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="godzillamididataset",
    version="25.5.3",
    description="Enormous, comprehensive, normalized and searchable MIDI dataset for MIR and symbolic music AI purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alex Lev",
    author_email="alexlev61@proton.me",
    url="https://github.com/asigalov61/godzillamididataset",
    project_urls={
        "SoundCloud": "https://soundcloud.com/aleksandr-sigalov-61",
        "Output Samples": "https://github.com/asigalov61/godzillamididataset/tree/main/godzillamididataset/midi_samples",
        "Examples": "https://github.com/asigalov61/godzillamididataset/tree/main/godzillamididataset/examples",
        "Issues": "https://github.com/asigalov61/godzillamididataset/issues",
        "Documentation": "https://github.com/asigalov61/godzillamididataset",
        "Discussions": "https://github.com/asigalov61/godzillamididataset/discussions",
        "Source Code": "https://github.com/asigalov61/godzillamididataset",
        "Official GitHub Repo": "https://github.com/asigalov61/godzillamididataset",
        "Hugging Face Dataset Repo": "https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Datase",
        "Hugging Face Spaces Demo": "https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Datase"
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'godzillamididataset': ['/', 'examples/', 'artwork/', 'midi_samples/', 'seed_midis/'],
    },
    keywords=['MIDI', 'music', 'music ai', 'music dataset', 'MIDI dataset', 'MIR'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research', 
        'Operating System :: OS Independent',        
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
)
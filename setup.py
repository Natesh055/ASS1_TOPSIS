from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="Topsis-102216077",
    version="0.0.1",
    description="A Python package implementing TOPSIS technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/Natesh055/Topsis_Repo.git'
    author="Natesh Singh Pundir",
    author_email="npundir_be22.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Tops"],
    include_package_data=True,
    install_requires=['scipy',
                      'tabulate',
                      'numpy',
                      'pandas'
     ],
     entry_points={
        "console_scripts": [
            "Tops=Tops.__main__:main",
        ]
     },
)

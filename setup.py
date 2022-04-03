from setuptools import find_packages, setup

setup(
    name="data-science-project",  # name used to install it. The code dir 'importname' is what you import. Can be identical.
    version="0.1.0",
    description="A template structure for data science projects",
    author="Henrik Hviid Hansen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    # install_requires=[""]  # put package / dependencies required to run this one
)

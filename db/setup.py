from setuptools import setup, find_packages
setup(
    name="computersecuritydb",
    version="1.0.0",
    # packages=find_packages(),
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'pydantic[email]'
    ],
    extras_require={
        "test": ["tox", "pytest"],
    },
)

from setuptools import setup

setup(
    name='wavvy',
    packages=['wavvy'],
    include_package_data=True,
    install_requires=[
        'flask', 'passlib',
    ],
)

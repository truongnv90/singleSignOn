from setuptools import setup, find_packages

setup(
    name='test_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    dependency_links=[
        'git+https://github.com/username/repo.git#egg=package-0.1',
    ],
)

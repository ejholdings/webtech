from setuptools import setup, find_packages

if __name__ == "__main__":
    with open("requirements.txt", 'r') as f:
        dependencies = f.read().splitlines()

    setup(
        scripts=["bin/webpy"],
        name='webtech',
        version='1',
        packages=find_packages(),
        install_requires=dependencies,
    )

    )

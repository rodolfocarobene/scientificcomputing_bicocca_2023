from setuptools import setup, find_packages

setup(
    name="mymodule",
    description="test module the SciComp class",
    url="https://github.com/rodolfocarobene",
    author="Rodolfo Carobene",
    author_email="rodolfo.carobene@gmail.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["numpy", "matplotlib"],
)

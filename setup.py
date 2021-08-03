import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testtile",
    install_requires=[],
    version="0.0.1",
    author="Dumbmachine",
    author_email="dumbmachine@github.com",
    description="Package for Taktile Coding Challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DumbMachine/coding-challenge",
    project_urls={
        "Bug Tracker": "https://github.com/DumbMachine/coding-challenge/issues",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "fold_tools"},
    packages=setuptools.find_packages(where="fold_tools", exclude=["tests"]),
    python_requires=">=3.6",
)

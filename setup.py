import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dash_xinet", 
    version="v0.0.3",
    author="xinetzone",
    author_email="xinzone@outlook.com",
    description="Dash App",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/xinetzone/dash-xinet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='>=3.9',
)
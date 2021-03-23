import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convert2tif-dakotagporter",
    version="0.0.4",
    author="Dakota Porter",
    author_email="dakotap3045@gmail.com",
    description="Small package that converts image(s) to .tif file format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dakotagporter/convert2tif",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "convert2tif"},
    packages=setuptools.find_packages(where="convert2tif"),
    python_requires=">=3.6",
)

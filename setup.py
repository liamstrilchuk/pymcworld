import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymcworld-gullyn",
    version="1.0.0",
    author="Liam Strilchuk",
    author_email="gullyn.games@gmail.com",
    description="Simple Minecraft world editor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gullyn/pymcworld",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

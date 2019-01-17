import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymesomake",
    version="0.2.0",
    author="Eric Theise",
    author_email="erictheise@gmail.com",
    description="An implementation of the mesostic generation algorithm Andrew Culver developed for John Cage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erictheise/pymesomake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'pymesomake = pymesomake.__main__:main'
        ]
    }
)

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="comex-fetcher",
    version="0.0.1",
    author="Daniel Komesu",
    author_email="danielkomesu@gmail.com",
    description="Fetcher of raw data from the SECEX website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    requires=["requests", "tqdm"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.10',
)

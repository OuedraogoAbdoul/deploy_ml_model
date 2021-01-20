import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="svm-model", # Replace with your own username
    version="0.0.1",
    author="Abdoul Ouedraogor",
    author_email="abdoul.w.ouedraogo@gmail.com",
    description="A package for support vector machine deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OuedraogoAbdoul/deploy_ml_model",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 38",
        "Programming Language :: Python :: 39",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

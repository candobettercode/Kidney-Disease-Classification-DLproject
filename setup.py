import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUHTOR_USER_NAME = "condonettercode"
SRC_REPO = "cnnClassifier"
AUHTOR_EMAIL = "siddhesh1199@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUHTOR_USER_NAME,
    author_email=AUHTOR_EMAIL,
    description="Kidney-Disease-Classification-App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
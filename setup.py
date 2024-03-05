import setuptools

with open("README.md", "r", encoding="utf-8") as f :
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "mlproject_1"
AUTHOR_USER_NAME = "him0397"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "himshoyo@gmail.com"

 

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/him0397/mlproject_1",
    #project_urls={}
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


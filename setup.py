from io import open
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="py-i18n-countries",
    version="0.1.1",
    author="Gunnar Sv Sigurbjörnsson",
    author_email="gunnar.sigurbjornsson@gmail.com",
    description="Mapping for ISO-3166-1 alpha-2 codes to country names and nationalities",
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/nossrannug/py-i18n-countries",
    license="MIT",
    keywords="country nationality iso 3166-1",
    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.5, <4",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={  # Optional
        "py_i8n_countrties": ["en.json"],
    },
)

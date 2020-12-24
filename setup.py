from io import open
from setuptools import setup, find_packages


setup(
    name="py-i18n-countries",
    version="0.1.0",
    author="Gunnar Sv Sigurbjörnsson",
    author_email="gunnar.sigurbjornsson@gmail.com",
    description="Mapping for ISO-3166-1 alpha-2 codes to country names and nationalities",
    long_description=(),
    url="",
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
    install_requires=["setuptools"],
    zip_safe=False,
    packages=find_packages("py_i18n_countries"),
    include_package_data=True,
    package_dir={'': 'py_i18n_countries'}
)

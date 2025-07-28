import json
import sys

from packaging.version import parse

from pathlib import Path

from setuptools import find_packages, setup

if __name__ == "__main__":
    base_dir = Path(__file__).parent

    about = {}
    with (base_dir / "__about__.py").open() as f:
        exec(f.read(), about)

    with (base_dir / "README.rst").open() as f:
        long_description = f.read()

    setup_requires = ["setuptools_scm"]

    # Define commonly-used pins here to be used in other repositories
    # e.g. vivarium_dependencies[numpy,pandas]>=1.2.0,<2.0.0
    extras_require = {
        "numpy": ["numpy<2.0.0"],
        "pandas": ["pandas"],
        "pyyaml": ["pyyaml>=5.1"],
        "scipy": ["scipy"],
        "click": ["click"],
        "tables": ["tables"],
        "loguru": ["loguru"],
        "pyarrow": ["pyarrow"],
        # testing
        "pytest": ["pytest"],
        "pytest-cov": ["pytest-cov"],
        "pytest-mock": ["pytest-mock"],
        "vivarium_testing_utils": ["vivarium_testing_utils"],
        # formatting and linting
        "black": ["black==22.3.0"],
        "isort": ["isort==5.13.2"],
        "mypy": ["mypy"],
        # docs
        "sphinx": ["sphinx>=4.0,<8.0.0"],
        "sphinx-rtd-theme": ["sphinx-rtd-theme"],
        "sphinx-autodoc-typehints": ["sphinx-autodoc-typehints"],
        "sphinx-click": ["sphinx-click"],
        "ipython": ["IPython"],
        "matplotlib": ["matplotlib"],
        # convenience sets
        "testing": [
            "vivarium_build_utils[pytest]",
            "vivarium_build_utils[pytest-cov]",
            "vivarium_build_utils[pytest-mock]",
        ],
        "linting": [
            "vivarium_build_utils[black]",
            "vivarium_build_utils[isort]",
        ],
        "plotting": [
            "vivarium_build_utils[ipython]",
            "vivarium_build_utils[matplotlib]",
        ],
    }

    setup(
        name=about["__title__"],
        description=about["__summary__"],
        long_description=long_description,
        license=about["__license__"],
        url=about["__uri__"],
        author=about["__author__"],
        author_email=about["__email__"],
        classifiers=[
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Natural Language :: English",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Operating System :: POSIX :: BSD",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Build Tools",
        ],
        extras_require=extras_require,
        zip_safe=False,
        setup_requires=setup_requires,
    )

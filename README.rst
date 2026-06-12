=====================
Vivarium Dependencies
=====================

**NOTE: This repository has been archived.**

The ``vivarium_dependencies`` package has been renamed and migrated into the
`vivarium-suite monorepo <https://github.com/ihmeuw/vivarium-suite>`_.

What changed
------------

- **Source:** ``ihmeuw/vivarium_dependencies`` (archived) ->
  ``ihmeuw/vivarium-suite`` (under ``libs/dependencies/``)

There are no downstream changes. This package is a code-less metapackage that
exposes only `extras <https://peps.python.org/pep-0508/#extras>`_; the PyPI
distribution name (``vivarium-dependencies``) and every extras reference in
downstream ``pyproject.toml`` files are unchanged.

Original package overview
=========================


Vivarium Dependencies contains dependency constraints commonly used in Simulation 
Science repositories.

Usage
=====

A downstream repository can use Vivarium Dependencies to define a setup dependency
by including the desired constraint(s) in the `install_requires` dictionary of its setup.py::

  # setup.py
  ...
  if __name__ == "__main__":
    ...
    install_requirements = [
      "vivarium_build_utils[layered_config_tree,pandas]"
      ...
    ]
    ...
    interactive_requirements = ["vivarium_dependencies[interactive]"]
    ...
  ...

Installation
============

You can build ``vivarium_dependencies`` from source with::

  $ git clone https://github.com/ihmeuw/vivarium_dependencies.git
  $ cd vivarium_dependencies
  $ conda create -n ENVIRONMENT_NAME
  $ pip install -e .

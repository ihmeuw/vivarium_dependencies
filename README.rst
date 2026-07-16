=====================
Vivarium Dependencies
=====================

**NOTE: This repository is archived and will receive no further updates.**

The ``vivarium_dependencies`` package's development has migrated into the
`vivarium-suite monorepo <https://github.com/ihmeuw/vivarium-suite>`_.

What changed
------------

- **PyPI distribution:** ``vivarium-dependencies`` (unchanged - same name)
- **Source:** ``ihmeuw/vivarium_dependencies`` (archived) ->
  ``ihmeuw/vivarium-suite`` (under ``libs/dependencies/``)

This repository's final release was ``v1.0.9``. The ``vivarium-dependencies``
distribution name is now published from the monorepo starting at ``v1.1.0``, so
downstream ``pyproject.toml`` files pin unchanged and ``pip install`` resolves
to the monorepo release. There are no import-path changes since this is a
code-less metapackage that exposes only
`extras <https://peps.python.org/pep-0508/#extras>`_. This repository is
frozen and will not receive updates.

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

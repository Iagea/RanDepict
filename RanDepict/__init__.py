# -*- coding: utf-8 -*-

"""
RanDepict Python Package.
This repository contains RanDepict,
an easy-to-use utility to generate a big variety of
chemical structure depictions (random depiction styles and image augmentations).


Typical usage example:

from RanDepict import RandomDepictor
smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
with RandomDepictor() as depictor:
    image = depictor(smiles)

Have a look in the RanDepictNotebook.ipynb for more examples.

For comments, bug reports or feature ideas,
please raise a issue on the Github repository.

"""

__version__ = "1.1.1"

__all__ = [
    "RanDepict",
]


from .randepict import RandomDepictor, DepictionFeatureRanges, RandomMarkushStructureCreator

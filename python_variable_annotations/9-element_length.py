#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
""" 
This function takes an iterable of sequences and returns a list of tuples
where each tuple contains a sequence and its length.
"""

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuples """
    return [(i, len(i)) for i in lst]

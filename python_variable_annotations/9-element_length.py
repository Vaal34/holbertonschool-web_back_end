#!/usr/bin/env python3
"""
This function takes an iterable of sequences and returns a list of tuples
where each tuple contains a sequence and its length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuples """
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3

import random

def wait_random(max_delay = 10):
    yield
    return random.uniform(0, max_delay)
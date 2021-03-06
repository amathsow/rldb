"""
HyperNEAT Best scores from DQN2013 paper.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "HyperNEAT Best",
    "algo-nickname": "HNeat Best",
    "algo-source-title": "A Neuroevolution Approach to General Atari Game Playing",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7

#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_O2_to_triplet/groups"
shortDesc = u""
longDesc = u"""
This family makes the transition from the excited O2 singlet state to the ground triplet state.
It also covers S2 and SO which are isoelectronic with O2 and behave similarly.
This family consists of these three transitions only, and cannot be generalized to structures other than O2, S2, SO.
This was added as a family rather than a library to enforce these transitions
(whereas a library has to be added to each run)
This family has a reverse recipe relative to the 1,2-Birad_to_alkene Family,
yet it is not its reverse since different species are considered.
"""

template(reactants=["Y_12birad"], products=["Y_alkene"], ownReverse=False)

reverse = "Triplet_O2_to_singlet"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "top_node",
    group =
"""
1 *1 [O2d,S2d] u0 p2 {2,D}
2 *2 [O2d,S2d] u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "O2",
    group =
"""
1 *1 O2d u0 p2 {2,D}
2 *2 O2d u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "S2",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 S2d u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "SO",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 O2d u0 p2 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: top_node
    L2: O2
    L2: S2
    L2: SO
"""
)

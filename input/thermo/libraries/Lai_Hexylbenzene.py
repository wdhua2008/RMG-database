#!/usr/bin/env python
# encoding: utf-8

name = "Hexylbenzene"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Hexylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {7,D} {9,S} {26,S}
9  C u0 p0 c0 {8,S} {10,D} {27,S}
10 C u0 p0 c0 {9,D} {11,S} {28,S}
11 C u0 p0 c0 {10,S} {12,D} {29,S}
12 C u0 p0 c0 {7,S} {11,D} {30,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.53848, 0.154692, -0.000505491, 1.21307e-06, -1.03076e-09, -11769.8, 15.735],
                Tmin = (10, 'K'),
                Tmax = (405.473, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.31497, 0.114635, -6.84889e-05, 1.97053e-08, -2.19288e-12, -10815.6, 38.7611],
                Tmin = (405.473, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-97.9049, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (706.73, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 2,
    label = "Styrene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  C u0 p0 c0 {6,S} {8,D} {15,S}
8  C u0 p0 c0 {3,S} {7,D} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.91381, 0.00507501, 0.000182357, -3.25547e-07, 1.82313e-10, 15456.5, 11.7174],
                Tmin = (10, 'K'),
                Tmax = (539.173, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.77087, 0.0711256, -4.71867e-05, 1.48906e-08, -1.78985e-12, 15938.1, 37.6194],
                Tmin = (539.173, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (128.478, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (378.308, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Styrene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "HexylbenzylRad1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u1 p0 c0 {5,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  C u0 p0 c0 {6,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}


""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.83083, 0.124716, -0.000340437, 8.86239e-07, -8.17332e-10, 6898.77, 17.2712],
                Tmin = (10, 'K'),
                Tmax = (389.843, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.38727, 0.116589, -7.18943e-05, 2.12444e-08, -2.41624e-12, 7774.22, 43.54],
                Tmin = (389.843, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (57.3216, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (685.944, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 4,
    label = "Butyl Radical",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.8048, 0.0225494, 1.82606e-05, -2.96978e-08, 1.03636e-11, 7489.25, 9.68915],
                Tmin = (10, 'K'),
                Tmax = (1043.96, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.40454, 0.0359845, -1.81441e-05, 4.47033e-09, -4.33902e-13, 6924.27, 8.53122],
                Tmin = (1043.96, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (62.2808, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (295.164, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butyl Radical calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 5,
    label = "Ethylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  C u0 p0 c0 {6,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.93256, 0.0045774, 0.000229019, -4.71073e-07, 3.18895e-10, 720.269, 12.7159],
                Tmin = (10, 'K'),
                Tmax = (378.139, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.62723, 0.0739489, -4.60899e-05, 1.38184e-08, -1.59588e-12, 1216.5, 37.9855],
                Tmin = (378.139, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (5.98516, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (424.038, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 6,
    label = "Ethylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,D}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  C u0 p0 c0 {6,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {9,S} {16,S}
9  C u0 p0 c0 {4,D} {8,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.91132, 0.00543209, 0.000200316, -3.74426e-07, 2.21934e-10, 19069.6, 13.1774],
                Tmin = (10, 'K'),
                Tmax = (504.174, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.56642, 0.0726363, -4.66693e-05, 1.43632e-08, -1.69469e-12, 19521.9, 37.9997],
                Tmin = (504.174, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (158.525, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (403.252, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 7,
    label = "Propylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {8,S} {19,S}
8  C u0 p0 c0 {7,S} {9,D} {20,S}
9  C u0 p0 c0 {4,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.72412, 0.0429039, 4.40028e-05, -7.58288e-08, 2.88791e-11, -2582.08, 12.2094],
                Tmin = (10, 'K'),
                Tmax = (967.569, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.13122, 0.0655377, -3.51925e-05, 9.12776e-09, -9.24042e-13, -4186.14, -1.41475],
                Tmin = (967.569, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-21.3967, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (494.711, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Propylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)



entry(
    index = 8,
    label = "Propylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {10,D}
6  C u0 p0 c0 {5,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {8,S} {17,S}
8  C u0 p0 c0 {7,S} {9,D} {18,S}
9  C u0 p0 c0 {8,D} {10,S} {19,S}
10 C u0 p0 c0 {5,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.89471, 0.00723012, 0.000275615, -5.94663e-07, 4.15797e-10, 16188.3, 15.1717],
                Tmin = (10, 'K'),
                Tmax = (414.99, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.59425, 0.0839895, -5.32106e-05, 1.61177e-08, -1.87171e-12, 16604.5, 39.2955],
                Tmin = (414.99, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (134.594, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (473.925, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Propylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 9,
    label = "Butylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {22,S}
9  C u0 p0 c0 {8,S} {10,D} {23,S}
10 C u0 p0 c0 {5,S} {9,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.17901, 0.0877537, -0.00021136, 5.83115e-07, -5.5537e-10, -5711.02, 13.8221],
                Tmin = (10, 'K'),
                Tmax = (394.37, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.26079, 0.0951888, -5.80606e-05, 1.70174e-08, -1.92366e-12, -4910.72, 39.7112],
                Tmin = (394.37, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-47.5121, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (565.384, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 10,
    label = "Butylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {11,D}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  C u0 p0 c0 {8,S} {10,D} {21,S}
10 C u0 p0 c0 {9,D} {11,S} {22,S}
11 C u0 p0 c0 {6,D} {10,S} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.70217, 0.0481911, 5.51547e-05, -9.61555e-08, 3.77439e-11, 12989.5, 14.9723],
                Tmin = (10, 'K'),
                Tmax = (937.336, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.6281, 0.0740216, -4.06696e-05, 1.07521e-08, -1.10595e-12, 11132.7, -2.17348],
                Tmin = (937.336, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (108.088, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (544.598, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 11,
    label = "Pentylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {6,D} {8,S} {23,S}
8  C u0 p0 c0 {7,S} {9,D} {24,S}
9  C u0 p0 c0 {8,D} {10,S} {25,S}
10 C u0 p0 c0 {9,S} {11,D} {26,S}
11 C u0 p0 c0 {6,S} {10,D} {27,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.88544, 0.117938, -0.000332991, 8.32039e-07, -7.35791e-10, -8792.9, 14.6085],
                Tmin = (10, 'K'),
                Tmax = (402.152, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.76962, 0.104944, -6.33527e-05, 1.84047e-08, -2.06544e-12, -7939.01, 38.7876],
                Tmin = (402.152, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-73.1433, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (636.057, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Pentylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 12,
    label = "Pentylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,S} {12,D}
8  C u0 p0 c0 {7,S} {9,D} {22,S}
9  C u0 p0 c0 {8,D} {10,S} {23,S}
10 C u0 p0 c0 {9,S} {11,D} {24,S}
11 C u0 p0 c0 {10,D} {12,S} {25,S}
12 C u0 p0 c0 {7,D} {11,S} {26,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.65179, 0.0690217, 8.62318e-06, -4.20781e-08, 1.57571e-11, 10092.1, 15.3011],
                Tmin = (10, 'K'),
                Tmax = (1148.08, 'K'),
            ),
            NASAPolynomial(
                coeffs = [14.2082, 0.0663492, -3.2446e-05, 7.6453e-09, -7.04837e-13, 5420.35, -46.8743],
                Tmin = (1148.08, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (84.0184, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (615.271, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Pentylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Benzyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {8,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {10,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.13967, -0.0141725, 0.000261854, -4.75457e-07, 2.76642e-10, 23304.6, 10.5067],
                Tmin = (10, 'K'),
                Tmax = (549.061, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.662671, 0.0580793, -3.73415e-05, 1.14394e-08, -1.33771e-12, 23270.3, 25.6807],
                Tmin = (549.061, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (193.736, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (332.579, 'J/(mol*K)'),
    ),
    shortDesc = u"""Calculation for Benzyl done by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 14,
    label = "Toluene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.04843, -0.00496311, 0.000190094, -3.12375e-07, 1.63599e-10, 3720.16, 10.905],
                Tmin = (10, 'K'),
                Tmax = (590.573, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.46624, 0.0620951, -3.84774e-05, 1.14026e-08, -1.29702e-12, 4089.7, 35.5174],
                Tmin = (590.573, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (30.9121, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (353.365, 'J/(mol*K)'),
    ),
    shortDesc = u"""Calculation for Toluene done by Lawrence Lai""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Indane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  C u0 p0 c0 {6,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {9,S}
9  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.05393, -0.00590968, 0.000256082, -4.22713e-07, 2.21322e-10, 4179.59, 11.8847],
                Tmin = (10, 'K'),
                Tmax = (594.808, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-4.42857, 0.0838269, -5.2664e-05, 1.57377e-08, -1.79928e-12, 4610.35, 43.5396],
                Tmin = (594.808, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (34.7223, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (457.296, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Indane calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 16,
    label = "IndaneRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {10,S} {11,S}
2  C u0 p0 c0 {1,D} {3,S} {12,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {9,S} {18,S} {19,S}
9  C u0 p0 c0 {5,S} {8,S} {10,D}
10 C u0 p0 c0 {1,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.00206, -0.0021151, 0.000260755, -4.42515e-07, 2.37477e-10, 19872.1, 13.1337],
                Tmin = (10, 'K'),
                Tmax = (577.899, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-4.52455, 0.0883507, -5.56849e-05, 1.6696e-08, -1.91438e-12, 20332.5, 45.0506],
                Tmin = (577.899, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (165.189, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (482.239, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Indane Radical calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 17,
    label = "Ethyltetralin",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {7,D} {9,S} {25,S}
9  C u0 p0 c0 {8,S} {10,D} {26,S}
10 C u0 p0 c0 {9,D} {11,S} {27,S}
11 C u0 p0 c0 {10,S} {12,D} {28,S}
12 C u0 p0 c0 {3,S} {7,S} {11,D}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.61601, 0.0421213, 0.00015139, -2.48903e-07, 1.12973e-10, -7263.88, 13.2472],
                Tmin = (10, 'K'),
                Tmax = (739.354, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.18674, 0.108057, -6.34363e-05, 1.78905e-08, -1.95192e-12, -7645.69, 27.5826],
                Tmin = (739.354, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-60.4008, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (673.472, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 18,
    label = "EthyltetralinRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {9,S} {26,S}
9  C u0 p0 c0 {8,S} {10,D} {27,S}
10 C u0 p0 c0 {9,D} {11,S} {28,S}
11 C u1 p0 c0 {10,S} {12,S} {13,S}
12 H u0 p0 c0 {11,S}
13 C u0 p0 c0 {3,S} {7,S} {11,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.61072, 0.0473956, 0.000136209, -2.20138e-07, 9.53756e-11, 6665.08, 13.9706],
                Tmin = (10, 'K'),
                Tmax = (788.688, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.103113, 0.109241, -6.32144e-05, 1.7577e-08, -1.89322e-12, 5913.22, 22.5258],
                Tmin = (788.688, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (55.4442, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (698.416, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin Radical calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 19,
    label = "1-PentylRadical",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.47258, 0.0518404, -9.83821e-05, 2.1257e-07, -1.6797e-10, 4338.11, 12.5789],
                Tmin = (10, 'K'),
                Tmax = (465.458, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.536753, 0.0539153, -3.045e-05, 8.39691e-09, -9.05101e-13, 4862.24, 27.1919],
                Tmin = (465.458, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (36.0561, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (365.837, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin Radical calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 20,
    label = "HexylbenzeneRad2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.59877, 0.154805, -0.000609286, 1.62243e-06, -1.47593e-09, 12181.7, 19.7013],
                Tmin = (10, 'K'),
                Tmax = (385.423, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.24183, 0.115893, -7.05084e-05, 2.05253e-08, -2.30125e-12, 13371.2, 51.9003],
                Tmin = (385.423, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (101.223, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 2 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 21,
    label = "HexylbenzeneRad3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.65581, 0.148005, -0.000555815, 1.48704e-06, -1.36252e-09, 11963.8, 19.3575],
                Tmin = (10, 'K'),
                Tmax = (384.533, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.19297, 0.116297, -7.11077e-05, 2.08011e-08, -2.34241e-12, 13097.8, 50.8816],
                Tmin = (384.533, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.4148, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 3 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 22,
    label = "HexylbenzeneRad4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.64345, 0.149629, -0.000570465, 1.5282e-06, -1.40016e-09, 11978.7, 20.0013],
                Tmin = (10, 'K'),
                Tmax = (384.254, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.25375, 0.116365, -7.11154e-05, 2.07901e-08, -2.33965e-12, 13130.7, 51.9042],
                Tmin = (384.254, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.5376, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 4 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 23,
    label = "HexylbenzeneRad5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.48051, 0.167113, -0.000676109, 1.75368e-06, -1.56349e-09, 11763.2, 18.2517],
                Tmin = (10, 'K'),
                Tmax = (388.368, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.51948, 0.114282, -6.91072e-05, 2.00059e-08, -2.23227e-12, 12938.4, 47.7742],
                Tmin = (388.368, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (97.7409, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 5 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 24,
    label = "HexylbenzeneRad6",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {5,S} {7,S} {19,S} {20,S}
7  C u0 p0 c0 {6,S} {8,S} {21,S} {22,S}
8  C u0 p0 c0 {7,S} {9,S} {23,S} {24,S}
9  C u0 p0 c0 {8,S} {10,S} {14,D}
10 C u0 p0 c0 {9,S} {11,D} {25,S}
11 C u0 p0 c0 {10,D} {12,S} {26,S}
12 C u0 p0 c0 {11,S} {13,D} {27,S}
13 C u0 p0 c0 {12,D} {14,S} {28,S}
14 C u0 p0 c0 {9,D} {13,S} {29,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.584, 0.151846, -0.000517195, 1.28776e-06, -1.12986e-09, 13247.6, 17.5928],
                Tmin = (10, 'K'),
                Tmax = (393.806, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.35399, 0.11298, -6.87556e-05, 2.00694e-08, -2.2584e-12, 14169.3, 40.6859],
                Tmin = (393.806, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (110.099, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 6 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 25,
    label = "ToluenePlusHOrtho",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {8,S} {14,S}
8  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94447, 0.00371676, 0.000199109, -3.98552e-07, 2.61611e-10, 17316.8, 10.9023],
                Tmin = (10, 'K'),
                Tmax = (391.042, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.19466, 0.0665475, -4.20309e-05, 1.27717e-08, -1.49365e-12, 17796.7, 34.7525],
                Tmin = (391.042, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (143.977, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (378.308, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHOrtho calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 26,
    label = "ToluenePlusHMeta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {7,S} {16,S}
7  C u1 p0 c0 {2,S} {6,S} {8,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94238, 0.00373416, 0.000189866, -3.65712e-07, 2.29978e-10, 17932.8, 11.2977],
                Tmin = (10, 'K'),
                Tmax = (408.683, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.52355, 0.0669984, -4.2256e-05, 1.28111e-08, -1.49441e-12, 18461.5, 36.7084],
                Tmin = (408.683, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (149.091, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (378.308, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHMeta calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)



entry(
    index = 27,
    label = "ToluenePlusHPara",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {8,D} {15,S}
8  C u0 p0 c0 {2,S} {7,D} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94034, 0.00368031, 0.000177387, -3.21352e-07, 1.88539e-10, 17945.9, 12.199],
                Tmin = (10, 'K'),
                Tmax = (440.604, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.18806, 0.0684758, -4.3479e-05, 1.325e-08, -1.55155e-12, 18573.3, 40.738],
                Tmin = (440.604, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (149.191, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (378.308, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHPara calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 28,
    label = "ToluenePlusHSub",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {13,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,D} {15,S}
8  C u0 p0 c0 {2,S} {7,D} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92063, 0.00475061, 0.000180439, -3.25908e-07, 1.86072e-10, 18796.8, 10.6913],
                Tmin = (10, 'K'),
                Tmax = (522.294, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.5955, 0.068928, -4.48671e-05, 1.40017e-08, -1.67289e-12, 19282.8, 36.0317],
                Tmin = (522.294, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (156.255, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (378.308, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHSub calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 29,
    label = "HexylbenzenePlusHOrtho",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {9,S} {27,S}
9  C u1 p0 c0 {8,S} {10,S} {11,S}
10 H u0 p0 c0 {9,S}
11 C u0 p0 c0 {9,S} {12,D} {28,S}
12 C u0 p0 c0 {11,D} {13,S} {29,S}
13 C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {13,S}
31 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.5092, 0.155564, -0.000463959, 1.07605e-06, -8.99619e-10, 2163.26, 16.6872],
                Tmin = (10, 'K'),
                Tmax = (410.116, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.830447, 0.118095, -7.07428e-05, 2.04243e-08, -2.28096e-12, 3026.22, 37.0036],
                Tmin = (410.116, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (17.9443, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (731.674, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHOrtho calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)


entry(
    index = 30,
    label = "HexylbenzenePlusHMeta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {7,D} {9,S} {27,S}
9  C u0 p0 c0 {8,S} {10,S} {28,S} {29,S}
10 C u0 p0 c0 {9,S} {11,D} {30,S}
11 C u0 p0 c0 {10,D} {12,S} {31,S}
12 C u1 p0 c0 {7,S} {11,S} {13,S}
13 H u0 p0 c0 {12,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.46487, 0.159417, -0.000477704, 1.08646e-06, -8.93664e-10, 2517.96, 16.3424],
                Tmin = (10, 'K'),
                Tmax = (413.815, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.387576, 0.116927, -6.97228e-05, 2.00563e-08, -2.23347e-12, 3353.91, 34.8352],
                Tmin = (413.815, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (20.8935, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (731.674, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHMeta calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)



entry(
    index = 31,
    label = "HexylbenzenePlusHPara",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {13,D}
8  C u0 p0 c0 {7,S} {9,D} {27,S}
9  C u0 p0 c0 {8,D} {10,S} {28,S}
10 C u0 p0 c0 {9,S} {11,S} {29,S} {30,S}
11 C u1 p0 c0 {10,S} {12,S} {13,S}
12 H u0 p0 c0 {11,S}
13 C u0 p0 c0 {7,D} {11,S} {31,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.43449, 0.164299, -0.000527222, 1.22987e-06, -1.02501e-09, 2442.97, 15.793],
                Tmin = (10, 'K'),
                Tmax = (409.466, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.766387, 0.117535, -7.00532e-05, 2.01241e-08, -2.23728e-12, 3359.26, 36.3653],
                Tmin = (409.466, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (20.2667, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (731.674, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHPara calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)



entry(
    index = 32,
    label = "HexylbenzenePlusHSub",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {27,S}
8  C u0 p0 c0 {7,S} {9,D} {28,S}
9  C u0 p0 c0 {8,D} {10,S} {29,S}
10 C u1 p0 c0 {9,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 C u0 p0 c0 {10,S} {13,D} {30,S}
13 C u0 p0 c0 {7,S} {12,D} {31,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {12,S}
31 H u0 p0 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.57652, 0.146954, -0.000385042, 8.72638e-07, -7.31177e-10, 3126.24, 16.669],
                Tmin = (10, 'K'),
                Tmax = (409.446, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.418165, 0.11887, -7.20885e-05, 2.10489e-08, -2.37357e-12, 3852.12, 34.312],
                Tmin = (409.446, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (25.9547, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (731.674, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHSub calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)



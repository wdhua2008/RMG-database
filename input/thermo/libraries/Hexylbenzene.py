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
                coeffs = [2.53847, 0.154692, -0.000505492, 1.21308e-06, -1.03077e-09, -11398.2, 15.735],
                Tmin = (10, 'K'),
                Tmax = (405.473, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.31498, 0.114635, -6.84888e-05, 1.97053e-08, -2.19288e-12, -10443.9, 38.7611],
                Tmin = (405.473, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-94.815, 'kJ/mol'),
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
                coeffs = [3.91438, 0.00504807, 0.000182605, -3.26259e-07, 1.82935e-10, 15869.4, 11.7163],
                Tmin = (10, 'K'),
                Tmax = (538.024, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.78289, 0.0711614, -4.72223e-05, 1.4905e-08, -1.79187e-12, 16353.8, 37.68],
                Tmin = (538.024, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (131.911, 'kJ/mol'),
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
                coeffs = [2.8299, 0.124847, -0.000341673, 8.89807e-07, -8.20653e-10, 7294.91, 17.2696],
                Tmin = (10, 'K'),
                Tmax = (389.773, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.39403, 0.116602, -7.19014e-05, 2.1246e-08, -2.41634e-12, 8172, 43.5774],
                Tmin = (389.773, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (60.6152, 'kJ/mol'),
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
                coeffs = [3.80479, 0.0225494, 1.82605e-05, -2.96978e-08, 1.03636e-11, 7538.75, 9.68916],
                Tmin = (10, 'K'),
                Tmax = (1043.96, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.40459, 0.0359844, -1.8144e-05, 4.4703e-09, -4.33899e-13, 6973.77, 8.53096],
                Tmin = (1043.96, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (62.6924, 'kJ/mol'),
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
                coeffs = [3.93254, 0.0045779, 0.000229014, -4.7106e-07, 3.18883e-10, 1009.62, 12.7159],
                Tmin = (10, 'K'),
                Tmax = (378.326, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.62729, 0.0739492, -4.60901e-05, 1.38185e-08, -1.5959e-12, 1505.87, 37.9858],
                Tmin = (378.326, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (8.39099, 'kJ/mol'),
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
                coeffs = [3.91148, 0.00542425, 0.000200392, -3.74658e-07, 2.22149e-10, 19461.4, 13.1771],
                Tmin = (10, 'K'),
                Tmax = (503.87, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.56917, 0.0726447, -4.66778e-05, 1.43666e-08, -1.69518e-12, 19914.3, 38.0134],
                Tmin = (503.87, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (161.782, 'kJ/mol'),
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
                coeffs = [3.72412, 0.0429039, 4.40028e-05, -7.58288e-08, 2.88791e-11, -2261.33, 12.2094],
                Tmin = (10, 'K'),
                Tmax = (967.569, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.13123, 0.0655377, -3.51925e-05, 9.12776e-09, -9.24042e-13, -3865.4, -1.41478],
                Tmin = (967.569, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-18.7299, 'kJ/mol'),
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
                coeffs = [3.69412, 0.0343661, 9.38387e-05, -1.62151e-07, 7.41706e-11, 15027.4, 14.1999],
                Tmin = (10, 'K'),
                Tmax = (752.472, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.98726, 0.0733477, -4.34887e-05, 1.23381e-08, -1.35086e-12, 14437.6, 16.3228],
                Tmin = (752.472, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (124.945, 'kJ/mol'),
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
                coeffs = [3.17901, 0.0877537, -0.00021136, 5.83117e-07, -5.55371e-10, -5355.9, 13.8221],
                Tmin = (10, 'K'),
                Tmax = (394.37, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.26079, 0.0951888, -5.80606e-05, 1.70174e-08, -1.92366e-12, -4555.6, 39.7112],
                Tmin = (394.37, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-44.5594, 'kJ/mol'),
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
                coeffs = [3.57311, 0.0522171, 5.318e-05, -1.03323e-07, 4.35113e-11, 12025, 15.2789],
                Tmin = (10, 'K'),
                Tmax = (874.478, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.06417, 0.0770386, -4.36721e-05, 1.18903e-08, -1.25571e-12, 10554.4, 1.36782],
                Tmin = (874.478, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (100.02, 'kJ/mol'),
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
                coeffs = [2.88543, 0.117939, -0.000332996, 8.3206e-07, -7.35814e-10, -8412.57, 14.6086],
                Tmin = (10, 'K'),
                Tmax = (402.149, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.76955, 0.104944, -6.33525e-05, 1.84046e-08, -2.06542e-12, -7558.69, 38.7872],
                Tmin = (402.149, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-69.981, 'kJ/mol'),
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
                coeffs = [3.65179, 0.0690217, 8.62322e-06, -4.20782e-08, 1.57572e-11, 10477.5, 15.3011],
                Tmin = (10, 'K'),
                Tmax = (1148.08, 'K'),
            ),
            NASAPolynomial(
                coeffs = [14.2082, 0.0663492, -3.2446e-05, 7.64531e-09, -7.04838e-13, 5805.76, -46.8743],
                Tmin = (1148.08, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (87.2229, 'kJ/mol'),
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
                coeffs = [4.04843, -0.0049632, 0.000190095, -3.12377e-07, 1.63601e-10, 4101.1, 10.905],
                Tmin = (10, 'K'),
                Tmax = (590.57, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.4663, 0.0620953, -3.84776e-05, 1.14027e-08, -1.29703e-12, 4470.66, 35.5177],
                Tmin = (590.57, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (34.0794, 'kJ/mol'),
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
                coeffs = [3.61601, 0.0421216, 0.000151389, -2.489e-07, 1.12971e-10, -6684.62, 13.2473],
                Tmin = (10, 'K'),
                Tmax = (739.358, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.18666, 0.108057, -6.34362e-05, 1.78905e-08, -1.95191e-12, -7066.45, 27.5823],
                Tmin = (739.358, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-55.5846, 'kJ/mol'),
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
                coeffs = [3.61072, 0.0473948, 0.000136213, -2.20144e-07, 9.5379e-11, 7271.12, 13.9706],
                Tmin = (10, 'K'),
                Tmax = (788.682, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.103208, 0.109241, -6.32145e-05, 1.7577e-08, -1.89323e-12, 6519.28, 22.5262],
                Tmin = (788.682, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (60.4831, 'kJ/mol'),
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
                coeffs = [3.47258, 0.0518401, -9.83785e-05, 2.1256e-07, -1.67962e-10, 4374.54, 12.5789],
                Tmin = (10, 'K'),
                Tmax = (465.46, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.536791, 0.0539153, -3.04499e-05, 8.39691e-09, -9.05101e-13, 4898.66, 27.1917],
                Tmin = (465.46, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (36.3589, 'kJ/mol'),
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
                coeffs = [2.5987, 0.154813, -0.000609282, 1.62249e-06, -1.47608e-09, 12574.9, 19.7018],
                Tmin = (10, 'K'),
                Tmax = (385.395, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.24047, 0.115904, -7.05204e-05, 2.05302e-08, -2.30192e-12, 13764, 51.8929],
                Tmin = (385.395, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (104.492, 'kJ/mol'),
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
                coeffs = [2.65588, 0.147993, -0.000555667, 1.48659e-06, -1.3621e-09, 12373.6, 19.3561],
                Tmin = (10, 'K'),
                Tmax = (384.535, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.1915, 0.116296, -7.11086e-05, 2.08017e-08, -2.3425e-12, 13507.3, 50.8724],
                Tmin = (384.535, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (102.822, 'kJ/mol'),
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
                coeffs = [2.64346, 0.149629, -0.000570468, 1.52823e-06, -1.40019e-09, 12381.2, 20.0014],
                Tmin = (10, 'K'),
                Tmax = (384.252, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.25399, 0.116365, -7.11161e-05, 2.07904e-08, -2.33967e-12, 13533.2, 51.9053],
                Tmin = (384.252, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (102.884, 'kJ/mol'),
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
                coeffs = [2.48051, 0.167114, -0.00067612, 1.75372e-06, -1.56354e-09, 12216.5, 18.2518],
                Tmin = (10, 'K'),
                Tmax = (388.366, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.51971, 0.114283, -6.91078e-05, 2.00061e-08, -2.23229e-12, 13391.7, 47.7754],
                Tmin = (388.366, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (101.51, 'kJ/mol'),
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
                coeffs = [2.58399, 0.151846, -0.000517162, 1.28765e-06, -1.12976e-09, 13655, 17.5932],
                Tmin = (10, 'K'),
                Tmax = (393.805, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.35309, 0.11298, -6.87567e-05, 2.007e-08, -2.25848e-12, 14576.6, 40.6819],
                Tmin = (393.805, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (113.486, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 6 calculated by Lawrence Lai""",
    longDesc = 
u"""

""",
)




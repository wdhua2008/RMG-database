#!/usr/bin/env python
# encoding: utf-8

name = "Lai_Hexylbenzene"
shortDesc = u"Reactions for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
In conjunction with the Lai_Hexylbenzene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to Hexylbenzene pyrolysis and supercritical water treatment.

Both calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Cantherm.
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were not used.

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation (and therefore the activation energy) by CBS-QB3 calculations to be + or - 2.4kcal/mol 
(http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448). 
"""
entry(
    index = 1,
    label = "butyl + styrene <=> rad1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(236.006, 'cm^3/(mol*s)'), n=2.7878, Ea=(15.4228, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, April 2017, CBS-QB3 level of theory"
)

entry(
    index = 2,
    label = "Hexylbenzene <=> Toluene + 1-Pentene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62907e+07, 's^-1'), n=1.6863, Ea=(309.226, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Max Liu, CBS-QB3 level of theory"
)


#!/usr/bin/env python
# encoding: utf-8

name = "Hexylbenzene2"
shortDesc = u"Beta scission reaction for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
Calculation performed by Lawrence Lai, April 2017

"""
entry(
    index = 1,
    label = "butyl + styrene <=> rad1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0697373, 'cm^3/(mol*s)'), n=3.83913, Ea=(2.23001, 'kJ/mol'), T0=(1, 'K')),
)


# -*- coding: utf-8 -*-
""" Classes for MSTM Model Manager's data model

This module provides the classes necssary for the MVC "Model" portion of the
MSTM Model Manager program.

Classes:
    Sphere
    SphereGroup
"""
from math import sqrt, pi


class Sphere:

    def __init__(self, x, y, z, r, n = 1, k = 0, rC = 0, iC = 0,
                 tmatrixFile = None):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.n = n
        self.k = k
        self.rC = rC
        self.iC = iC
        self.tmatrixFile = tmatrixFile

    def distanceFrom(self, x1, y1, z1):
        """Return the distance of the center of this sphere from the provided 
        coordinates.
        
        Args:
            x1 -- the x coord of the point from which distance is calculated
            y1 -- the y coord of the point from which distance is calculated
            z1 -- the z coord of the point from which distance is calculated
        
        Returns:
            The distance from the provided coords to the center of this sphere.
        
        """

        return (sqrt((self.x - x1) ^ 2 + (self.y - y1) ^ 2
                     + (self.z - z1) ^ 2))

    def geomXSec(self):
        """Return the geometric cross section of this sphere."""

        return (pi * self.r ^ 2)


class SphereGroup:

    def __init__(self, sphereList = list(), groupName = None, groupN = None,
                 groupK = None, groupRChiral = None, groupIChiral = None,
                 tmatrixFile = None):
        self.sphereList = sphereList
        self.shortName = groupName
        self.groupN = groupN
        self.groupK = groupK
        self.groupRChiral = groupRChiral
        self.groupIChiral = groupIChiral
        self.tmatrixFile = tmatrixFile

        if ((self.groupN is not None)
            or (self.groupK is not None)
            or (self.groupRChiral is not None)
            or (self.groupIChiral is not None)):

            self.applyOC(groupN, groupK, groupRChiral, groupIChiral)

    def addSphere(self, aSphere):
        self.sphereList.append(aSphere)

    def applyOC(self, n = None, k = None, rC = None, iC = None):
        if n is not None:
            for i in self.sphereList:
                i.n = n
        if k is not None:
            for i in self.sphereList:
                i.k = k
        if rC is not None:
            for i in self.sphereList:
                i.rC = rC
        if iC is not None:
            for i in self.sphereList:
                i.iC = iC
from paramak.shape import Shape
import pytest
import math
import paramak
from capsule_vacuum_vessel import CapsuleVacuumVessel
'''This tests the length of the list of points created by the point find function. 
12 points should be calculated plus an addition of the first point at the end of the list to create a link'''
def test_pointnum1():
     shape = CapsuleVacuumVessel((0,0),300,10)
     pointnum = len(shape.points)
     
     assert pointnum == 13

def test_pointnum2():
     shape = CapsuleVacuumVessel((100,-100),400,25)
     pointnum = len(shape.points)
     assert pointnum == 13

def test_pointnum3():
     shape = CapsuleVacuumVessel((1000,-500),5000,50)
     pointnum = len(shape.points)
     assert pointnum == 13

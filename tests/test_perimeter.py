import pytest
import math
import paramak
from capsule_vacuum_vessel import CapsuleVacuumVessel
'''This test evaluates the perimeter of the resultant points and asserts them agaist the known value'''

def perimeter(outer_start_point,radius,thickness):

    test_shape = CapsuleVacuumVessel(
        outer_start_point = outer_start_point,
        radius = radius,
        thickness = thickness
    )
    point1 = test_shape.points[0]
    point2 = test_shape.points[1]
    point3 = test_shape.points[2]
    point4 = test_shape.points[3]
    point5 = test_shape.points[4]
    point6 = test_shape.points[5]
    point7 = test_shape.points[6]
    point8 = test_shape.points[7]
    point9 = test_shape.points[8]
    point10 = test_shape.points[9]
    point11 = test_shape.points[10]
    point12 = test_shape.points[11]
    
    straightedges = float((point12[1]-point1[1]) + (point6[1]-point7[1]) + (point4[1]-point3[1]) + (point9[1]-point10[1]))
    curvededges = float((math.pi*radius) + (math.pi*(radius-thickness)))
    total = float(straightedges + curvededges)

    return total

def test_perimeter1():
    testp = round(perimeter((0,0),300,10),2)
    assert testp == 3073.54

def test_perimeter2():
    testp = round(perimeter((100,-100),400,25),2)
    assert testp == 4084.73

def test_perimeter3():
    testp = round(perimeter((1000,-500),5000,50),2)
    assert testp == 51358.85
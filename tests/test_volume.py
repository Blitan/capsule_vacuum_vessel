import pytest
import math
import paramak
from capsule_vacuum_vessel import CapsuleVacuumVessel

def volume(outer_start_point,radius,thickness,angle):

    test_shape = CapsuleVacuumVessel(
        outer_start_point = outer_start_point,
        radius = radius,
        thickness = thickness,
        rotation_angle = angle
    )
    
    point3 = test_shape.points[2]
    point4 = test_shape.points[3]
    
    point9 = test_shape.points[8]
    point10 = test_shape.points[9]
    

    outer_volume_cylinder = float(math.pi * (radius**2) * (point4[1]-point3[1]))
    inner_volume_cylinder = float(math.pi * ((radius-thickness)**2) * (point9[1]-point10[1]))
    outer_volume_sphere = float((4/3)*math.pi*(radius**3))
    inner_volume_sphere = float((4/3)*math.pi*((radius-thickness)**3))
    outer_volume = outer_volume_sphere + outer_volume_cylinder
    inner_volume = inner_volume_cylinder + inner_volume_sphere
    total_volume = (angle/360) * (outer_volume-inner_volume)
    
    return total_volume

volume((0,0),300,10,180)

def testvolume1():
    testvol = round(volume((0,0),300,10,180),2)
    assert testvol == 11029084.61

def testvolume2():
    testvol = round(volume((100,-100),400,25,360),2)
    assert testvol == 95884025.78

def testvolume3():
    testvol = round(volume((1000,-500),5000,50,90),2)
    assert testvol == 7795207671.41

from capsule_vacuum_vessel import point_find

def test_pointnum1():
     pointnum = len(point_find((0,0),300,10))
     assert pointnum == 12

def test_pointnum2():
     pointnum = len(point_find((100,-100),400,25))
     assert pointnum == 12

def test_pointnum3():
     pointnum = len(point_find((1000,-500),5000,50))
     assert pointnum == 12


from capsule_vacuum_vessel import point_find

def test_pointnum1():
     pointnum = len(point_find((0,0),300,10))
     assert pointnum == 12


import math
import paramak

def point_find(outer_start_point,radius,thickness):
    
    bottom_outer_x, bottom_outer_y = outer_start_point
    top_outer_y = bottom_outer_y + (4 * radius)
    top_outer_x = bottom_outer_x
    inner_r = radius - thickness
    bottom_outer_x, bottom_outer_y, thickness, radius, top_outer_x, top_outer_y, inner_r = float(bottom_outer_x), float(bottom_outer_y), float(thickness), float(radius), float(top_outer_x), float(top_outer_y), float(inner_r)
    
    p1 = (bottom_outer_x,bottom_outer_y, 'circle')
    p3 = (p1[0] + radius, p1[1] + radius, 'straight')
    p4 = (p3[0], p3[1] + radius*2, 'circle')
    p6 = (top_outer_x,top_outer_y, 'straight')
    p7 = (p6[0],p6[1] - thickness, 'circle')
    p9 = (p4[0]-thickness, p4[1],'straight')
    p10 = (p3[0] - thickness, p3[1],'circle')
    p12 = (p1[0], p1[1] + thickness, 'straight')
    p2 = ((p1[0]) + (radius*math.cos((3*math.pi)/8)),(p1[1]+radius) -(radius*math.sin((3*math.pi)/8)),'circle')
    p5 = ((p6[0] + (radius*math.cos((2*math.pi)/8))),(p6[1] - radius) + (radius*math.sin((2*math.pi)/8)),'circle')
    p8 = ((p7[0] + (inner_r*math.cos((2*math.pi)/8))),(p7[1] - inner_r) + (inner_r*math.sin((2*math.pi)/8)),'circle')
    p11 = ((p12[0]) + (inner_r*math.cos((3*math.pi)/8)),(p12[1]+inner_r) -(inner_r*math.sin((3*math.pi)/8)),'circle')
    
    return [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
    
points = point_find((0,0),300,10)
print(points)

def vacuum_vessel(outer_start_point,radius,thickness,angle):
    
    pointsfind= point_find(outer_start_point,radius,thickness)
    
    vacuum_vessel = paramak.RotateMixedShape(
        rotation_angle=angle,
       
        points = point_find(outer_start_point,radius,thickness)
        
    )
    stp_filename="Capsule_shaped_vacuum_vessel.stp"

    vacuum_vessel.export_stp("Capsule_shaped_vacuum_vessel.stp")

vacuum_vessel((0,0),300,10,180)

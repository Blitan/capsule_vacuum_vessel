def point_find(outer_start_point,radius,thickness):
    
    bottom_outer_x, bottom_outer_y = outer_start_point
    bottom_outer_x, bottom_outer_y, thickness, radius = float(bottom_outer_x), float(bottom_outer_y), float(thickness), float(radius)
    
    p1 = (bottom_outer_x,bottom_outer_y)
    p3 = (p1[0] + radius, p1[1] + radius)
    p4 = (p3[0], p3[1] + radius*2)
    p6 = (p1[0],p1[1]+ 4*radius)
    p7 = (p6[0],p6[1] - thickness)
    p9 = (p4[0]-thickness, p4[1])
    p10 = (p3[0] - thickness, p3[1])
    p12 = (p1[0], p1[1] + thickness)
    
    print(p1,p3,p4,p6,p7,p9,p10,p12)
    
point_find((0,0),300,10)
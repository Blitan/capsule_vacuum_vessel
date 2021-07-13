from typing import Optional, Tuple
from paramak import RotateMixedShape
import math


class CapsuleVacuumVessel(RotateMixedShape):
    """A cylindrical vessel volume with constant thickness that has addition sphereical edges.
    Arguments:
        outer_start_point: the x,z coordinates of the outer bottom of the vacuum vessel
        radius: the radius from which the centres of the vessel meets the outer circumference. 
        thickness: the radial thickness of the vessel in cm.
        stp_filename: Defaults to "CapsuleVacuumVessel.stp".
        stl_filename: Defaults to "CapsuleVacuumVessel.stl".
        material_tag: Defaults to "capsule_vacuum_vessel_mat".
    """

    def __init__(
        self,
        
        radius: float,
        outer_start_point: Tuple[float,float],
        thickness: float,
        stp_filename: Optional[str] = "CapsuleVacuumVessel.stp",
        stl_filename: Optional[str] = "CapsuleVacuumVessel.stl",
        material_tag: Optional[str] = "capsule_vacuum_vessel_mat",
        **kwargs
    ):
        self.radius = radius
        self.thickness = thickness
        self.outer_start_point = outer_start_point[0], outer_start_point[1]
        super().__init__(
            material_tag=material_tag,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )
    

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.radius must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.radius must be a positive number above 0. Not', value)
        self._radius = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.thickness must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.thickness must be a positive number above 0. Not', value)
        self._thickness = value
        
    
   
                
    


    def find_points(self):
        """
        Finds the XZ points joined by straight and circle connections that describe the
        2D profile of the vessel shape.
        """
        
        radius = self.radius
        thickness = self.thickness
        bottom_outer_x, bottom_outer_y = self.outer_start_point
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
    
        self.points = [
            p1,
            p2,
            p3,
            p4,
            p5,
            p6,
            p7,
            p8,
            p9,
            p10,
            p11,
            p12
        ]


class RoundedVacuumVessel(RotateMixedShape):
    """A reactangular vessel volume with constant thickness that has addition rounded edges.
    Arguments:
        outer_start_point: the x,z coordinates of the outer bottom of the vacuum vessel
        radius: the radius from which the centres of the vessel meets the curved edge. 
        thickness: the radial thickness of the vessel in cm.
        stp_filename: Defaults to "CapsuleVacuumVessel.stp".
        stl_filename: Defaults to "CapsuleVacuumVessel.stl".
        material_tag: Defaults to "capsule_vacuum_vessel_mat".
    """

    def __init__(
        self,
        
        radius: float,
        height: float,
        outer_start_point: Tuple[float,float],
        thickness: float,
        stp_filename: Optional[str] = "RoundedVacuumVessel.stp",
        stl_filename: Optional[str] = "RoundedVacuumVessel.stl",
        material_tag: Optional[str] = "rounded_vacuum_vessel_mat",
        **kwargs
    ):
        self.radius = radius
        self.height = height
        self.thickness = thickness
        self.outer_start_point = outer_start_point[0], outer_start_point[1]
        super().__init__(
            material_tag=material_tag,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )
    

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.radius must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.radius must be a positive number above 0. Not', value)
        self._radius = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.thickness must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.thickness must be a positive number above 0. Not', value)
        self._thickness = value
        
    
   
                
    


    def find_points(self):
        """
        Finds the XZ points joined by straight and circle connections that describe the
        2D profile of the vessel shape.
        """
        
        radius = self.radius
        height = self.height
        thickness = self.thickness
        top_outer_x, top_outer_y = self.outer_start_point
        
        inner_r = radius - thickness
        mid_length = height - (2 * radius)
        thickness, radius, top_outer_x, top_outer_y, inner_r,mid_length = float(thickness), float(radius), float(top_outer_x), float(top_outer_y), float(inner_r),float(mid_length)
    
        p1 = (top_outer_x,top_outer_y, 'straight')
        p2 = (p1[0] + radius, p1[1], 'circle')
        p3 = ((p2[0] + (radius*math.cos((2*math.pi)/8))),(p2[1] - radius) + (radius*math.sin((2*math.pi)/8)),'circle')
        p4 = (p2[0]+radius,p2[1]-radius,'straight')
        p5 = (p4[0],p4[1]-mid_length,'circle')
        p7 = (p5[0]-radius,p5[1]-radius,'straight')
        p6 = ((p7[0]) + (radius*math.cos((3*math.pi)/8)),(p7[1]+radius) -(radius*math.sin((3*math.pi)/8)),'circle')
        p8 = (p7[0]-radius,p7[1],'straight')
        p9 = (p8[0],p8[1]+thickness,'straight')
        p10 = (p9[0]+radius,p9[1],'circle')
        p11 = ((p10[0]) + (inner_r*math.cos((3*math.pi)/8)),(p10[1]+inner_r) -(inner_r*math.sin((3*math.pi)/8)),'circle')
        p12 = (p10[0]+inner_r,p10[1]+inner_r,'straight')
        p13 = (p12[0],p12[1]+mid_length,'circle')
        p15 = (p13[0]-inner_r,p13[1]+inner_r,'straight')
        p14 = ((p15[0] + (inner_r*math.cos((2*math.pi)/8))),(p15[1] - inner_r) + (inner_r*math.sin((2*math.pi)/8)),'circle')
        p16 = (p15[0]-radius,p15[1],'straight')
    
        self.points = [
            p1,
            p2,
            p3,
            p4,
            p5,
            p6,
            p7,
            p8,
            p9,
            p10,
            p11,
            p12,
            p13,
            p14,
            p15,
            p16

        ]

class RoundedVacuumVesselInnerLeg(RotateMixedShape):
    """A reactangular vessel volume with constant thickness that has rounded edges and an inner leg.
    Arguments:
        outer_start_point: the x,z coordinates of the outer bottom of the vacuum vessel
        radius: the radius from which the centres of the vessel meets the curved edge. 
        height: the total height of the vacuum vessel
        thickness: the radial thickness of the vessel in cm.
        inner_leg_thickness: the thickness of the inner leg
        stp_filename: Defaults to "CapsuleVacuumVessel.stp".
        stl_filename: Defaults to "CapsuleVacuumVessel.stl".
        material_tag: Defaults to "capsule_vacuum_vessel_mat".
    """

    def __init__(
        self,
        
        radius: float,
        height: float,
        inner_leg_thickness: float,
        outer_start_point: Tuple[float,float],
        thickness: float,
        stp_filename: Optional[str] = "RoundedVacuumVessel.stp",
        stl_filename: Optional[str] = "RoundedVacuumVessel.stl",
        material_tag: Optional[str] = "rounded_vacuum_vessel_mat",
        **kwargs
    ):
        self.radius = radius
        self.height = height
        self.thickness = thickness
        self.inner_leg_thickness = inner_leg_thickness
        self.outer_start_point = outer_start_point[0], outer_start_point[1]
        super().__init__(
            material_tag=material_tag,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )
    

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.radius must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.radius must be a positive number above 0. Not', value)
        self._radius = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError(
                'VacuumVessel.thickness must be a number. Not', value)
        if value <= 0:
            raise ValueError(
                'VacuumVessel.thickness must be a positive number above 0. Not', value)
        self._thickness = value
        
    
   
                
    


    def find_points(self):
        """
        Finds the XZ points joined by straight and circle connections that describe the
        2D profile of the vessel shape.
        """
        
        radius = self.radius
        height = self.height
        thickness = self.thickness
        top_outer_x, top_outer_y = self.outer_start_point
        inner_leg_thickness = self.inner_leg_thickness
        
        inner_r = radius - thickness
        mid_length = height - (2 * radius)
        thickness, radius, top_outer_x, top_outer_y, inner_r,mid_length, inner_leg_thickness = float(thickness), float(radius), float(top_outer_x), float(top_outer_y), float(inner_r),float(mid_length),float(inner_leg_thickness)
    
        p1 = (top_outer_x,top_outer_y, 'straight')
        p2 = (p1[0] + radius, p1[1], 'circle')
        p3 = ((p2[0] + (radius*math.cos((2*math.pi)/8))),(p2[1] - radius) + (radius*math.sin((2*math.pi)/8)),'circle')
        p4 = (p2[0]+radius,p2[1]-radius,'straight')
        p5 = (p4[0],p4[1]-mid_length,'circle')
        p7 = (p5[0]-radius,p5[1]-radius,'straight')
        p6 = ((p7[0]) + (radius*math.cos((3*math.pi)/8)),(p7[1]+radius) -(radius*math.sin((3*math.pi)/8)),'circle')
        p8 = (p7[0]-radius,p7[1],'straight')
        p9 = (p8[0],p8[1]+thickness,'straight')
        p10 = (p9[0]+radius,p9[1],'circle')
        p11 = ((p10[0]) + (inner_r*math.cos((3*math.pi)/8)),(p10[1]+inner_r) -(inner_r*math.sin((3*math.pi)/8)),'circle')
        p12 = (p10[0]+inner_r,p10[1]+inner_r,'straight')
        p13 = (p12[0],p12[1]+mid_length,'circle')
        p15 = (p13[0]-inner_r,p13[1]+inner_r,'straight')
        p14 = ((p15[0] + (inner_r*math.cos((2*math.pi)/8))),(p15[1] - inner_r) + (inner_r*math.sin((2*math.pi)/8)),'circle')
        p16 = (p15[0]-radius+inner_leg_thickness,p15[1],'straight')
        p17 = (p9[0]+inner_leg_thickness,p9[1],'straight')
        p18 = (p9[0],p9[1],'straight')
        
    
        self.points = [
            p1,
            p2,
            p3,
            p4,
            p5,
            p6,
            p7,
            p8,
            p9,
            p10,
            p11,
            p12,
            p13,
            p14,
            p15,
            p16,
            p17,
            p18,
            

        ]
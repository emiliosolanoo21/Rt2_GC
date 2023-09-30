import mathLib as ml
from math import tan, pi, atan2, acos

class Intercept(object):
    def __init__(self, distance, point, texcoords, normal, obj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.obj = obj

class Shape(object):
    def __init__(self,position,material):
        self.position = position
        self.material = material

    def ray_intersect(self,orig,dir):
        return None

class Sphere(Shape):
    def __init__(self,position,radius,material):
        self.radius = radius
        super().__init__(position,material)
        
    def ray_intersect(self, orig, dir):
        l = ml.substractV(self.position, orig)
        lengthL = ml.magV(l)
        tca = ml.dotProd(l,dir)
        
        #if radius < d: no hay contacto (False)
        #if radius > d: si hay contacto (True)
        d = (lengthL**2 - tca**2)**0.5
        if d > self.radius:
            return None
        
        thc = (self.radius**2 - d**2)**0.5
        t0 = tca - thc
        t1 = tca + thc
        
        if t0<0:
            t0 = t1
        if t0<0:
            return None
        
        #P = O+D*t0
        p = ml.addV(orig,ml.VxE(dir, t0))
        normal = ml.substractV(p,self.position)
        normal = ml.normalizeV(normal)
        
        u = (atan2(normal[2], normal[0]) / (2*pi)) + 0.5
        v = acos(normal[1]) / pi
        
        return Intercept(distance = t0,
                         point = p,
                         normal = normal,
                         texcoords= (u,v),
                         obj = self)
        
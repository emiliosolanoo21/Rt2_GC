import pygame
from pygame.locals import * 
from rt import Raytracer
from figures import *
from lights import *
from materials import *

width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

raytracer = Raytracer(screen)

#Se puede usar cualquier formato de imagen.
#hdri-hub.com
raytracer.envMap = pygame.image.load("images/night.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)

flowTexture = pygame.image.load("images/flow.jpg")

brick = Material(diffuse=(1,0.4,0.4), spec = 8,  ks = 0.01)
grass = Material(diffuse=(0.4,1,0.4), spec = 32,  ks = 0.1)
water = Material(diffuse=(0.4,0.4,1), spec = 256, ks = 0.2)

mirror = Material(diffuse=(0.9,0.9,0.9), spec = 64, ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9), spec = 32, ks = 0.15, matType = REFLECTIVE)
colorFlow = Material(texture = flowTexture)
reflectFlow = Material(texture = flowTexture, spec = 64, ks = 0.1, matType= REFLECTIVE)

glass = Material(diffuse=(0.9,0.9,0.9), spec = 64, ks = 0.15, ior = 1.5, matType = TRANSPARENT)
diamond = Material(diffuse=(0.9,0.9,0.9), spec = 128, ks = 0.2, ior = 2.417, matType = TRANSPARENT)
water = Material(diffuse=(0.4,0.4,1.0), spec = 128, ks = 0.2, ior = 1.33, matType = TRANSPARENT)

""" raytracer.scene.append(Sphere(position=(1,1,-5), radius = 0.5, material = grass))
raytracer.scene.append(Sphere(position=(0.5,-1,-5), radius = 0.3, material = water)) """

""" raytracer.scene.append(Sphere(position=(-2,0,-7), radius = 1.5, material = reflectFlow))
raytracer.scene.append(Sphere(position=(2,0,-7), radius = 2, material = colorFlow))
raytracer.scene.append(Sphere(position=(0,-1,-5), radius = 0.5, material = mirror)) """

raytracer.scene.append(Sphere(position=(-1,0,-5), radius = 1, material = glass))
raytracer.scene.append(Sphere(position=(1,0,-5), radius = 0.7, material = diamond))
raytracer.scene.append(Sphere(position=(0,1,-8), radius = 1, material = brick))

""" raytracer.scene.append(Sphere(position=(0,0,-5), radius = 1.5, material = water)) """

#iluminacion minima del ambiente
raytracer.lights.append(AmbientLight(intensity=0.1))
raytracer.lights.append(DirectionalLight(direction=(-1,-1,-1), intensity=0.9))
#raytracer.lights.append(PointLight(point=(1.5,0,-5), intensity=1, color= (1,0,1)))

raytracer.rtClear()
raytracer.rtRender()

print("\nTiempo de renderizado:", pygame.time.get_ticks() / 1000, "segundos")

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning=False
                
pygame.quit()           
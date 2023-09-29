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

#Carga de texturas
flowTexture = pygame.image.load("images/flow.jpg")
CLTexture = pygame.image.load("images/Champions.jpg")
JabulaniTexture = pygame.image.load("images/Jabulani.jpg")
discoTexture = pygame.image.load("images/discoBall.jpg")
TGTexture = pygame.image.load("images/Teamgeist.jpg")

#Carga de materiales
Jabulani = Material(texture = JabulaniTexture, spec = 20, ks = 0.01)
Teamgeist = Material(texture = TGTexture, spec = 5,  ks = 0.5)

reflectFlow = Material(texture = flowTexture, spec = 64, ks = 0.1, matType= REFLECTIVE)
discoBall = Material(texture = discoTexture, spec = 200, ks = 0.45, matType= REFLECTIVE)

CLBall = Material(texture = CLTexture, spec = 64, ks = 0.15, ior = 4.5, matType = TRANSPARENT)
Heineken = Material(diffuse=(0,0.478,0.082), spec = 100, ks = 0.05, ior = 1.5, matType = TRANSPARENT)

#Posicionamiento de esferas
raytracer.scene.append(Sphere(position=(-1.5,0.75,-5), radius = 0.5, material = Jabulani))
raytracer.scene.append(Sphere(position=(-1.5,-0.75,-5), radius = 0.5, material = Teamgeist))

raytracer.scene.append(Sphere(position=(0,0.75,-5), radius = 0.5, material = reflectFlow))
raytracer.scene.append(Sphere(position=(0,-0.75,-5), radius = 0.5, material = discoBall))

raytracer.scene.append(Sphere(position=(1.5,0.75,-5), radius = 0.5, material = CLBall))
raytracer.scene.append(Sphere(position=(1.5,-0.75,-5), radius = 0.5, material = Heineken))

#iluminacion minima del ambiente
raytracer.lights.append(AmbientLight(intensity=0.15))
raytracer.lights.append(DirectionalLight(direction=(-2,-3,-1), intensity=0.75))
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

rect = pygame.Rect(0,0,width,height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "Rt2.jpg")
                
pygame.quit()           
#Yadira Fuentes Calderón, A01745235
#Programa que genera un espirógrafo con datos introducidos por el usuario

import pygame
import math
import random


ANCHO = 1080
ALTO = 720

BLANCO = (255, 255, 255)



def crearColor():
    rojo= random.randint(0,255)
    verde= random.randint(0,255)
    azul= random.randint(0,255)

    return(rojo,verde,azul)

def dibujar(r,R,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        radio = 100

        for angulo in range (0,360*(r//math.gcd(r,R)),1):
            color=crearColor()

            a = math.radians(angulo)

            k= r/R
            x= int(R*(((l-k)*math.cos(a)+l*k*math.cos(((l-k)/k)*a))))
            y= int(R*(((l-k)*math.sin(a)+l*k*math.sin(((l-k)/k)*a))))

            pygame.draw.circle(ventana, (color), (x+ANCHO//2,ALTO//2-y), 1)

        pygame.display.flip()
        reloj.tick(1)


    pygame.quit()



def main():
    r= int(input("Introduce la r: "))
    R= int(input("Introduce la R: "))
    l= float(input("Introduce la l : "))


    dibujar(r,R,l)   #20,100,3


main()
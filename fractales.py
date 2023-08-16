from math import cos, pi, sin
from random import randint
import sys
from pygame import *

sys.setrecursionlimit(10000)

# random color
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def random_gradiant():
    return random_color(), random_color()

# fonction qui dessine un triangle
def triangle(x1, y1, x2, y2, x3, y3, color):
    draw.polygon(fenetre, color, [(x1, y1), (x2, y2), (x3, y3)])


# fonction récursive qui dessine des triangles imbriqués
def triangle_fractale(depth, x1, y1, x2, y2, x3, y3, colors):
    # si la profondeur est nulle, on dessine un triangle
    triangle(x1, y1, x2, y2, x3, y3, colors[depth])
    if depth == 0:
        pass
    # sinon, on divise le triangle en 4 triangles plus petits
    else:
        angle = pi/100
        rotation_mat = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
        factor = 99/100

        # calcul des coordonnées des points du triangle 2/3 plus petit après une rotaion autour du point (x1, y1)

        x2 = factor*(x2-x1) + x1
        y2 = factor*(y2-y1) + y1
        x3 = factor*(x3-x1) + x1
        y3 = factor*(y3-y1) + y1
        
        x2, y2 = x2-x1, y2-y1
        x3, y3 = x3-x1, y3-y1
        x2, y2 = rotation_mat[0][0]*x2 + rotation_mat[0][1]*y2, rotation_mat[1][0]*x2 + rotation_mat[1][1]*y2
        x3, y3 = rotation_mat[0][0]*x3 + rotation_mat[0][1]*y3, rotation_mat[1][0]*x3 + rotation_mat[1][1]*y3
        x2, y2 = x2+x1, y2+y1
        x3, y3 = x3+x1, y3+y1

        # appel récursif sur un triangle plus petit avec une rotation de 31degrés (de profondeur n-1)
        
        triangle_fractale(depth-1, x1, y1, x2, y2, x3, y3, colors)

# fonction qui dessine une branche
def branche(x1, y1, x2, y2, color):
    draw.line(fenetre, color, (x1, y1), (x2, y2))

# création d'une fenêtre
fenetre = display.set_mode((1000, 900))

# profondeur de la fractale
depth = 3000

# création des couleurs liées à la profondeur
colors = []

# couleurs par gradiant
gradiant = random_gradiant()
if(depth>100):
    for i in range(depth+1):
            if(i%100==0 and i != 0):
                gradiant = (gradiant[1],random_color())
                colors.append(gradiant[0])
            else:
                colors.append((gradiant[0][0] + (gradiant[1][0] - gradiant[0][0]) * (i%100) / 100, gradiant[0][1] + (gradiant[1][1] - gradiant[0][1]) * (i%100) / 100, gradiant[0][2] + (gradiant[1][2] - gradiant[0][2]) * (i%100) / 100))
else:
    for i in range(depth+1):
        colors.append((gradiant[0][0] + (gradiant[1][0] - gradiant[0][0]) * i / depth, gradiant[0][1] + (gradiant[1][1] - gradiant[0][1]) * i / depth, gradiant[0][2] + (gradiant[1][2] - gradiant[0][2]) * i / depth))

# couleurs aléatoires
# for i in range(depth+1):
#     colors.append(random_color())

# dessin de la fractale
triangle_fractale(depth, 500, 450, 1000, 0, 1000, 1000, colors)

# mise à jour de l'affichage
display.flip()

# attente d'un clic de souris
while event.wait().type != MOUSEBUTTONDOWN:
    pass

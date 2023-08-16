from math import cos, pi, sin
from random import randint
from pygame import *

# random color
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# fonction qui dessine un triangle
def triangle(x1, y1, x2, y2, x3, y3, color):
    draw.line(fenetre, color, (x1, y1), (x2, y2))
    draw.line(fenetre, color, (x2, y2), (x3, y3))
    draw.line(fenetre, color, (x3, y3), (x1, y1))

# fonction récursive qui dessine des triangles imbriqués
def triangle_fractale(depth, x1, y1, x2, y2, x3, y3, colors):
    # si la profondeur est nulle, on dessine un triangle
    triangle(x1, y1, x2, y2, x3, y3, colors[depth])
    if depth == 0:
        pass
    # sinon, on divise le triangle en 4 triangles plus petits
    else:
        angle = pi/6
        rotation_mat = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]

        # calcul des coordonnées des points du triangle 2/3 plus petit après une rotaion autour du point (x1, y1)
        x2 = 2*(x2-x1)/3 + x1
        y2 = 2*(y2-y1)/3 + y1
        x3 = 2*(x3-x1)/3 + x1
        y3 = 2*(y3-y1)/3 + y1
        
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
fenetre = display.set_mode((640, 480))

# profondeur de la fractale
depth = 10

# création des couleurs liées à la profondeur
colors = []
for i in range(depth+1):
    colors.append(random_color())

# dessin de la fractale
triangle_fractale(depth, 320, 240, 20, 460, 620, 460, colors)

# mise à jour de l'affichage
display.flip()

# attente d'un clic de souris
while event.wait().type != MOUSEBUTTONDOWN:
    pass

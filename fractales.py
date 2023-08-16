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
    # draw.line(fenetre, color, (x1, y1), (x2, y2))
    # draw.line(fenetre, color, (x2, y2), (x3, y3))
    # draw.line(fenetre, color, (x3, y3), (x1, y1))


# fonction récursive qui dessine des triangles imbriqués
def triangle_fractale(depth, x1, y1, x2, y2, x3, y3, colors):
    # si la profondeur est nulle, on dessine un triangle
    triangle(x1, y1, x2, y2, x3, y3, colors[depth])
    if depth == 0:
        pass
    # sinon, on divise le triangle en 4 triangles plus petits
    else:
        angle = pi/200
        rotation_mat = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
        factor = 99/100

        centrex = 500
        centrey = 500

        centrex2 = (x1+x3)/2
        centrey2 = (y1+y3)/2

        centrex3 = (x2+x3)/2
        centrey3 = (y2+y3)/2

        x1 = factor*(x1-centrex) + centrex
        y1 = factor*(y1-centrey) + centrey
        x2 = factor*(x2-centrex) + centrex
        y2 = factor*(y2-centrey) + centrey
        x3 = factor*(x3-centrex) + centrex
        y3 = factor*(y3-centrey) + centrey

        # calcul des coordonnées des points du triangle plus petit après une rotaion autour du point (x1, y1)
        
        
        x4, y4 = x1-centrex, y1-centrey
        x5, y5 = x2-centrex, y2-centrey
        x6, y6 = x3-centrex, y3-centrey
        x4, y4 = rotation_mat[0][0]*x4 + rotation_mat[0][1]*y4, rotation_mat[1][0]*x4 + rotation_mat[1][1]*y4
        x5, y5 = rotation_mat[0][0]*x5 + rotation_mat[0][1]*y5, rotation_mat[1][0]*x5 + rotation_mat[1][1]*y5
        x6, y6 = rotation_mat[0][0]*x6 + rotation_mat[0][1]*y6, rotation_mat[1][0]*x6 + rotation_mat[1][1]*y6
        x4, y4 = x4+centrex, y4+centrey
        x5, y5 = x5+centrex, y5+centrey
        x6, y6 = x6+centrex, y6+centrey

        # calcul des coordonnées des points du triangle plus petit après une rotaion autour du point (x2, y3)

        x7, y7 = x1-centrex2, y1-centrey2
        x8, y8 = x2-centrex2, y2-centrey2
        x9, y9 = x3-centrex2, y3-centrey2
        x7, y7 = rotation_mat[0][0]*x7 + rotation_mat[0][1]*y7, rotation_mat[1][0]*x7 + rotation_mat[1][1]*y7
        x8, y8 = rotation_mat[0][0]*x8 + rotation_mat[0][1]*y8, rotation_mat[1][0]*x8 + rotation_mat[1][1]*y8
        x9, y9 = rotation_mat[0][0]*x9 + rotation_mat[0][1]*y9, rotation_mat[1][0]*x9 + rotation_mat[1][1]*y9
        x7, y7 = x7+centrex2, y7+centrey2
        x8, y8 = x8+centrex2, y8+centrey2
        x9, y9 = x9+centrex2, y9+centrey2

        # calcul des coordonnées des points du triangle plus petit après une rotaion autour du point (x3, y3)

        x10, y10 = x1-x3, y1-y3
        x11, y11 = x2-x3, y2-y3
        x12, y12 = x3-x3, y3-y3
        x10, y10 = rotation_mat[0][0]*x10 + rotation_mat[0][1]*y10, rotation_mat[1][0]*x10 + rotation_mat[1][1]*y10
        x11, y11 = rotation_mat[0][0]*x11 + rotation_mat[0][1]*y11, rotation_mat[1][0]*x11 + rotation_mat[1][1]*y11
        x12, y12 = rotation_mat[0][0]*x12 + rotation_mat[0][1]*y12, rotation_mat[1][0]*x12 + rotation_mat[1][1]*y12
        x10, y10 = x10+x3, y10+y3
        x11, y11 = x11+x3, y11+y3
        x12, y12 = x12+x3, y12+y3

        # appel récursif
        triangle_fractale(depth-1, x4, y4, x5, y5, x6, y6, colors)
        # triangle_fractale(depth-1, x7, y7, x8, y8, x9, y9, colors)
        # triangle_fractale(depth-1, x10, y10, x11, y11, x12, y12, colors)
        

# fonction qui dessine une branche
def branche(x1, y1, x2, y2, color):
    draw.line(fenetre, color, (x1, y1), (x2, y2))

# création d'une fenêtre
fenetre = display.set_mode((1000, 900))

# profondeur de la fractale
depth = 1000

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
triangle_fractale(depth, 500, 450, 0, 1000, 1000, 1000, colors)
triangle_fractale(depth, 500, 450, 0, 0, 1000, 0, colors)
triangle_fractale(depth, 500, 450, 0, 0, 0, 1000, colors)
triangle_fractale(depth, 500, 450, 1000, 0, 1000, 1000, colors)

# mise à jour de l'affichage
display.flip()

# attente d'un clic de souris
while event.wait().type != MOUSEBUTTONDOWN:
    pass

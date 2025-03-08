from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
import math

points = []
speed = 0.02
prev_state_speed = 0.02
space_down = False

cover = False
alpha = 1

w_width = 800
w_height = 800

def draw_cover():
    global alpha
    
    period = abs(math.sin(time.time()))
    if period > 0.6:
        alpha = 1
    if period < 0.4:
        alpha = 0
    
    glColor4f(0,0,0,alpha) 
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(0,w_height)
    glVertex2f(w_width,w_height)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(w_width,w_height)
    glVertex2f(w_width,0)
    glEnd()


def update_points():
    global speed
    for point in points:
        # Updating ball position based on direction and speed
        point["x"] += point["dir_x"] * speed
        point["y"] += point["dir_y"] * speed

        # Bouncing off walls logic using reversing x and y direction multiplying -1
        if point["x"] <= 0 or point["x"] >= w_width:
            point["dir_x"] *= -1  
        if point["y"] <= 0 or point["y"] >= w_height:
            point["dir_y"] *= -1  

    glutPostRedisplay()

def draw_points(x, y, color):
    glColor3f(*color)
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def mouse_click(button, state, x, y):
    global cover, blink_start_time
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        point_dict = {
        "x": x,
        "y": w_height - y, # Convertg window coordinate to opengl coordinate(bottom-left) 
        "dir_x": random.choice([-1, 1]), 
        "dir_y": random.choice([-1, 1]),
        "color": (random.random(), random.random(), random.random())
        }
        points.append(point_dict)  # Store the point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        cover = not cover 

    
        glutPostRedisplay()  
def special_key_listener(key, x, y):
    global speed
    if key == GLUT_KEY_UP:
        speed+=0.01
    if key == GLUT_KEY_DOWN:
        if speed > 0.01:
            speed-=0.01
    glutPostRedisplay()  
        
def keyboard_listener(key, x, y):
    global speed, prev_state_speed, space_down

    if key == b' ':
        if space_down == False:
            prev_state_speed = speed 
            speed = 0.0
            space_down = True
        else:
            speed = prev_state_speed 
            space_down = False

    glutPostRedisplay()  
    
def reshape(width, height):
    global w_width, w_height
    w_width = width
    w_height = height
    glViewport(0, 0, w_width, w_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w_width, 0.0, w_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glEnable(GL_BLEND) #enable blending.
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    for point in points:
        draw_points(point['x'], point['y'], point['color'])

    if cover == True:
        draw_cover()
    
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w_width, w_height) #window size
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Magic Box Simulation") #window title name 
    glutDisplayFunc(showScreen)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse_click)
    glutSpecialFunc(special_key_listener)
    glutKeyboardFunc(keyboard_listener)
    glutIdleFunc(update_points) 
    glutMainLoop()
    return 0

if __name__ == "__main__":
    main()
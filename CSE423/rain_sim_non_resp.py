from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time
import math

light_dark_intensity = 0.0
speed = 5
drop_positions = []
drop_val = []
angle = 0


#Ground
def ground():
    glColor3f(0.60, 0.45, 0.10)
    glBegin(GL_TRIANGLES)
    glVertex(0,0)
    glVertex(0,700)
    glVertex(1800,700)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex(0,0)
    glVertex(1800,700)
    glVertex(1800,0)
    glEnd()

def house():

    # House white box
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(600,300)
    glVertex2f(600,600)
    glVertex2f(1200,600)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glVertex2f(1200,600)
    glVertex2f(600,300)
    glVertex2f(1200,300)
    glEnd()
    # Roof
    glColor3f(0.62, 0.12, 0.94)
    glBegin(GL_TRIANGLES)
    glVertex2f(900,760)
    glVertex2f(560,600)
    glVertex2f(1260,600)
    glEnd()
    # Door 
    glColor3f(0.196, 0.616, 0.969)
    glBegin(GL_TRIANGLES)
    glVertex2f(850,300)
    glVertex2f(850,520)
    glVertex2f(960,520)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(850,300)
    glVertex2f(960,300)
    glVertex2f(960,520)
    glEnd()

    # Door knob
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(930,400)
    glEnd()

    # Windows 
    # Left 
    glColor3f(0.196, 0.616, 0.969)
    glBegin(GL_TRIANGLES)
    glVertex2f(700,400)
    glVertex2f(700,500)
    glVertex2f(800,500)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(700,400)
    glVertex2f(800,500)
    glVertex2f(800,400)
    glEnd()

    # Right 
    glBegin(GL_TRIANGLES)
    glVertex2f(1007,400)
    glVertex2f(1007,500)
    glVertex2f(1107,500)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(1007,400)
    glVertex2f(1107,500)
    glVertex2f(1107,400)
    glEnd()
    
#window line
    #left
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(750,400)
    glVertex2f(750,500)
    glVertex2f(700,450)
    glVertex2f(800,450)
    glEnd()

    #right
    glBegin(GL_LINES)
    glVertex2f(1057,400)
    glVertex2f(1057,500 )
    glVertex2f(1007,450)
    glVertex2f(1107,450)
    glEnd()

def tree():
 
    glBegin(GL_TRIANGLES)
    left_x = 0
    right_x = 100

    for _ in range(18):
        glColor3f(0.098, 0.522, 0.024)
        glVertex2f(left_x,500)
        glVertex2f(right_x,500)
        glColor3f(0.376, 0.941, 0.282)
        glVertex2f((left_x+right_x)/2,700)
        left_x = right_x
        right_x+=100
    glEnd()
       
# Raindrop 
def rain_drop(angle):
    global drop_positions, drop_val 
    glColor3f(0.0, 0.7, 1.0)
    glLineWidth(2)
    glBegin(GL_LINES)

    rad = math.radians(angle)

    for j in range(1000):
        x1 = drop_positions[j]
        y1 = drop_val[j]
        x2 = x1 + (20*math.sin(rad)) # transformed x2, y2
        y2 = y1 + (20*math.cos(rad))

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

        # Update the y-coordinate for the next frame
        drop_val[j] -= speed
        if drop_val[j] <= 0:
            drop_val[j] = random.randint(700, 1000) # Reset with random y-coordinate

    glEnd()
    glutPostRedisplay()



def create_raindrop():
    global drop_positions, drop_val
    for _ in range(1000):
        drop_positions.append(random.randint(0, 1800))
        drop_val.append(random.randint(450, 1000))

#keyboard stuff
def keyboard_listener(key, x, y):
    global angle, light_dark_intensity
    if key == GLUT_KEY_LEFT and angle < 50:
            angle += 5 
    if key == GLUT_KEY_RIGHT and angle > -50:
            angle -= 5 
    if key == GLUT_KEY_UP:
        light_dark_intensity += 0.01
        if light_dark_intensity > 1.0:
            light_dark_intensity = 1.0
    if key == GLUT_KEY_DOWN:
        light_dark_intensity -= 0.01
        if light_dark_intensity < 0.0:
            light_dark_intensity = 0.0

    glutPostRedisplay()
    
def iterate():
    glViewport(0,0,1800,1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1800, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global light_dark_intensity
    glClearColor(light_dark_intensity,light_dark_intensity,light_dark_intensity,1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 3.0) 
    ground()
    tree()
    house()
    rain_drop(angle)
    glutSwapBuffers()

def main():
    create_raindrop() # Creating randops at random position
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1800,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"Rain Simulation")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(keyboard_listener)
    glutMainLoop()
    return 0


if __name__ == "__main__":
    main()

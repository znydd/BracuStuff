from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

light_dark_intensity = 0.0
speed = 5
drop_positions = []
drop_val = []
angle = 0
rain_drop_len = 20

w_width = 1800
w_height = 1000

def ground():
    glColor3f(0.60, 0.45, 0.10)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(0, w_height * 0.7)
    glVertex2f(w_width, w_height * 0.7)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(w_width, w_height * 0.7)
    glVertex2f(w_width, 0)
    glEnd()

def house():
    # House white box
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.33, w_height * 0.3)
    glVertex2f(w_width * 0.33, w_height * 0.6)
    glVertex2f(w_width * 0.67, w_height * 0.6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.67, w_height * 0.6)
    glVertex2f(w_width * 0.33, w_height * 0.3)
    glVertex2f(w_width * 0.67, w_height * 0.3)
    glEnd()

    # Roof
    glColor3f(0.62, 0.12, 0.94)
    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.5, w_height * 0.76)
    glVertex2f(w_width * 0.31, w_height * 0.6)
    glVertex2f(w_width * 0.69, w_height * 0.6)
    glEnd()

    # Door
    glColor3f(0.196, 0.616, 0.969)
    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.45, w_height * 0.3)
    glVertex2f(w_width * 0.45, w_height * 0.52)
    glVertex2f(w_width * 0.53, w_height * 0.52)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.45, w_height * 0.3)
    glVertex2f(w_width * 0.53, w_height * 0.3)
    glVertex2f(w_width * 0.53, w_height * 0.52)
    glEnd()

    # Door knob
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(w_width * 0.51, w_height * 0.4)
    glEnd()

    # Windows
    # Left
    glColor3f(0.196, 0.616, 0.969)
    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.38, w_height * 0.4)
    glVertex2f(w_width * 0.38, w_height * 0.5)
    glVertex2f(w_width * 0.44, w_height * 0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.38, w_height * 0.4)
    glVertex2f(w_width * 0.44, w_height * 0.5)
    glVertex2f(w_width * 0.44, w_height * 0.4)
    glEnd()

    # Right
    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.56, w_height * 0.4)
    glVertex2f(w_width * 0.56, w_height * 0.5)
    glVertex2f(w_width * 0.62, w_height * 0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(w_width * 0.56, w_height * 0.4)
    glVertex2f(w_width * 0.62, w_height * 0.5)
    glVertex2f(w_width * 0.62, w_height * 0.4)
    glEnd()

    # Window lines
    # Left
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(w_width * 0.41, w_height * 0.4)
    glVertex2f(w_width * 0.41, w_height * 0.5)
    glVertex2f(w_width * 0.38, w_height * 0.45)
    glVertex2f(w_width * 0.44, w_height * 0.45)
    glEnd()

    # Right
    glBegin(GL_LINES)
    glVertex2f(w_width * 0.59, w_height * 0.4)
    glVertex2f(w_width * 0.59, w_height * 0.5)
    glVertex2f(w_width * 0.56, w_height * 0.45)
    glVertex2f(w_width * 0.62, w_height * 0.45)
    glEnd()


def tree():

    glBegin(GL_TRIANGLES)
    left_x = 0
    right_x = w_width * 0.055

    for _ in range(18):
        glColor3f(0.098, 0.522, 0.024)
        glVertex2f(left_x, w_height * 0.5)
        glVertex2f(right_x, w_height * 0.5)
        glColor3f(0.376, 0.941, 0.282)
        glVertex2f((left_x + right_x) / 2, w_height * 0.7)
        left_x = right_x
        right_x += w_width * 0.055
    glEnd()

def rain_drop(angle):
    global drop_positions, drop_val, rain_drop_len
    glColor3f(0.0, 0.7, 1.0)
    glLineWidth(2)
    glBegin(GL_LINES)

    rad = math.radians(angle)

    for j in range(1000):
        x1 = drop_positions[j]
        y1 = drop_val[j]

        # Transformed x2 and y2 for angle
        x2 = x1 + (rain_drop_len * math.sin(rad))
        y2 = y1 + (rain_drop_len * math.cos(rad))

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

        drop_val[j] -= speed # Updating the y-cord for the next frame
        if drop_val[j] <= 0:
            drop_val[j] = random.randint(int(w_height * 0.7), w_height)
    glEnd()
    glutPostRedisplay()

def create_raindrop():
    global drop_positions, drop_val
    for _ in range(1000):
        drop_positions.append(random.randint(0, w_width))
        drop_val.append(random.randint(int(w_height * 0.45), w_height))

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

# Putting iterate()'s stuff inside reshape()
def reshape(width, height): # Using glutReshapeFunc() for responsive content according to window size
    global w_width, w_height
    w_width = width
    w_height = height
    glViewport(0, 0, w_width, w_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w_width, 0.0, w_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global light_dark_intensity
    glClearColor(light_dark_intensity, light_dark_intensity, light_dark_intensity, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    ground()
    tree()
    house()
    rain_drop(angle)
    glutSwapBuffers()

def main():
    create_raindrop() # Creating randops at random position
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w_width, w_height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Rain Simulation")
    glutDisplayFunc(showScreen)
    glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard_listener)
    glutMainLoop()
    return 0

if __name__ == "__main__":
    main()
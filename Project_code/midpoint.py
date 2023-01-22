import OpenGL.GL as gl
from OpenGL.GLU import *
from math import radians as rad
from math import sin, cos

WIDTH = 1600
HEIGHT = 1000
def addPixel(a,b):
    gl.glVertex2f( (a-(WIDTH/2))/(WIDTH/2)  , -1 * (b-(HEIGHT/2))/(HEIGHT/2)   )

def findZone(x1,y1,x2,y2):
  if x2 - x1 == 0:
    m = (y2-y1)*float('inf')
  else:
    m = (y2-y1)/(x2-x1)
  if 0 <= m < 1:
    if x2 > x1:
      return 0
    else:
      return 4
  elif m > 1:
    if y2 > y1:
      return 1
    else: 
      return 5
  elif m < -1:
    if y2 > y1:
      return 2
    else:
      return 6
  else:
    if x2 > x1:
      return 7
    else:
      return 3

def to_zero_from_zone(zone,x1, y1, x2, y2):
    if zone == 0:
        return x1 , y1 , x2 , y2
    elif zone == 1:
        return y1 , x1 , y2 , x2
    elif zone == 2:
        return y1 , -1*x1 , y2 , -1*x2
    elif zone == 3:
        return -1*x1 , y1 , -1*x2 , y2
    elif zone == 4:
        return -1*x1 , -1*y1 , -1*x2 , -1*y2
    elif zone == 5:
        return -1*y1 , -1*x1 , -1*y2 , -1*x2
    elif zone == 6:
        return -1*y1 , x1 , -1*y2 , x2
    elif zone == 7:
        return x1 , -1*y1 , x2 , -1*y2

def from_zero_to(zone, x, y):
    if zone == 0:
        return x , y
    elif zone == 1:
        return y , x
    elif zone == 2:
        return -1*y , x
    elif zone == 3:
        return -1*x , y
    elif zone == 4:
        return -1*x , -1*y
    elif zone == 5:
        return -1*y , -1*x
    elif zone == 6:
        return y , -1*x
    elif zone == 7:
        return x , -1*y

def DrawLine(x1,y1,x2,y2):
  gl.glBegin(gl.GL_POINTS)
  zone = findZone(x1,y1,x2,y2)
  x1,y1,x2,y2 = to_zero_from_zone(zone, x1, y1, x2, y2)
  dx = x2 - x1
  dy = y2 - y1
  d = 2*dy-dx
  delE = 2*dy
  delNE = 2*(dy-dx)
  y = y1
  for x in range(x1, x2+1):
    nx, ny = from_zero_to(zone,x,y)
    addPixel(nx,ny)
    if d > 0: # NE
      d = d + delNE
      y = y + 1
    else: # E
      d = d + delE
  gl.glEnd()

def draw_score(score, x,y,s, color = (0,0,0)):
  gl.glColor3f(color[0],color[1],color[2])
  gl.glPointSize(5)
  score = str(score)
  shifter = 0
  for i in score:
    if i == '1':
      DrawLine(x+s,y,x+s,y+s)       #BottomRight |
      DrawLine(x+s,y+s,x+s,y+2*s)        #TopRight |
    elif i == '2':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x+s,y,x+s,y+s)        #TopRight |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x,y+2*s,x,y+s)     #LeftBottom |
      DrawLine(x+s,y+2*s,x,y+2*s)    #Bottom -
    elif i == '3':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x+s,y,x+s,y+s)        #TopRight |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y+2*s,x+s,y+s)    #BottomRight |
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom -
    elif i == '4':
      DrawLine(x,y,x,y+s)       #Left |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y,x+s,y+2*s)        #TopRight |
    elif i == '5':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x,y,x,y+s)       #Left |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y+2*s,x+s,y+s)    #BottomRight |
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom -
    elif i == '6':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x,y,x,y+s)       #Left |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y+2*s,x+s,y+s)
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom -
      DrawLine(x+s,y+2*s,x+s,y+s)    #BottomRight |
    elif i == '7':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x+s,y,x+s,y+2*s)        #TopRight |
    elif i == '8':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x,y,x,y+2*s)       #Left |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y,x+s,y+2*s)        #TopRight |
      DrawLine(x+s,y+2*s,x+s,y+s)    #BottomRight |
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom -
    elif i == '9':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x,y,x,y+s)       #Left |
      DrawLine(x,y+s,x+s,y+s)        #Middle -
      DrawLine(x+s,y,x+s,y+2*s)        #TopRight |
      DrawLine(x+s,y+2*s,x+s,y+s)    #BottomRight |
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom -
    elif i == '0':
      DrawLine(x,y,x+s,y)      #Top -
      DrawLine(x,y,x,y+2*s)       #Left |
      DrawLine(x,y+2*s,x+s,y+2*s)    #Bottom - 
      DrawLine(x+s,y,x+s,y+2*s)        #TopRight |
    
    x += 2*s

def eightway_symetry(x, y, a, b):
    addPixel(x + a, y + b)
    addPixel(y + a, x + b)
    addPixel(y + a, -x + b)
    addPixel(x + a, -y + b)
    addPixel(-x + a, -y + b)
    addPixel(-y + a, -x + b)
    addPixel(-y + a, x + b)
    addPixel(-x + a, y + b)

def Draw_circle(radius,centerX = 0, centerY = 0):
    gl.glBegin(gl.GL_POINTS)
    x = 0
    y = radius
    d = 1 - radius
    while x <= y:
        eightway_symetry(x,y,centerX,centerY)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    gl.glEnd()


def pattern(n = 8, r = 200, centerX = 0, centerY = 0, theta = 0):
    Draw_circle(r,centerX, centerY)
    del_theta = 360/n
    small_r = r//2
    for i in range(n):
      newCenterX = small_r*cos(rad(theta))
      newCenterY = small_r*sin(rad(theta))
      Draw_circle(small_r,newCenterX + centerX, newCenterY + centerY)
      theta += del_theta


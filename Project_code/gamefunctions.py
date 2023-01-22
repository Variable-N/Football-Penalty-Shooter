from midpoint import *
import numpy as np
import math
def background():
    # Draw the background
    #Grass
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0, .61, .098)
    addPixel(0,562)
    addPixel(1600,562)
    addPixel(1600,1000)
    addPixel(0,1000)
    gl.glEnd()
    #AKASH
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0.53, .807, .921)
    addPixel(0,562)
    addPixel(1600,562)
    addPixel(1600,0)
    addPixel(0,0)
    gl.glEnd()


def goalPost():
    #NET
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0.8, .95, 1)
    addPixel(350,562)
    addPixel(400,562)
    addPixel(400,300)
    addPixel(350,262)
    gl.glEnd()
    gl.glBegin(gl.GL_QUADS)
    addPixel(1250,562)
    addPixel(1200,562)
    addPixel(1200,300)
    addPixel(1250,262)
    gl.glEnd()
    gl.glBegin(gl.GL_QUADS)
    addPixel(1200,300)
    addPixel(400,300)
    addPixel(350,262)
    addPixel(1250,262)
    gl.glEnd()
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0.58, .857, .951)
    addPixel(1200,300)
    addPixel(400,300)
    addPixel(400,562)
    addPixel(1200,562)
    gl.glEnd()
    
    
    #Goal Post
    gl.glPointSize(15)
    gl.glColor3f(1, 1, 1)   #562 GROUND
    DrawLine(350,562,350,262)
    DrawLine(350,262,1250,262)
    DrawLine(1250,262,1250,562)
    gl.glPointSize(9)
    DrawLine(350,262,400,300)
    DrawLine(1250,262,1200,300)
    gl.glPointSize(7)
    DrawLine(1200,300,400,300)
    gl.glPointSize(7)
    DrawLine(1200,300,1200,559)
    DrawLine(400,300,400,559)
    
    #Court
    gl.glPointSize(5)
    gl.glColor3f(0.9, 1, 0.8)   #562 GROUND
    DrawLine(250,562, 100, 700)
    DrawLine(1350,562, 1500, 700)
    DrawLine( 100, 700, 1500, 700)

class Ball:
    def __init__(self):
        self.x = 800
        self.y = 900
        self.radius = 35
        self.theta = 60
    
    def DrawBall(self):
        gl.glPointSize(2)
        gl.glColor3f(1, 1, 1)
        for r in range(1,round(self.radius),2):
            Draw_circle(r, self.x, self.y)
        gl.glColor3f(0, 0, 0)
        pattern(5, round(self.radius), self.x, self.y, self.theta)

    def Ball_up(self):
        if self.y > 30:
            self.y -= 10
            self.radius -= 0.25
            self.DrawBall()
    
    def Ball_down(self):
        if self.y < 970:
            self.y += 10
            self.radius += 0.25
            self.DrawBall()
    
    def Ball_left(self,e = 10):
        if self.x > 30:
            self.x -= e
            self.theta -= 15
            self.DrawBall()
    
    def Ball_right(self, e = 10):
        if self.x < 1570:
            self.x += e
            self.theta += 15
            self.DrawBall()
    
    
        

class GoalKeeper():
    def __init__(self, x = 800, y = 467, team = "BRA"):
        self.x = x
        self.y = y
        self.t = 0
        self.team = team
        if self.team == "BRA":
            self.bodyC = (1,1,0)
            self.legC = (0,0,1)
        elif self.team == "ARG":
            self.bodyC = (100/255, 150/255, 255/255)
            self.legC = (1,1,1)
        elif self.team == "FRN":
            self.bodyC = (7/255, 42/255, 108/255)
            self.legC = (170/255, 74/255, 68/255)
        elif self.team == "GER":
            self.bodyC = (1,1,1)
            self.legC = (0,0,0)
        elif self.team == "SPA":
            self.bodyC = (170/255, 74/255, 68/255)
            self.legC = (7/255, 42/255, 108/255)
        elif self.team == "POR":
            self.bodyC = (238/255, 75/255, 43/255)
            self.legC = (9/255,46/255,32/255)
        elif self.team == "NET":
            self.bodyC = (255/255, 191/255, 0/55)
            self.legC = (242/255, 210/255, 189/255)
        elif self.team == "CRO":
            self.bodyC = (170/255, 74/255, 68/255)
            self.legC = (1,1,1)
        elif self.team == "MOR":
            self.bodyC = (136/255, 8/255, 8/255)
            self.legC = (0,1,0)

        self.head = (self.x, self.y-68)
        self.hand11 = (self.x -29, self.y-30)
        self.hand12 = (self.x -50, self.y+30)
        self.hand21 = (self.x +29, self.y-30)
        self.hand22 = (self.x +50, self.y+30)
        self.body1 = (self.x-30, self.y-36)
        self.body2 = (self.x+30, self.y-36)
        self.body3 = (self.x+30, self.y+30)
        self.body4 = (self.x-30, self.y+30)
        self.leg1 = (self.x-20, self.y+30)
        self.leg2 = (self.x+20, self.y+30)
        self.leg3 = (self.x+20, self.y+97)
        self.leg4 = (self.x-20, self.y+97)
    
    def reset(self):
        self.x = 800
        self.y = 467
        self.t = 0
        self.head = (self.x, self.y-68)
        self.hand11 = (self.x -29, self.y-30)
        self.hand12 = (self.x -50, self.y+30)
        self.hand21 = (self.x +29, self.y-30)
        self.hand22 = (self.x +50, self.y+30)
        self.body1 = (self.x-30, self.y-36)
        self.body2 = (self.x+30, self.y-36)
        self.body3 = (self.x+30, self.y+30)
        self.body4 = (self.x-30, self.y+30)
        self.leg1 = (self.x-20, self.y+30)
        self.leg2 = (self.x+20, self.y+30)
        self.leg3 = (self.x+20, self.y+97)
        self.leg4 = (self.x-20, self.y+97)
    
    def Draw(self):
        #Head
        gl.glPointSize(7)
        gl.glColor3f(0.776,0.525,0.259)
        for r in range(0,30,7):
            Draw_circle(r, int(self.head[0]),int(self.head[1]))
        #Hand
        gl.glColor3f(0.776,0.525,0.259)
        DrawLine(int(self.hand11[0]), int(self.hand11[1]), int(self.hand12[0]), int(self.hand12[1]))
        DrawLine(int(self.hand21[0]), int(self.hand21[1]), int(self.hand22[0]), int(self.hand22[1]))
        #Body
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3f(self.bodyC[0],self.bodyC[1],self.bodyC[2])
        addPixel(int(self.body1[0]), int(self.body1[1]))
        addPixel(int(self.body2[0]), int(self.body2[1]))
        addPixel(int(self.body3[0]), int(self.body3[1]))
        addPixel(int(self.body4[0]), int(self.body4[1]))
        gl.glEnd()
        #Leg
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3f(self.legC[0],self.legC[1],self.legC[2])
        addPixel(int(self.leg1[0]), int(self.leg1[1]))
        addPixel(int(self.leg2[0]), int(self.leg2[1]))
        addPixel(int(self.leg3[0]), int(self.leg3[1]))
        addPixel(int(self.leg4[0]), int(self.leg4[1]))
        gl.glEnd()
    
    def rotate(self,t):
        if self.t+t < 90 and self.t+t > -90:
            self.t += t
            a = math.cos(math.radians(t))
            b = math.sin(math.radians(t)) 

            r = np.array([[a, -b, 0],
                        [b, a, 0],
                        [0, 0, 1]])
            self.head = np.matmul(r, np.array([self.head[0] - self.x, self.head[1] - self.y, 1]))
            self.hand11 = np.matmul(r, np.array([self.hand11[0] - self.x, self.hand11[1] - self.y, 1]))
            self.hand12 = np.matmul(r, np.array([self.hand12[0] - self.x, self.hand12[1] - self.y, 1]))
            self.hand21 = np.matmul(r, np.array([self.hand21[0] - self.x, self.hand21[1] - self.y, 1]))
            self.hand22 = np.matmul(r, np.array([self.hand22[0] - self.x, self.hand22[1] - self.y, 1]))
            self.body1 = np.matmul(r, np.array([self.body1[0] - self.x, self.body1[1] - self.y, 1]))
            self.body2 = np.matmul(r, np.array([self.body2[0] - self.x, self.body2[1] - self.y, 1]))
            self.body3 = np.matmul(r, np.array([self.body3[0] - self.x, self.body3[1] - self.y, 1]))
            self.body4 = np.matmul(r, np.array([self.body4[0] - self.x, self.body4[1] - self.y, 1]))
            self.leg1 = np.matmul(r, np.array([self.leg1[0] - self.x, self.leg1[1] - self.y, 1]))
            self.leg2 = np.matmul(r, np.array([self.leg2[0] - self.x, self.leg2[1] - self.y, 1]))
            self.leg3 = np.matmul(r, np.array([self.leg3[0] - self.x, self.leg3[1] - self.y, 1]))
            self.leg4 = np.matmul(r, np.array([self.leg4[0] - self.x, self.leg4[1] - self.y, 1]))
            
            self.head = (self.head[0] + self.x, self.head[1] + self.y)
            self.hand11 = ((self.hand11[0] + self.x), (self.hand11[1] + self.y))
            self.hand12 = ((self.hand12[0] +self.x), (self.hand12[1] +self.y))
            self.hand21 = ((self.hand21[0] + self.x), (self.hand21[1] +self.y))
            self.hand22 = ((self.hand22[0] + self.x), (self.hand22[1] +self.y))
            self.body1 = ((self.body1[0] + self.x), (self.body1[1] +self.y))
            self.body2 = ((self.body2[0] + self.x), (self.body2[1] +self.y))
            self.body3 = ((self.body3[0] + self.x), (self.body3[1] +self.y))
            self.body4 = ((self.body4[0] + self.x), (self.body4[1] +self.y))
            self.leg1 = ((self.leg1[0] + self.x), (self.leg1[1] +self.y))
            self.leg2 = ((self.leg2[0] + self.x), (self.leg2[1] +self.y))
            self.leg3 = ((self.leg3[0] + self.x), (self.leg3[1] +self.y))
            self.leg4 = ((self.leg4[0] + self.x), (self.leg4[1] +self.y))
            self.Draw()

    def moveLeft(self, speed = 5):
        if self.x - speed > 300:
            self.x -= speed
            self.head = (self.head[0] - 5, self.head[1])
            self.hand11 = (self.hand11[0] - 5, self.hand11[1])
            self.hand12 = (self.hand12[0] - 5, self.hand12[1])
            self.hand21 = (self.hand21[0] - 5, self.hand21[1])
            self.hand22 = (self.hand22[0] - 5, self.hand22[1])
            self.body1 = (self.body1[0] - 5, self.body1[1])
            self.body2 = (self.body2[0] - 5, self.body2[1])
            self.body3 = (self.body3[0] - 5, self.body3[1])
            self.body4 = (self.body4[0] - 5, self.body4[1])
            self.leg1 = (self.leg1[0] - 5, self.leg1[1])
            self.leg2 = (self.leg2[0] - 5, self.leg2[1])
            self.leg3 = (self.leg3[0] - 5, self.leg3[1])
            self.leg4 = (self.leg4[0] - 5, self.leg4[1])
            self.Draw()
    
    def moveRight(self, speed = 5):
        if self.x + speed < 1300:
            self.x += speed
            self.head = (self.head[0] + 5, self.head[1])
            self.hand11 = (self.hand11[0] + 5, self.hand11[1])
            self.hand12 = (self.hand12[0] + 5, self.hand12[1])
            self.hand21 = (self.hand21[0] + 5, self.hand21[1])
            self.hand22 = (self.hand22[0] + 5, self.hand22[1])
            self.body1 = (self.body1[0] + 5, self.body1[1])
            self.body2 = (self.body2[0] + 5, self.body2[1])
            self.body3 = (self.body3[0] + 5, self.body3[1])
            self.body4 = (self.body4[0] + 5, self.body4[1])
            self.leg1 = (self.leg1[0] + 5, self.leg1[1])
            self.leg2 = (self.leg2[0] + 5, self.leg2[1])
            self.leg3 = (self.leg3[0] + 5, self.leg3[1])
            self.leg4 = (self.leg4[0] + 5, self.leg4[1])
            self.Draw()

    def moveUp(self, speed = 5):
        if self.y - speed > 380:
            self.y -= speed
            self.head = (self.head[0], self.head[1] - 5)
            self.hand11 = (self.hand11[0], self.hand11[1] - 5)
            self.hand12 = (self.hand12[0], self.hand12[1] - 5)
            self.hand21 = (self.hand21[0], self.hand21[1] - 5)
            self.hand22 = (self.hand22[0], self.hand22[1] - 5)
            self.body1 = (self.body1[0], self.body1[1] - 5)
            self.body2 = (self.body2[0], self.body2[1] - 5)
            self.body3 = (self.body3[0], self.body3[1] - 5)
            self.body4 = (self.body4[0], self.body4[1] - 5)
            self.leg1 = (self.leg1[0], self.leg1[1] - 5)
            self.leg2 = (self.leg2[0], self.leg2[1] - 5)
            self.leg3 = (self.leg3[0], self.leg3[1] - 5)
            self.leg4 = (self.leg4[0], self.leg4[1] - 5)
            self.Draw()

    def moveDown(self, speed = 5):
        if self.y + speed < 500:
            self.y += speed
            self.head = (self.head[0], self.head[1] + 5)
            self.hand11 = (self.hand11[0], self.hand11[1] + 5)
            self.hand12 = (self.hand12[0], self.hand12[1] + 5)
            self.hand21 = (self.hand21[0], self.hand21[1] + 5)
            self.hand22 = (self.hand22[0], self.hand22[1] + 5)
            self.body1 = (self.body1[0], self.body1[1] + 5)
            self.body2 = (self.body2[0], self.body2[1] + 5)
            self.body3 = (self.body3[0], self.body3[1] + 5)
            self.body4 = (self.body4[0], self.body4[1] + 5)
            self.leg1 = (self.leg1[0], self.leg1[1] + 5)
            self.leg2 = (self.leg2[0], self.leg2[1] + 5)
            self.leg3 = (self.leg3[0], self.leg3[1] + 5)
            self.leg4 = (self.leg4[0], self.leg4[1] + 5)
            self.Draw()

    
    def LeftDive(self):
        for _ in range(15):
            self.moveLeft()
            self.moveLeft()
            if self.t >-87:
                self.rotate(-5)
        self.moveDown(0.2)
    
    def RightDive(self):
        for _ in range(15):
            self.moveRight()
            self.moveRight()
            if self.t <87:
                self.rotate(5)
        self.moveDown(0.2)

    def collision(self,x,y):
        if self.x - 70 < x < self.x + 70 and self.y - 100 < y < self.y + 60:
            print("collision")
            return True
        else:
            return False
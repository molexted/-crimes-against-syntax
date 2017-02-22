from tkinter import *
from random import randint

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("ge]am")
        self.width = 600
        self.height = 600
        height = self.height
        width = self.width
        self.canvas =Canvas(window, bg = "white", width = self.width, height = self.height      )
        self.canvas.pack()
        frame = Frame(window)
        self.x = 0
        self.y = 0
        self.dy = 0
        self.dx = 3
        self.mx = width
        self.my = height-35
        self.mdy = 0
        self.mdx = -4.5
        self.sleepTime = 25#animation delay     
        self.canvas.create_text(self.x, 520, text = "  0  ", tags = "text")
        self.canvas.create_text(self.x, 530, text = "./|\.", tags = "text2")
        self.canvas.create_text(self.x, 540, text = " / \ ", tags = "text3")
        self.canvas.create_text(self.x, 572, text = "x"*600, tags = "text4")
        frame.bind("<Up>", self.faster)#binds ^ to function
        frame.bind('<Down>', self.slower)#"              "
        frame.bind('<space>', self.jump)#" 
        frame.focus_set()
        frame.pack()
        while True:
            self.animate()
            self.conditionals()
            self.enemies()
            self.loser()
            
        window.mainloop()
    def faster(self, event):#doubles speed
        self.dx = self.dx * 2
        print("Speeding up to", self.dx)
    def slower(self, event):#halves speed
        self.dx = self.dx / 2
        print("Slowing down to", self.dx)
    def jump(self, event):#halves speed
        self.dy = -3
        self.canvas.move("text", 0, self.dy)
        self.canvas.move("text2", 0, self.dy)
        self.canvas.move("text3", 0, self.dy)
        self.y=self.dy+self.y
        print("Jumping", self.dy)
    def animate(self):#moves ASCII art according to self.dx
            self.canvas.move("text", self.dx, self.dy)
            self.canvas.move("text2", self.dx, self.dy)
            self.canvas.move("text3", self.dx, self.dy)
            #print("moving")
            self.canvas.after(self.sleepTime)
            self.canvas.update()
    def conditionals(self):
            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0       
                self.y = 0
                self.canvas.delete("text")
                self.canvas.delete("text2")
                self.canvas.delete("text3")
                self.canvas.create_text(self.x, 520, text = "  0  ", tags = "text")
                self.canvas.create_text(self.x, 530, text = "./|\.", tags = "text2")
                self.canvas.create_text(self.x, 540, text = " / \ ", tags = "text3")
            if self.y>=17:
                self.dy=0 
                self.y=17                   
                #print("stopping")
            else:
                self.dy= self.dy+0.2
                self.y += self.dy
                #print("not stopping")
    def enemies(self): 
        self.canvas.create_text(self.mx, self.my, text = " 0 ", tags = "mob")
        self.canvas.move("mob", self.mdx, self.mdy)
        self.mx=self.mdx+self.mx
        self.my=self.mdy+self.my
        self.canvas.after(self.sleepTime)
        self.canvas.update()
        if self.mx < 0:
            self.canvas.delete("mob")
            print("Done here")
            self.mx=self.width  
            
        else:
            #print("Done here")
            False
    def loser(self):
        if (self.mx - self.x <= 50)== True & (self.my - self.y <=50)==True:
            print("loser")
            quit
ControlAnimation()
#EOF

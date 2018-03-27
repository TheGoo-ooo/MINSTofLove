# noinspection PyInterpreter
import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import pygame, random
import cv2


class MainWindow():
    def __init__(self, window):
        # create all of the main containers
        self.top_frame = Frame(window, bg='gray', width=450, height=50, pady=3)
        self.center = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
        self.btm_frame = Frame(window, bg='white', width=450, height=60, pady=0)
        
        
        # layout all of the main containers
        window.grid_rowconfigure(1, weight=1)
        window.grid_columnconfigure(0, weight=1)
        
        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=1, sticky="nsew")
        self.btm_frame.grid(row=2, sticky="ew")
        
        
        # create the center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(0, weight=1)
        
        self.ctr_left = Canvas(self.center, width=370, height=300)
        self.ctr_left.grid(row=0, column=0, sticky="ns")
        
        self.ctr_right = Canvas(self.center, width=370, height=300, bg='white')
        self.ctr_right.grid(row=0, column=2, sticky="ns")
        
        self.lblRight = Label(self.btm_frame, text="MASTER \n HAHA")
        self.lblRight.grid(row=0, column=0, sticky="nsew")
        
        # create the widgets for the top frame
        self.btn_import = Button(self.top_frame, text="From picture", command=self.open)
        self.btn_draw = Button(self.top_frame, text="From draw", command=self.draw)
        self.btn_work = Button(self.top_frame, text="Work", command=self.work)
        
        
        # layout the widgets in the top frame
        self.btn_import.grid(row=1, column=2, padx=3)
        self.btn_draw.grid(row=1, column=3, padx=3)
        self.btn_work.grid(row=1, column=4, padx=3)
        
        
    def work(self):
        print("hehe")
        
    
    # Pygame window
    def draw(self):
        (width, height) = (280, 280)
        screen = pygame.display.set_mode((width, height))
        screen.fill((0, 0, 0))
        draw_on = False
        last_pos = (0, 0)
        color=(255, 255, 255)
        radius = 6
        try:
            while True:
                e = pygame.event.wait()
                if e.type == pygame.QUIT:
                    raise StopIteration
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                if e.type == pygame.MOUSEBUTTONUP:
                    draw_on = False
                if e.type == pygame.MOUSEMOTION:
                    if draw_on:
                        pygame.draw.circle(screen, color, e.pos, radius)
                        self.roundline(screen, color, e.pos, last_pos,  radius)
                    last_pos = e.pos
                if e.type == pygame.KEYDOWN:
                    if e.key==pygame.K_ESCAPE:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                    if e.key==pygame.K_SPACE:
                        pygame.image.save(screen, "imgTest.png")
                        self.filename="imgTest.png"
                        self.displayPicture()
                        raise StopIteration
                pygame.display.flip()
        
        except StopIteration:
            pass
        pygame.quit()
        
    
    # For drawing line
    def roundline(self, srf, color, start, end, radius=1):
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            pygame.draw.circle(srf, color, (x, y), radius)
        
    
    # Open a picture and get filename
    def open(self):
        self.filename = tk.filedialog.askopenfilename(title="Open a picture", filetypes=[('png files', '.png'),('all files','.*')])
        self.displayPicture()
        
     
    # Display picture on the canvas
    def displayPicture(self):
        self.img = Image.open(self.filename)
        self.img = self.img.resize((350, 350), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(self.img)
        self.ctr_left.create_image(self.ctr_left.winfo_width()/2, self.ctr_left.winfo_width()/2, image=self.pic, anchor=CENTER)

        

root = Tk()
root.title('Traitement Image')
root.geometry("750x550")
root.resizable(False, False)
MainWindow(root)
root.mainloop()
# -*- coding: utf-8 -*-
"""
@author: GriesserGA
"""
import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import pygame, random
import cv2
import TI_Knn_Mnist_Digits as TI
import preprocessing as Prep
import os, os.path
import use_dnn as dnn


class MainWindow():
    def __init__(self, window):
        
        self.result = StringVar()
        self.result.set("Result here : ")
        
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
        
        self.ctr_right = Canvas(self.center, width=370, height=300)
        self.ctr_right.grid(row=0, column=2, sticky="ns")
        
        self.lblRight = Label(self.btm_frame, textvariable=self.result)
        self.lblRight.config(font=("Arial", 20))
        self.lblRight.grid(row=0, column=0, sticky="nsew")
        
        # create the widgets for the top frame
        self.btn_import = Button(self.top_frame, text="From picture", command=self.open)
        self.btn_draw = Button(self.top_frame, text="From draw", command=self.draw)
        self.btn_work = Button(self.top_frame, text="Work Fasmy", command=self.workFasmy)
        self.btn_work2 = Button(self.top_frame, text="Work Julien", command=self.workJulien)

        
        
        # layout the widgets in the top frame
        self.btn_import.grid(row=1, column=2, padx=3)
        self.btn_draw.grid(row=1, column=3, padx=3)
        self.btn_work.grid(row=1, column=4, padx=3)
        self.btn_work2.grid(row=1, column=6, padx=3)
        
        self.saveFilenameRes = ''
        self.dirPrep =  "./ressources/prep"
        self.dirKnn = "./ressources/knn"
        
    #Delete repository files
    def cleanRepository(self):
        for file in os.listdir(self.dirPrep):
            if file.endswith(".png"):
                os.remove(self.dirPrep + '/' + file)

        for file in os.listdir(self.dirKnn):
            if file.endswith(".png"):
                os.remove(self.dirKnn + '/' + file)

    #Use preprocessing algo to prepare img
    def prepFiles(self, type):
        self.cleanRepository()

        tabFiles = []
        Prep.preprocess(self.saveFilename, type)
        for file in os.listdir(self.dirPrep):
            if file.endswith(".png"):
                tabFiles.append(self.dirPrep + '/' + file)
                
        return tabFiles
            
        
    def workFasmy(self):
        tabFiles = self.prepFiles('FASMY')
    
        for f in tabFiles:
            print("HAHA" + f)
            #self.result.set("Your number is " + dnn.predict(f))
        

    def workJulien(self):
        tabFiles = self.prepFiles('JULIEN')
        tabRes = []
        strRes = ''
        for f in tabFiles:
            res = TI.KNNDigits(f)
            tabRes.append(str(res))
        for i in tabRes:
            strRes += i
        
        self.result.set("Your number is " + strRes)
        #self.displayPictureRight()                
    
    
    # Pygame window
    def draw(self):
        (width, height) = (280, 280)
        screen = pygame.display.set_mode((width, height))
        screen.fill((255, 255, 255))
        draw_on = False
        last_pos = (0, 0)
        color=(0, 0, 0)
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
                        screen.fill((255, 255, 255))
                        pygame.display.update()
                    if e.key==pygame.K_SPACE:
                        pygame.image.save(screen, "ressources/imgDraw.png")
                        self.saveFilename="ressources/imgDraw.png"
                        self.displayPictureLeft()
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
        
    
    # Open a picture and get saveFilename
    def open(self):
        self.saveFilename = tk.filedialog.askopenfilename(title="Open a picture", filetypes=[('png files', '.png'),('all files','.*')])
        self.displayPictureLeft()
        
     
    # Display picture on the canvas
    def displayPictureLeft(self):
        self.imgLeft = Image.open(self.saveFilename)
        self.imgLeft = self.imgLeft.resize((350, 350), Image.ANTIALIAS)
        self.picLeft = ImageTk.PhotoImage(self.imgLeft)
        self.ctr_left.create_image(self.ctr_left.winfo_width()/2, self.ctr_left.winfo_width()/2, image=self.picLeft, anchor=CENTER)

    # Display picture on the canvas
    def displayPictureRight(self):
        self.imgRight = Image.open(self.saveFilenameRes)
        self.imgRight = self.imgRight.resize((280, 280), Image.ANTIALIAS)
        self.picRight = ImageTk.PhotoImage(self.imgRight)
        self.ctr_right.create_image(self.ctr_right.winfo_width()/2, self.ctr_right.winfo_width()/2, image=self.picRight, anchor=CENTER)
        

root = Tk()
root.title('Traitement Image')
root.geometry("750x550")
root.resizable(False, False)
MainWindow(root)
root.mainloop()
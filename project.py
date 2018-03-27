# noinspection PyInterpreter
import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import pygame, random
import cv2


window = Tk()
window.title('Traitement Image')
window.geometry("750x500")
window.resizable(False, False)
#ctr_left=Canvas()


def work():
    print("hehe")
    

# Open a pygame screen for drawing
def draw():
    (width, height) = (280, 280)
    screen = pygame.display.set_mode((width, height))
    screen.fill((0, 0, 0))
    draw_on = False
    last_pos = (0, 0)
    color=(255, 255, 255)
    radius = 10
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
                    roundline(screen, color, e.pos, last_pos,  radius)
                last_pos = e.pos
            if e.type == pygame.KEYDOWN:
                if e.key==pygame.K_ESCAPE:
                    screen.fill((255, 255, 255))
                    pygame.display.update()
                if e.key==pygame.K_SPACE:
                    pygame.image.save(screen, "imgTest.png")
                    pass
            pygame.display.flip()
    
    except StopIteration:
        pass
    pygame.quit()
    

# Define draw
def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)


# Open a picture and get filename
def open():
    filename = tk.filedialog.askopenfilename(title="Open a picture", filetypes=[('png files', '.png')])
    img = Image.open(filename)
    img = img.resize((350, 350), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(img)
    ctr_left.create_image(ctr_left.winfo_width()/2, ctr_left.winfo_width()/2, image=pic, anchor=CENTER)
    tk.Update


#def main():
# create all of the main containers
top_frame = Frame(window, bg='gray', width=450, height=50, pady=3)
center = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(window, bg='white', width=450, height=45, pady=3)


# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=2, sticky="ew")


# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)

ctr_left = Canvas(center, width=370, height=350)
ctr_left.grid(row=0, column=0, sticky="ns")

ctr_right = Canvas(center, width=370, height=350, bg='white')
ctr_right.grid(row=0, column=2, sticky="ns")


# create the widgets for the top frame
btn_import = Button(top_frame, text="From picture", command=open)
btn_draw = Button(top_frame, text="From draw", command=draw)
btn_work = Button(top_frame, text="Work", command=work)


# layout the widgets in the top frame
btn_import.grid(row=1, column=2, padx=3)
btn_draw.grid(row=1, column=3, padx=3)
btn_work.grid(row=1, column=4, padx=3)


window.mainloop()

#if __name__ == '__main__':
#    main()
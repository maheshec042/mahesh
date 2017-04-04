#!/bin/env python

from Tkinter import *
import Image
import ImageTk

def markImage(im, p, bg):
    pix = im.load()
    pix[ p[0], p[1] ] = bg

def naiveZoom(im, p, zf, bg):
    out = Image.new(im.mode, im.size)
    pix = out.load()
    iw, ih = im.size
    for x in range(iw):
        for y in range(ih):
            xorg = x + zf*(p[0]+0.5-x) + zf*(1-zf)*(p[0]-iw/2)
            yorg = y + zf*(p[1]+0.5-y) + zf*(1-zf)*(p[1]-ih/2)
            if xorg >= 0 and xorg < iw and yorg >= 0 and yorg < ih:
                pix[x,y] = im.getpixel( (xorg , yorg) )
            else:
                pix[x,y] = bg
    return out

class Zoom:
    def __init__(self, parent=None):
        root = Tk()
        self.im = Image.open('C:\Users\Mahesh\Desktop\999.jpg')
        self.zf = 0.0
        self.deltazf = 0.05
        self.p = (round(0.3*self.im.size[0]), round(0.3*self.im.size[1]) )
        self.bg = 255
        markImage(self.im, self.p, self.bg)
        canvas = Canvas(root, width=self.im.size[0]+20 , height=self.im.size[1]+20)
        canvas.pack()
        root.bind('<Key>', self.Key)
        self.canvas = canvas
        self.photo = ImageTk.PhotoImage(self.im)
        self.item = self.canvas.create_image(10, 10, anchor=NW, image=self.photo)
        self.change = False
    def Key(self, event):
        if event.char == "+":
            if self.zf < 1:
                self.zf += self.deltazf
                self.change = True
        elif event.char == "-":
            if self.zf > 0:
                self.zf -= self.deltazf
                self.change = True
        if self.change:
            self.out = naiveZoom(self.im, self.p, self.zf, self.bg)
            self.photo = ImageTk.PhotoImage(self.out)   
            self.canvas.delete(self.item)
            self.change = False
        self.item = self.canvas.create_image(10, 10, anchor=NW, image=self.photo)
        print self.p, self.zf

if __name__ == "__main__":
    Zoom()
    mainloop()

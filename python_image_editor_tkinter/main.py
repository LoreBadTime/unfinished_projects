from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.ttk as tttk
from PIL import ImageTk,Image,ImageDraw

class ttk:
    Bthemes = []
    class Tk(Tk):
         theme = "default"
         def __init__(self):
            super().__init__()
            self.configure(background="#202020")
            self.style = tttk.Style(self)
            self.style.theme_use(self.theme)

            # definizione stili
            new_style = "buttonDark.TButton"
            self.style.map(new_style,
                background = [("active", "black"), ("!active", "#202020")],
                foreground = [("active", "white"), ("!active", "white")]
                )
            self.style.configure(new_style,borderwidth=0)
            ttk.Bthemes.append(new_style)

    class Button(tttk.Button):
            sizeButtonSmall = "30 30 30 30"
            def __init__(self,window,txt):
                super().__init__(window, text=txt,padding=self.sizeButtonSmall,style="buttonDark.TButton")

            


class imageWindow:
    canvas = None
    # inizializzazione dell'immagine, salvataggio immagine e finestra tkinter
    def __init__(self,window):
        self.window = window
        # controlla la funzione dopo
        self.action = -1
        self.counter = 0

    # impostazione dell'azione da svolgere (se action è a 0 -> elimina se è a 1 non elimina)
    def setPointerAction(self,action):
        self.action = action

    # caricamento di una nuova immagine nel canvas
    def loadNewImage(self,path):
        self.rawimg = Image.open(path)
        self.imgsize = (self.rawimg.size[0],self.rawimg.size[1])
        self.img = ImageTk.PhotoImage(image=self.rawimg)
        self.delete()
        return self
    def loadBlankImage(self,x,y):
        self.rawimg = Image.new('RGB', (x, y))
        self.imgsize = (x,y)
        self.img = ImageTk.PhotoImage(image=self.rawimg)
        self.delete()
        return self
    def updateRawImg(self):
        self.canvas.itemconfig(tagOrId=self.id,image = self.img)
    def drawline(self,positions):       #colore       
        self.drawimg.line(positions, (100, 100, 100), 3)
    # gestore evento di quando si clicca dentro il canvas, in base ad action si esegue un'azione
    def pointerAction(self,event):
        self.counter += 1
        if self.action == 1:
            self.predpos.append((event.x,event.y))
            # increasing this parameter increases more the performance/efficiency, but less fps
            if self.counter % 3 == 0:
                self.drawline(self.predpos)
                self.predpos = [(event.x,event.y)]
                self.relase(None)
        elif self.action == 0:
            self.delete()
        
        # tutti i casi, con event poi possiamo p
        # elif self.acrion == 1: 
        # bla bla    

    # caricamento reale dell'immagine a schermo
    # canvasx,canvasy sono le dimensioni del canvas,sizex,sizey solo le dimensioni dell'immagine
    # positionx e positiony sono invece 
    def relase(self,event):
        self.img = ImageTk.PhotoImage(self.rawimg)
        self.updateRawImg()
    def point(self,event):
        self.counter += 1
        if self.action == 0:
            self.delete()
        if self.action == 1:
            self.rawimg.putpixel((event.x,event.y) ,(100, 100, 100))
            self.predpos = [(event.x,event.y)]
            self.relase(None)
        # tutti i casi, con event poi possiamo p
        # elif self.acrion == 1: 
        # bla bla    
    def loadInCanvas(self,positionx,positiony):
        self.canvas = Canvas(master=self.window,width=self.imgsize[0],height=self.imgsize[1],bg="white")
        self.id = self.canvas.create_image(self.imgsize[0]/2, self.imgsize[1]/2,image = self.img)
        self.drawimg = ImageDraw.Draw(self.rawimg)
        self.canvas.place(x=positionx,y=positiony)
        self.canvas.bind("<Button-1>", self.point)
        self.canvas.bind("<B1-Motion>", self.pointerAction)
        self.canvas.bind("<ButtonRelease-1>", self.relase)
        
    def overwritePositionCanvas(self,canvasx,canvasy,sizex,sizey,positionx,positiony):
        self.canvas.destroy()
        self.loadInCanvas(canvasx,canvasy,sizex,sizey,positionx,positiony)
    
    def delete(self):
        if self.canvas != None:
            self.canvas.destroy()

class editImage:
    def __init__(self,window,imageW):
        self.imageWindow = imageW
        self.window = window
        self.imageWindow.setPointerAction(-1)
        self.c = ttk.Button(self.window, "elimina")
        self.c.configure(command=lambda :self.callback(0))
        self.c.place(x=10 ,y=20)
        self.e = ttk.Button(self.window, "color")
        self.e.configure(command=lambda :self.callback(1))
        self.e.place(x=10 ,y=90)
        self.f = ttk.Button(self.window, "loadnewfile")
        self.f.configure(command=lambda : self.newLoadImage(askopenfilename()).loadInCanvas(500,0))
        self.f.place(x=10 ,y=160)
    def newBlankImage(self,width,height):
        self.imageWindow.loadBlankImage(width,height)
        return self.imageWindow
    def newLoadImage(self,path):
        self.imageWindow.loadNewImage(path)
        return self.imageWindow
    def callback(self,num):
        self.imageWindow.setPointerAction(num)

window = ttk.Tk()
window.state('zoomed')
window.resizable(False, True)


(editImage(window,imageWindow(window)))



window.mainloop()
    
from tkinter import *
from PIL import ImageTk, Image, ImageGrab
from tkinter import filedialog
import cv2 as cv
import numpy as np
import os


root = Tk()
screen_width = 1366
screen_height = 768
root.geometry(str(screen_width)+"x"+str(int(screen_height)))
root.resizable(0,0)
root.title("Editor")

global isblur
isblur = 0
global isgray
isgray=0

global name
name = ''


def open_():
    global img
    global canvas
    global resized_image
    global new_img
    global file
    global gray_button
    global normal_button
    global blur_button
    global edge_button
    global horizontal
    global export_image
    global name
    root.filename = filedialog.askopenfilename(initialdir="Images", title="Select a file", filetypes=(("all files", "*.*"),("png files", ".png"),("jpg files", ".jpg")))
    file = root.filename
    if file:
        name = file
        gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=3, column=0,pady=5)
        normal_button = Button(root, text="Normal", command=convert_normal,width=20, bg='blue', fg='white').grid(row=3, column=1,pady=5)
        blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=4, column=0,pady=5)
        edge_button = Button(root, text="Edges/Contours", command=convert_edge,width=20, bg='blue', fg='white').grid(row=4, column=1,pady=5)
        canvas= Canvas(root, width= 300, height= 300)
        canvas.grid(row=5, column=0, columnspan=2)
        img= Image.open(root.filename)
        resized_image= img.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img)
        
        horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL, command=slide)
        horizontal.grid(row=6, column=0, columnspan=2)  
        export_image = Button(root, text="Export as PNG", command=export,width=20, height=1, bg='blue', fg='white').grid(row=7, column=0,columnspan=2, padx=((screen_width/2)-70), pady=5)
    else:
        if (name != ''):
            file = name
            gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=3, column=0,pady=5)
            normal_button = Button(root, text="Normal", command=convert_normal,width=20, bg='blue', fg='white').grid(row=3, column=1,pady=5)
            blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=4, column=0,pady=5)
            edge_button = Button(root, text="Edges/Contours", command=convert_edge,width=20, bg='blue', fg='white').grid(row=4, column=1,pady=5)
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            img= Image.open(name)
            resized_image= img.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
            
            horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL, command=slide)
            horizontal.grid(row=6, column=0, columnspan=2)  
            export_image = Button(root, text="Export as PNG", command=export,width=20, height=1, bg='blue', fg='white').grid(row=7, column=0,columnspan=2, padx=((screen_width/2)-70), pady=5)
        else:
            Label(root, text="CHOOSE AN IMAGE").grid(row=3, column=0, columnspan=2)    
            
caution1 = Label(root, text='CAUTION: You cannot change the grayscale/blur attribute of a contoured image.', font=('Arial', 15)).grid(row=0, column=0, columnspan=2, pady=(20,0))
caution2 = Label(root, text='You can change brightness of a grayscale/blur image but not of a contoured image and you cannot change anything after changing the brightness. So change the brightness at the end.', font=('Arial', 12)).grid(row=1, column=0, columnspan=2, pady=(10,5))
open_image = Button(root, text="Open Image", command=open_, width=20, height=3, bg='blue', fg='white').grid(row=2, column=0,columnspan=2, padx=((screen_width/2)-70), pady=30)
def export():
    filename = filedialog.asksaveasfilename(title = "Create Image")
    if filename:
        if os.path.exists(filename):
            print("Name already exists!")
        else:
                x1 = root.winfo_rootx() + canvas.winfo_x()
                y1 = root.winfo_rooty() + canvas.winfo_y()
                x2 = x1 + canvas.winfo_width()
                y2 = y1 + canvas.winfo_height()
                # Extract image
                image = ImageGrab.grab().crop((x1, y1, x2, y2))
                # And save it
                image.save(filename+'.png')
                print(f"Saved image")
    else:
        print("Cancel")


def convert_gray():
    global img
    global file     
    global canvas
    global resized_image
    global new_img
    global blur_button
    global edge_button
    global isgray
    global isblur
    global blur
    global blur_pil
    
    
    if isgray==0:
        if isblur == 0:
            img = cv.imread(file)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray_pil = Image.fromarray(gray)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= gray_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
            
           
        else:
        
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
            gray_pil = Image.fromarray(gray)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= gray_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='black', fg='white').grid(row=3, column=0,pady=5)
    else:
        if isblur==0:
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            img= Image.open(file)
            resized_image= img.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
            
    
        else:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            blur_pil = Image.fromarray(blur)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= blur_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=3, column=0,pady=5)
    
    isgray=abs(isgray-1)
    
def convert_normal():

    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur_button
    global edge_button
    global isblur
    global isgray
    
    isgray=0
    isblur=0
    canvas.grid_forget()
    canvas= Canvas(root, width= 300, height= 300)
    canvas.grid(row=5, column=0, columnspan=2)
    img= Image.open(file)
    resized_image= img.resize((300,300), Image.LANCZOS)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, anchor=NW, image=new_img)
    gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=3, column=0,pady=5)
    blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=4, column=0,pady=5)
    edge_button = Button(root, text="Edges/Contours", command=convert_edge,width=20, bg='blue', fg='white').grid(row=4, column=1,pady=5)
    horizontal.set(0)
def convert_blur():
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global gray_button
    global blur
    global blur_pil
    global isblur
    global isgray
    
    if isblur==0:
        if isgray==0:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            blur_pil = Image.fromarray(blur)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= blur_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)  
        else:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
            gray_pil = Image.fromarray(gray)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= gray_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='black', fg='white').grid(row=4, column=0,pady=5)
    else:
         if isgray==0:
             canvas.grid_forget()
             canvas= Canvas(root, width= 300, height= 300)
             canvas.grid(row=5, column=0, columnspan=2)
             img= Image.open(file)
             resized_image= img.resize((300,300), Image.LANCZOS)
             new_img = ImageTk.PhotoImage(resized_image)
             canvas.create_image(0,0, anchor=NW, image=new_img)
             
    
         if isgray==1:
             img = cv.imread(file)
             gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
             gray_pil = Image.fromarray(gray)
             canvas.grid_forget()
             canvas= Canvas(root, width= 300, height= 300)
             canvas.grid(row=5, column=0, columnspan=2)
             resized_image= gray_pil.resize((300,300), Image.LANCZOS)
             new_img = ImageTk.PhotoImage(resized_image)
             canvas.create_image(0,0, anchor=NW, image=new_img)
         blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=4, column=0,pady=5)
    isblur = abs(isblur-1)

    
def convert_edge():
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur
    global blur_pil
    global gray
    global gray_pil
    global gray_button
    global blur_button
    global isblur
    global isgray
    if isblur == 0:
        if isgray==0:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            canny = cv.Canny(rgb, 125, 175,)
            canny_pil = Image.fromarray(canny)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= canny_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        else:
            img = cv.imread(file)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            canny = cv.Canny(gray, 125, 175,)
            canny_pil = Image.fromarray(canny)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= canny_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        
    if isblur==1:
        if isgray==0:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            canny = cv.Canny(blur, 125, 175,)
            canny_pil = Image.fromarray(canny)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= canny_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
        else:
            img = cv.imread(file)
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
            canny = cv.Canny(gray, 125, 175,)
            canny_pil = Image.fromarray(canny)
            canvas.grid_forget()
            canvas= Canvas(root, width= 300, height= 300)
            canvas.grid(row=5, column=0, columnspan=2)
            resized_image= canny_pil.resize((300,300), Image.LANCZOS)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
            
        
    
    gray_button = Button(root, text="Grayscale", command=convert_gray, state=DISABLED,width=20, bg='blue', fg='white').grid(row=3, column=0,pady=5)
    blur_button = Button(root, text="Blur", command=convert_blur, state=DISABLED,width=20, bg='blue', fg='white').grid(row=4, column=0,pady=5)
    
def slide(e):
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur
    global blur_pil
    global gray
    global gray_pil
    global gray_button
    global blur_button
    global edge_button
    global horizontal
    global isblur
    global isgray

    
    canvas.grid_forget()
    canvas= Canvas(root, width= 300, height= 300)
    canvas.grid(row=5, column=0, columnspan=2)
    
    if isgray == 0 and isblur == 0:
        img= cv.imread(file)
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        M = np.ones(img.shape, dtype='uint8') * abs(horizontal.get())
        if horizontal.get() > 0:
            added = cv.add(rgb, M)      
        elif horizontal.get() < 0:
            added = cv.subtract(rgb, M)  
        elif horizontal.get() == 0:
            added = rgb
        added_pil = Image.fromarray(added)
        
        
        resized_image= added_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img)    
        
    elif isgray == 1 and isblur==0:
        img = cv.imread(file)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        M = np.ones(gray.shape, dtype='uint8') * abs(horizontal.get())
        if horizontal.get() > 0:
            added = cv.add(gray, M)      
        elif horizontal.get() < 0:
            added = cv.subtract(gray, M)  
        elif horizontal.get() == 0:
            added = gray
        added_pil = Image.fromarray(added)
        
        
        resized_image= added_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img) 
    elif isgray==0 and isblur==1:
        img = cv.imread(file)
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
        M = np.ones(blur.shape, dtype='uint8') * abs(horizontal.get())
        if horizontal.get() > 0:
            added = cv.add(blur, M)      
        elif horizontal.get() < 0:
            added = cv.subtract(blur, M)  
        elif horizontal.get() == 0:
            added = blur
        added_pil = Image.fromarray(added)
        
        
        resized_image= added_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img) 
    
    elif isgray==1 and isblur==1:
        img = cv.imread(file)
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
        gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
        M = np.ones(gray.shape, dtype='uint8') * abs(horizontal.get())
        if horizontal.get() > 0:
            added = cv.add(gray, M)      
        elif horizontal.get() < 0:
            added = cv.subtract(gray, M)  
        elif horizontal.get() == 0:
            added = gray
        added_pil = Image.fromarray(added)
        
        
        resized_image= added_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img) 
root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2 as cv
import numpy as np

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(screen_width)+"x"+str(int(screen_height)))
root.title("Editor")

global isblur
isblur = 0


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
    root.filename = filedialog.askopenfilename(initialdir="Images", title="Select a file", filetypes=(("all files", "*.*"),("png files", ".png"),("jpg files", ".jpg")))
    file = root.filename
    if file:
        gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=1, column=0,pady=5)
        normal_button = Button(root, text="Normal", command=convert_normal,width=20, bg='blue', fg='white').grid(row=1, column=1,pady=5)
        blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=2, column=0,pady=5)
        edge_button = Button(root, text="Edges/Contours", command=convert_edge,width=20, bg='blue', fg='white').grid(row=2, column=1,pady=5)
        canvas= Canvas(root, width= 400, height= 400)
        canvas.grid(row=3, column=0, columnspan=2)
        img= Image.open(root.filename)
        resized_image= img.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(50,10, anchor=NW, image=new_img)
        horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL)
        horizontal.grid(row=4, column=0)  
        bright_button = Button(root, text="Brightness",command=slide,width=20, bg='blue', fg='white').grid(row=4, column=1)
    else:
        Label(root, text="CHOOSE AN IMAGE").grid(row=1, column=0, columnspan=2)
    

open_image = Button(root, text="Open Image", command=open_, width=20, height=3, bg='blue', fg='white').grid(row=0, column=0, columnspan=2, padx=((screen_width/2)-50), pady=30)
def convert_gray():
    global img
    global file     
    global canvas
    global resized_image
    global new_img
    global blur_button
    global edge_button
    
    img = cv.imread(file)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_pil = Image.fromarray(gray)
    canvas.grid_forget()
    canvas= Canvas(root, width= 400, height= 400)
    canvas.grid(row=3, column=0, columnspan=2)
    resized_image= gray_pil.resize((300,300), Image.LANCZOS)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(50,10, anchor=NW, image=new_img)
    
    blur_button = Button(root, text="Blur", command=convert_blur, state=DISABLED,width=20, bg='blue', fg='white').grid(row=2, column=0,pady=5)
    edge_button = Button(root, text="Edges/Contours", command=convert_edge, state=DISABLED,width=20, bg='blue', fg='white').grid(row=2, column=1,pady=5)
    
def convert_normal():

    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur_button
    global edge_button
    global isblur
    
    isblur=1
    canvas.grid_forget()
    canvas= Canvas(root, width= 400, height= 400)
    canvas.grid(row=3, column=0, columnspan=2)
    img= Image.open(file)
    resized_image= img.resize((300,300), Image.LANCZOS)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(50,10, anchor=NW, image=new_img)
    gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white').grid(row=1, column=0,pady=5)
    blur_button = Button(root, text="Blur", command=convert_blur,width=20, bg='blue', fg='white').grid(row=2, column=0,pady=5)
    edge_button = Button(root, text="Edges/Contours", command=convert_edge,width=20, bg='blue', fg='white').grid(row=2, column=1,pady=5)
def convert_blur():
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global gray_button
    global blur
    global blur_pil
    
    img = cv.imread(file)
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
    blur_pil = Image.fromarray(blur)
    canvas.grid_forget()
    canvas= Canvas(root, width= 400, height= 400)
    canvas.grid(row=3, column=0, columnspan=2)
    resized_image= blur_pil.resize((300,300), Image.LANCZOS)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(50,10, anchor=NW, image=new_img)
    gray_button = Button(root, text="Grayscale", command=convert_gray, state=DISABLED,width=20, bg='blue', fg='white').grid(row=1, column=0,pady=5)

def convert_edge():
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur
    global blur_pil
    global gray_button
    global blur_button
    global isblur
    if isblur == 0:
        img = cv.imread(file)
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        canny = cv.Canny(rgb, 125, 175,)
        canny_pil = Image.fromarray(canny)
        canvas.grid_forget()
        canvas= Canvas(root, width= 400, height= 400)
        canvas.grid(row=3, column=0, columnspan=2)
        resized_image= canny_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(50,10, anchor=NW, image=new_img)
    if isblur==1:
        img = cv.imread(file)
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        blur = cv.GaussianBlur(rgb, (7,7), cv.BORDER_DEFAULT)
        canny = cv.Canny(blur, 125, 175,)
        canny_pil = Image.fromarray(canny)
        canvas.grid_forget()
        canvas= Canvas(root, width= 400, height= 400)
        canvas.grid(row=3, column=0, columnspan=2)
        resized_image= canny_pil.resize((300,300), Image.LANCZOS)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(50,10, anchor=NW, image=new_img)
    gray_button = Button(root, text="Grayscale", command=convert_gray, state=DISABLED,width=20, bg='blue', fg='white').grid(row=1, column=0,pady=5)
    blur_button = Button(root, text="Blur", command=convert_blur, state=DISABLED,width=20, bg='blue', fg='white').grid(row=2, column=0,pady=5)
    
def slide():
    global img
    global file
    global canvas
    global resized_image
    global new_img
    global blur
    global blur_pil
    global gray_button
    global blur_button
    global edge_button
    global horizontal
    
    gray_button = Button(root, text="Grayscale", command=convert_gray, state=DISABLED,width=20, bg='blue', fg='white').grid(row=1, column=0,pady=5)
    blur_button = Button(root, text="Blur", command=convert_blur, state=DISABLED,width=20, bg='blue', fg='white').grid(row=2, column=0,pady=5)
    edge_button = Button(root, text="Edges/Contours", command=convert_edge, state=DISABLED,width=20, bg='blue', fg='white').grid(row=2, column=1,pady=5)
    
    canvas.grid_forget()
    canvas= Canvas(root, width= 400, height= 400)
    canvas.grid(row=3, column=0, columnspan=2)
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
    canvas.create_image(50,10, anchor=NW, image=new_img)
        



root.mainloop()
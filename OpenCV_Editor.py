from tkinter import *
from tkinter import messagebox 
import cv2 as cv
from PIL import ImageTk, Image, ImageGrab, ImageOps, ImageFilter, ImageEnhance
from tkinter import filedialog
import numpy as np
import os
root = Tk()
root.geometry("800x600")
root.resizable(0,0)
root.title("Image Editor")
global name

name = ''
global settings 
settings = {
    'gray':False,
    'blur':0,
    'contours':0,
    'brightness':1,
}
global width
global height
    
def open_():
    global img
    global backup_img
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
    global width
    global height
    root.filename = filedialog.askopenfilename(initialdir="Images", title="Select a file", filetypes=(("all files", "*.*"),("png files", ".png"),("jpg files", ".jpg")))
    file = root.filename
    
    if file:
        name = file
       
        gray_button = Button(root, text="Grayscale", command=convert_gray,width=20, bg='blue', fg='white')
        gray_button.grid(row=3, column=0,pady=5)
        normal_button = Button(root, text="Normal",width=20, bg='blue', fg='white', command=normal)
        normal_button.grid(row=3, column=1,pady=5)
        blur_button = Scale(root, label='Blur',from_=0, to=10, length=160,bg='blue',fg='white', orient=HORIZONTAL, command=blur)
        blur_button.grid(row=4, column=0,pady=5)
        edge_button = Button(root, text="Edges/Contours", width=20, bg='blue', fg='white', command=edges).grid(row=4, column=1,pady=5)
        try:
            img = Image.open(root.filename)
            backup_img = Image.open(root.filename)
        except:
            messagebox.showinfo("showinfo", "Select Image File") 
        
        width, height = img.size
        width = int(width*300/height)
        height = 300
        
        canvas= Canvas(root, width=int(width), height= int(height))
        canvas.grid(row=5, column=0, columnspan=2)
        
        resized_image= img.resize((int(width),int(height)), Image.NEAREST)
        new_img = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor=NW, image=new_img)
        
        horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL, command=brightness)
        horizontal.grid(row=6, column=0, columnspan=2)  
        export_image = Button(root, text="Export as PNG",width=20, height=1, bg='blue', fg='white', command=export).grid(row=7, column=0,columnspan=2, padx=300, pady=5)
    else:
        if (name != ''):
            file = name
            
            gray_button = Button(root, text="Grayscale",command=convert_gray,width=20, bg='blue', fg='white')
            gray_button.grid(row=3, column=0,pady=5)
            normal_button = Button(root, text="Normal",width=20, bg='blue', fg='white', command=normal)
            normal_button.grid(row=3, column=1,pady=5)
            blur_button = Scale(root, label='Blur',from_=0, to=10, length=160,bg='blue',fg='white', orient=HORIZONTAL,  command=blur)
            blur_button.grid(row=4, column=0,pady=5)
            edge_button = Button(root, text="Edges/Contours",width=20, bg='blue', fg='white', command=edges).grid(row=4, column=1,pady=5)
            try:
                img = Image.open(name)
                backup_img = Image.open(name)
            except:
                messagebox.showinfo("showinfo", "Select Image File") 
            
            width, height = img.size
            width = int(width*300/height)
            height = 300
            canvas= Canvas(root, width= int(width), height= int(height))
            canvas.grid(row=5, column=0, columnspan=2)
            
            resized_image= img.resize((int(width),int(height)), Image.NEAREST)
            new_img = ImageTk.PhotoImage(resized_image)
            canvas.create_image(0,0, anchor=NW, image=new_img)
            
            horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL,command=brightness)
            horizontal.grid(row=6, column=0, columnspan=2)  
            export_image = Button(root, text="Export as PNG",width=20, height=1, bg='blue', fg='white', command=export).grid(row=7, column=0,columnspan=2, padx=300, pady=5)
        else:
            Label(root, text="CHOOSE AN IMAGE").grid(row=3, column=0, columnspan=2)    
open_image = Button(root, text="Open Image", command=open_, width=13, height=2, bg='blue', fg='white', font=('Arial', 12)).grid(row=0, column=0,columnspan=2, padx=300, pady=10)

def convert_gray():
    global gray_button
    global settings
    global img
    global canvas
    global new_img
    global resized_image
    if settings['gray'] == False:
        gray_button.configure(bg='red') 
        settings.update({'gray':True})
        img = ImageOps.grayscale(img) 
        
            
    else:
        gray_button.configure(bg='blue')    
        settings.update({'gray':False})
        img = backup_img
        img = img.filter(ImageFilter.BoxBlur(blur_button.get()))
        brightened = ImageEnhance.Brightness(img)
        img = brightened.enhance(settings['brightness'])
    img = img.filter(ImageFilter.BoxBlur(blur_button.get()))
    brightened = ImageEnhance.Brightness(img)
    img = brightened.enhance(settings['brightness'])
    width, height = img.size
    width = int(width*300/height)
    height = 300
    canvas.grid_forget()
    canvas= Canvas(root, width= width, height= height)
    canvas.grid(row=5, column=0, columnspan=2)
    resized_image= img.resize((width,height), Image.NEAREST)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, anchor=NW, image=new_img)
def blur(e):
    global blur_button
    global settings
    global img
    global canvas
    global new_img
    global resized_image
    global backup_img
    img = img.filter(ImageFilter.BoxBlur(blur_button.get()))
    brightened = ImageEnhance.Brightness(img)
    img = brightened.enhance(settings['brightness'])
    width, height = img.size
    width = int(width*300/height)
    height = 300
    canvas.grid_forget()
    canvas= Canvas(root, width= width, height= height)
    canvas.grid(row=5, column=0, columnspan=2)
    resized_image= img.resize((width,height), Image.NEAREST)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, anchor=NW, image=new_img)
    settings.update({'blur':blur_button.get()})
    img = backup_img
    
    if settings['gray']==True:
        img = ImageOps.grayscale(img)
def brightness(e):
    global blur_button
    global settings
    global img
    global canvas
    global new_img
    global resized_image
    global backup_img
    global horizontal
    if horizontal.get()>0:
        brightness_level = 1 + horizontal.get()/40
    if horizontal.get()<0:
        brightness_level = 1 + horizontal.get()/150
    if horizontal.get()==0:
        brightness_level = 1
        
    settings.update({'brightness':brightness_level})
    img = img.filter(ImageFilter.BoxBlur(settings['blur']))
    brightened = ImageEnhance.Brightness(img)
    img = brightened.enhance(settings['brightness'])
    width, height = img.size
    width = int(width*300/height)
    height = 300
    canvas.grid_forget()
    canvas= Canvas(root, width= width, height= height)
    canvas.grid(row=5, column=0, columnspan=2)
    resized_image= img.resize((width,height), Image.NEAREST)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, anchor=NW, image=new_img)
    
    img = backup_img
    
    if settings['gray']==True:
        img = ImageOps.grayscale(img)
def normal():
    global blur_button
    global gray_button
    global settings
    global img
    global canvas
    global new_img
    global resized_image
    global backup_img
    img= backup_img
    width, height = img.size
    width = int(width*300/height)
    height = 300
    canvas= Canvas(root, width= int(width), height= int(height))
    canvas.grid(row=5, column=0, columnspan=2)
            
    resized_image= img.resize((int(width),int(height)), Image.NEAREST)
    new_img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, anchor=NW, image=new_img)
    settings.update({'gray':False})
    settings.update({'brightness':1})
    settings.update({'blur':0})
    settings.update({'contours':0})
    gray_button.configure(bg='blue')
    blur_button = Scale(root, label='Blur',from_=0, to=10, length=160,bg='blue',fg='white', orient=HORIZONTAL, command=blur)
    blur_button.grid(row=4, column=0,pady=5)
    horizontal = Scale(root, label='Brightness',from_=-100, to=100, length=200,bg='blue',fg='white', orient=HORIZONTAL, command=brightness)
    horizontal.grid(row=6, column=0, columnspan=2)  
def export():
        global img
        filename = filedialog.asksaveasfilename(title = "Create Image")
        
        if filename:
            if os.path.exists(filename):
                print("Name already exists!")
            else:
                
                
                img.save(filename+'.png')
                print(f"Saved image")
        else:
            print("Cancel")
def edges():
    global img
    global canvas2
    global resized_image2
    global new_img2
    global inverted
    global invert_button
    inverted = False
    open_cv_image = np.array(img)
    
    open_cv_image = open_cv_image[:, ::-1].copy()

    width, height = img.size
    width = int(width*300/height)
    height = 300
    
    new_window = Toplevel()
    new_window.title("Contours")
    new_window.geometry("600x600")
    def reveal_contours(e):
        global img
        global canvas2
        global resized_image2
        global new_img2
        global inverted
        global invert_button
        global open_cv_image
        global pil_img
        invert_button.configure(state=NORMAL)
        export_contour.configure(state=NORMAL)
        open_cv_image = np.array(img)
    
        open_cv_image = open_cv_image[:, ::-1].copy()
        open_cv_image = cv.Canny(open_cv_image, int(contour_slider.get()/1.5),int((contour_slider.get()+30)/1.5))
        
        width, height = img.size
        width = int(width*300/height)
        height = 300
        
        if inverted == True:
            ret, thresh = cv.threshold(open_cv_image, 125, 255, cv.THRESH_BINARY_INV)
            pil_img = Image.fromarray(thresh)
        else:
            pil_img = Image.fromarray(open_cv_image) 
        pil_img = ImageOps.mirror(pil_img)
        canvas2.grid_forget()
        
        canvas2= Canvas(new_window, width= width, height= height)
        canvas2.grid(row=0, column=0, padx=200)
        resized_image2= pil_img.resize((width,height), Image.NEAREST)
        new_img2 = ImageTk.PhotoImage(resized_image2)
        canvas2.create_image(0,0, anchor=NW, image=new_img2)
    def invert():
        global pil_img
        global img
        global canvas2
        global resized_image2
        global new_img2
        global inverted
        global open_cv_image
       
        
        width, height = img.size
        width = int(width*300/height)
        height = 300

        
        ret, thresh = cv.threshold(open_cv_image, 125, 255, cv.THRESH_BINARY_INV)
        open_cv_image = thresh
        pil_img = Image.fromarray(thresh)
        
             

        pil_img = ImageOps.mirror(pil_img)
        
        canvas2.grid_forget()
        
        canvas2= Canvas(new_window, width= width, height= height)
        canvas2.grid(row=0, column=0, padx=200)
        resized_image2= pil_img.resize((width,height), Image.NEAREST)
        new_img2 = ImageTk.PhotoImage(resized_image2)
        canvas2.create_image(0,0, anchor=NW, image=new_img2)
        inverted = not inverted
    canvas2= Canvas(new_window, width= width, height= height)
    canvas2.grid(row=0, column=0, padx=200)
    resized_image2= img.resize((width,height), Image.NEAREST)
    new_img2 = ImageTk.PhotoImage(resized_image)
    canvas2.create_image(0,0, anchor=NW, image=new_img)
    contour_slider = Scale(new_window, label='Contours',from_=0, to=201, length=201,bg='blue',fg='white', orient=HORIZONTAL,command=reveal_contours)
    contour_slider.grid(row=1, column=0)
    invert_button = Button(new_window, text='Invert Color', bg='blue', fg='white', command=invert,state = DISABLED)
    invert_button.grid(row=2, column=0,pady=10)
    def export_contour():
        global pil_img
        filename = filedialog.asksaveasfilename(title = "Create Image")
        
        if filename:
            if os.path.exists(filename):
                print("Name already exists!")
            else:
                
                
                pil_img.save(filename+'.png')
                print(f"Saved image")
        else:
            print("Cancel")
    export_contour = Button(new_window, text='Export as PNG', bg='blue', fg='white', command=export_contour,state=DISABLED)
    export_contour.grid(row=3, column=0)
root.mainloop()

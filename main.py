#Tkinter app to add watermark to images !
#
# A similar online service is: https://watermarkly.com/
#
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from PIL import Image,ImageDraw,ImageFont,ImageTk

window = Tk()
window.title("Watermarker")
window.config(padx=40,pady=30)
window.resizable(FALSE,FALSE)

def create_img(path):
    img = Image.open(f"{path}",mode='r')
    I1 = ImageDraw.Draw(img)
    wid, ht = img.size
    f_size=int(wid/20)
    myFont = ImageFont.truetype("arial.ttf", f_size)
    I1.text((50, 60), f"{t.get()}", font=myFont, fill=(229, 229, 229))
    I1.text((wid-200, ht-50), f"{t.get()}", font=myFont, fill=(229, 229, 229))
    img.show()

def open_file():
    global filename
    filetypes = (
        ('Image Files', '*jpeg'),
        ('All files', '*.*')
    )
    filename = askopenfile(
        title='Open a file',
        filetypes=filetypes)
    create_img(filename.name)

def btn_save():
    path = filename.name
    img = Image.open(f"{path}", mode='r')
    I1 = ImageDraw.Draw(img)
    wid, ht = img.size
    f_size = int(wid / 20)
    myFont = ImageFont.truetype("arial.ttf", f_size)
    I1.text((50, 50), f"{t.get()}", font=myFont, fill=(229, 229, 229))
    I1.text((wid - 200, ht - 50), f"{t.get()}", font=myFont, fill=(229, 229, 229))
    save_path = path[:-5] + "-edit" + ".jpeg"
    img.save(f"{save_path}", mode='r')
    showinfo("Saved","Watermarked image saved successfully")

label = Label(text="Add your text and image to add watermark",font=80)
label.grid(row=0,column=0,columnspan=3,padx=30,pady=20)

add_img = Button(
    window,
    text ='Choose File',
    command = lambda:open_file()
    )
add_img.grid(row=2,column=2,padx=30)

t_label = Label(text="Enter the text to watermark")
t_label.grid(row=1,column=0)

t= Entry(width=15)
t.grid(row=2,column=0)

btn=Button(text="Save Edited image",command=btn_save)
btn.grid(row=3,column=1,pady=5)

window.mainloop()
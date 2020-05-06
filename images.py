            #---------------------------------#
            #creating the stable  image viewer#
            #---------------------------------#
from tkinter import *
from PIL import ImageTk,Image
#importing the tkinter and pillow packages
root=Tk()#creating the root window
root.geometry("500x500")#assign the window size
root.title("image test")#assign the title to window
root.iconbitmap("icon.ico")#adding the icon to window
#note: here we take only ico file as input search for web site that convert image into ico files
#creating and assigning  the image values
my_img1=ImageTk.PhotoImage(Image.open("path of image.png"))
my_img2=ImageTk.PhotoImage(Image.open("path of image.png"))
my_img3=ImageTk.PhotoImage(Image.open("path of image.png"))
my_img4=ImageTk.PhotoImage(Image.open("path of image.png"))
my_img5=ImageTk.PhotoImage(Image.open("path of image.png"))
#creating list of images
img_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img1)#creating for default image
my_label.grid(row=0,column=0,columnspan=3)#we use grid insted to pack beacuse we need to put buttons for">>""<<","exit
status=Label(root,text="image 1 of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
#ausing bd,relief nad anchor label tag to make window
def froward(img_num):#funcyion for forward
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()#to erase the old photo for the progra memory
    my_label=Label(image=img_list[img_num-1])
    button_forward=Button(root,text=">>",command=lambda :froward(img_num+1))
    #when click the button ">>" that increment the image value by one
    button_back= Button(root, text="<<", command=lambda: backword(img_num-1))
    # when click the button "<<" that decrement the image value by one
    if(img_num==5):
        button_forward = Button(root, text=">>", state=DISABLED)
        #if the image number is 5 then it disable the ">>"button
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="image " +str(img_num)+"of "+ str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    #creation of the status bar

def backword(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=img_list[img_num-1])
    button_forward=Button(root,text=">>",command=lambda :froward(img_num+1))
    button_back= Button(root, text="<<", command=lambda :backword(img_num-1))
    if (img_num == 1):
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text="image " +str(img_num)+"of "+ str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
#assign the grid column and rows
button_exit=Button(root,text="exit",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:froward(2))
button_back=Button(root,text="<<",command=backword,state=DISABLED)
button_exit.grid(row=1,column=1,pady=10)
button_forward.grid(row=1,column=2)
button_back.grid(row=1,column=0)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
#execute the main loop
root.mainloop()
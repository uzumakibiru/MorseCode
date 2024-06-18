# Import random to generate choose random variable

from morsecode import decode
from tkinter import *
from tkinter import messagebox


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#Function to get the user Input and change to morse code
def to_morse():
    # morse_box.delete(0,END)
    user_text=text_box.get().upper()
    code=[]
    for i in user_text:
        # code=[key for key in decode.keys() if decode[key]==i]
        # print(code)
        for key in decode.keys():
            
            if decode[key]== i:
                code.append(key)
    str_code=','.join(code)
    morse_message= Message(width=400,fg="black",text=str_code,font=(FONT_NAME,20,"bold"))
    morse_message.grid(row=4,column=0)
    
    # A message box output
    # messagebox.showinfo(title="To Morsecode",message=f"{user_text}\n {str_code}")
    # Output on a textbox
    # morse_box.insert(END,string=str_code)

window=Tk()
window.title("To Morsecode")

window.config(padx=100,pady=100)
#Load image
img_path= PhotoImage(file="logo.png")
morse_logo= Canvas(width=100,height=100)
morse_logo.create_image(50,50,image=img_path)
morse_logo.grid(row=0,column=0)

#User input
text_label=Label(text="Enter any text")
text_label.grid(row=1,column=0)

text_box=Entry(width=40)
text_box.grid(row=2,column=0)

#Button to change to morsecode
morse_button=Button(text="To Morse",width=15,command=to_morse)
morse_button.grid(row=3,column=0)

#Morse Text
# morse_box=Entry(width=40)
# morse_box=Text(height=2,width=20)
# morse_box.grid(row=4,column=0)

# Morse Message
# morse_message= Message(text="Your Morsecode")
# morse_message.grid(row=4,column=0)

window.mainloop()
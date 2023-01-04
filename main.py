from tkinter import *

from Circle import Circle


def is_float(string): #String nime võib määrata ise
    try:
        float(string)
        return True
    except ValueError:
        return False

def calculate(event):
    #print("Button clicked") #test
    radius = user_input.get() #radius is string
    print(radius) #Test
    if is_float(radius):
        user_input.delete(0, END)
        radius = float(radius) # now is radius float
        circle = Circle(radius)
        txt_field["state"] = "normal" #can change text field
        txt_field.delete("1.0", END) # Clear txt_fields line 1 to end
        txt_field.insert(END, "Radius: " +str(circle.radius) + "\n")
        txt_field.insert(END, "Diameter: " + str(circle.diameter()) + "\n")
        txt_field.insert(END, "Perimeter: " + str(circle.perimeter()) + "\n")
        txt_field.insert(END, "Area: " + str(circle.area()) + "\n")
        txt_field["state"] = "disabled" # user cant change text field
        # print("Number")  # test
    # else:  # test
        # print("Error")  # test

#Main window properties
window = Tk()
window.title("Geometry - Circle") # Title text
window.geometry("400x500") #w-400 h-500
window.resizable(False,False) # suuruste muutmine - laius, kõrgus. False ei saa muuta, True saab muuta

# Frames
frame_top = Frame(window, bg="#89CFF0", height=50)
frame_top.pack(fill="both") # võib kasutada ka x ja y

frame_bottom = Frame(window, bg="#90EE90", height=50)
frame_bottom.pack(fill="both") #võib kirjutatda suute tähtededega BOTH. Siis ei pea kirjutama ülekomasid

#First line in frame top

lbl = Label(frame_top, text="Circle radius:", bg="#89CFF0") #lbl ise määratud
lbl.pack(side="left") #võib kirjutatda suute tähtededega LEFT. Siis ei pea kirjutama ülekomasid

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus() # kursor on kohe aktiivne


btn_calc = Button(frame_top, text="Calculate", command=lambda: calculate(0))
btn_calc.pack(side=LEFT, padx=4, pady=4) # "ipadx/y" saab muuta nupu suurust

# second line, one big textfield
txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side=LEFT, padx=2,pady=2)

# Bind Entry key
window.bind("<Return>", lambda event: calculate(event))

# No MVC last line
window.mainloop()
from tkinter import *
from variable_storage import *
from skill_functions import *
#from skill_labels import *
window = Tk()
# add widgets here

#Frame for Combat Modifiers
skill_frame = Frame(window, height = 100, width = 100, bd = 2, relief=GROOVE)
skill_frame.pack
skill_frame.place(x = 10)



appraise_value_label = Label(skill_frame, text = appraise_skill(appraise_ranks, int_bonus, appraise_misc), fg = 'black', font = ('Helvetica', 12))
























window.title("Jans'risian Record of Birth")
window.geometry("1280x720+10+20")
window.mainloop()





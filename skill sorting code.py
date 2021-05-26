from tkinter import *
from variable_storage import *
from skill_functions import *



#Pulls associated variables from skill list
def skill_sorter():
    with open("skill_labels.py") as skills:
        for line in skills:
            x = line.partition('_')[0]
            print(str(x + '= Label(skill_frame, text =' + x + " + ': ', fg = 'black', font = ('Helvetica', 12))" + x +".pack(fill=BOTH)" + x + "_entry = Entry(skill_frame, width = 5, text = '', bd = 1)" + x + "_entry.pack(fill=BOTH)"))

skill_sorter()


            # #Attribute Entry:
            # name_lbl = Label(NEEDS FRAME, text = ": ", fg = "black", font = ("Helvetica", 12))
            # name_lbl.pack(fill = BOTH)
            # name_entry = Entry(NEEDS FRAME, width = 5, text = "", bd = 1)
            # name_entry.pack(fill = BOTH)


# #Pulls relevant info from sorted skills list and inserts into label code
# def labeler_function():
#     with open("skill_list.py") as skills:
#         iteration = 0
#         for line in skills:
#             x = line.partition("skill")[0] +"value_label"
#             print(x +" = Label(skill_frame, text = " + line + ", fg = 'black', font = ('Helvetica', 12))")

# text = raw_input("Type something:")
# left_text = text.partition("!")[0]
# #Retrieves skills from skills file
# with open("skill_functions.py") as skills:
#     for line in skills:
#         if "def" in line:
#             print(line)
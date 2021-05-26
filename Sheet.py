from tkinter import *
#from skills import *
window = Tk()
# add widgets here

#This will be the stats page.  Enter attributes and combat stats here to be displayed on main character page



#Page label
lbl = Label(window, text = "Jans'risian Record of Birth", fg = "black", font = ("Helvetica", 18))
lbl.place(x = 500, y = 30)

#Frame for attributes
attribute_frame = Frame(window, height = 200, width = 100, bd = 2, relief=GROOVE)
attribute_frame.pack
attribute_frame.place(x = 10)

#Attribute Entry: Strength
strength_lbl = Label(attribute_frame, text = "Strength: ", fg = "black", font = ("Helvetica", 12))
strength_lbl.pack(fill = BOTH)
strength_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
strength_entry.pack(fill = BOTH)

#Attribute Entry: Dexterity
dexterity_lbl = Label(attribute_frame, text = "Dexterity: ", fg = "black", font = ("Helvetica", 12))
dexterity_lbl.pack(fill = BOTH)
dexterity_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
dexterity_entry.pack(fill = BOTH)

#Attribute Entry: Constitution
constitution_lbl = Label(attribute_frame, text = "Constitution: ", fg = "black", font = ("Helvetica", 12))
constitution_lbl.pack(fill = BOTH)
constitution_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
constitution_entry.pack(fill = BOTH)

#Attribute Entry: Intelligence
intelligence_lbl = Label(attribute_frame, text = "Intelligence: ", fg = "black", font = ("Helvetica", 12))
intelligence_lbl.pack(fill = BOTH)
intelligence_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
intelligence_entry.pack(fill = BOTH)

#Attribute Entry: Wisdom
wisdom_lbl = Label(attribute_frame, text = "Wisdom: ", fg = "black", font = ("Helvetica", 12))
wisdom_lbl.pack(fill = BOTH)
wisdom_entry_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
wisdom_entry_entry.pack(fill = BOTH)

#Attribute Entry: Charisma
charisma_lbl = Label(attribute_frame, text = "Charisma: ", fg = "black", font = ("Helvetica", 12))
charisma_lbl.pack(fill = BOTH)
charisma_entry = Entry(attribute_frame, width = 5, text = "", bd = 1)
charisma_entry.pack(fill = BOTH)




#Frame for Combat Modifiers
combat_frame = Frame(window, height = 100, width = 100, bd = 2, relief=GROOVE)
combat_frame.pack
combat_frame.place(x = 10)



#Attribute Entry: Base Attack Bonus
bab_lbl = Label(combat_frame, text = "Base Attack Bonus:", fg = "black", font = ("Helvetica", 12))
bab_lbl.pack(fill = BOTH)
bab_entry = Entry(combat_frame, width = 5, text = "", bd = 1)
bab_entry.pack(fill = BOTH)

#Attribute Entry: Base Fortitude Save
fort_lbl = Label(combat_frame, text = "Base Fortitude Save: ", fg = "black", font = ("Helvetica", 12))
fort_lbl.pack(fill = BOTH)
fort_entry = Entry(combat_frame, width = 5, text = "", bd = 1)
fort_entry.pack(fill = BOTH)

#Attribute Entry: Base Reflex Save
reflex_lbl = Label(combat_frame, text = "Base Reflex Save: ", fg = "black", font = ("Helvetica", 12))
reflex_lbl.pack(fill = BOTH)
reflex_entry = Entry(combat_frame, width = 5, text = "", bd = 1)
reflex_entry.pack(fill = BOTH)

#Attribute Entry: Base Will Save
will_lbl = Label(combat_frame, text = "Base Will Save: ", fg = "black", font = ("Helvetica", 12))
will_lbl.pack(fill = BOTH)
will_entry = Entry(combat_frame, width = 5, text = "", bd = 1)
will_entry.pack(fill = BOTH)

alchemy= Label(skill_frame, text =alchemy + ': ', fg = 'black', font = ('Helvetica', 12))alchemy.pack(fill=BOTH)alchemy_entry = Entry(skill_frame, width = 5, text = '', bd = 1)alchemy_entry.pack(fill=BOTH)





# #Attribute Entry:
# namwe_lbl = Label(NEEDS FRAME, text = ": ", fg = "black", font = ("Helvetica", 12))
# name_lbl.pack(fill = BOTH)
# name_entry = Entry(NEEDS FRAME, width = 5, text = "", bd = 1)
# name_entry.pack(fill = BOTH)


attribute_frame.grid(row = 0, column = 1)
combat_frame.grid(row = 1, column = 1)


window.title("Jans'risian Record of Birth")
window.geometry("1280x720+10+20")
window.mainloop()



#Text field that allows dynamic searching and matching, (hovering over matches gives preview of match description(later?)

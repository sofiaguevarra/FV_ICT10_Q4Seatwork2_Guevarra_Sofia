import numpy as np
import pyscript

#class is blueprint for creating objects
class Classmate:
    def __init__(self, name, section, favorite_subject): #parameters (including self)
        self.name = name #attributes
        self.section = section #attributes
        self.favorite_subject = favorite_subject #attributes

    def introduce(self): #this is a method
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."
    #this will show up when the user clicks the show list button

#list of classmates:
classmates = [
    Classmate("Audrey", "Emerald", "English"),
    Classmate("Gianna", "Emerald", "Science"),
    Classmate("Luisa", "Emerald", "Math"),
    Classmate("Ioana", "Emerald", "English"),
    Classmate("Cyrene", "Emerald", "Social Studies"),
]

#this is supposed to show the list of classmates when user clicks the "show list" button
def show_list():
    output_div = pyscript.document.getElementById("output")
    results = ""


#This connects to the add classmate button, this will show users input when they click the button
def add_classmate():
    name = pyscript.document.getElementById("name").value
    section = pyscript.document.getElementById("section").value
    subject = pyscript.document.getElementById("subject").value

#order of the users input, so it won't be jumbled up (name, section, subject)
    classmates.append(Classmate(name, section, subject))

    pyscript.document.getElementById("name").value = ""
    pyscript.document.getElementById("section").value = ""
    pyscript.document.getElementById("subject").value = ""

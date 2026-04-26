from pyscript import display
from js import document, alert


classmates = []

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

def show_list(e):
    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value
    output = document.getElementById("output")
    output.innerHTML = ""  

    student1 = Classmate('Kelsey','Amethyst', 'Math')
    student2 = Classmate('Jennifer', 'Sapphire', 'Science')
    student3 = Classmate('Euan', 'Emerald', 'Computer')
    student4 = Classmate('Micah', 'Ruby', 'Art')
    student5 = Classmate('Anakin', 'Sapphire', 'History')

    display(f'Hi! my name is {student1.name} from {student1.section}. My favorite subject is {student1.subject}.', target='output')
    display(f'Hi! my name is {student2.name} from {student2.section}. My favorite subject is {student2.subject}.', target='output')
    display(f'Hi! my name is {student3.name} from {student3.section}. My favorite subject is {student3.subject}.', target='output')
    display(f'Hi! my name is {student4.name} from {student4.section}. My favorite subject is {student4.subject}.', target='output')
    display(f'Hi! my name is {student5.name} from {student5.section}. My favorite subject is {student5.subject}.', target='output')

    for student in classmates:
        display(f'Hi! my name is {name} from {section}. My favorite subject is {subject}.', target='output')

def add_classmate(e):
    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value

    if name and section and subject:
        classmates.append(Classmate(name, section, subject))
        alert(f"Student Successfully Added!") 

        document.getElementById('name').value = ""
        document.getElementById('section').value = ""
        document.getElementById('subject').value = ""
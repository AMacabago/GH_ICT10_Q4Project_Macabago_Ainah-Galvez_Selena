from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [0, 0, 0, 0, 0]

def attendance_checker(event):
    # get values
    document.getElementById("output").innerHTML = ""
    day_selected = document.getElementById("dayOption").value
    absence_number = document.getElementById("absencesOption").value

    absence_number = int(absence_number)
    index = days.index(day_selected)
    absences[index] = absence_number

    # preload to avoid font cache message
    plt.figure()
    plt.plot([0, 1], [0, 1])
    plt.close()

    # creating graph using matplotlib
    plt.figure()
    plt.plot(days, absences)

    plt.title('Weekly Attendance (Absences)')
    plt.xlabel('Days')
    plt.ylabel('Number of Absences')

    display(plt, target="output")
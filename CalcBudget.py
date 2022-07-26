from tkinter import *
from tkinter import ttk
import webbrowser

def Calc_Budget():
    goal = budget_goal.get() # assume the amount of remaining money is for entire year
    interval = budget_interval.get() # user choose the time interval for their budget goal

    if interval == "daily":
        goal = round((float(goal)/365), 2)
    elif interval == "monthly":
        goal = round((float(goal)/12), 2)
    # otherwise, the value of goal remains unchanged.

    webbrowser.open('http://localhost:5000/goal:{}interval:{}'.format(goal, interval))

window = Tk()
window.geometry("500x600")

header = Label(window, text="Budget Goal Calculator", font=('Helvetica', 18))
header.pack()

# Input windo for remaining amount of money
goal_label = Label(window, text="Enter the remaining amount of money after deduction of expenses:", font=('Helvetica', 14))
goal_label.pack()
budget_goal = Entry(window, width=40)
budget_goal.pack()

# Input window for preferred time interval
interval_label = Label(window, text="Click a button below to choose your preferred time interval:", font=('Helvetica', 14))
interval_label.pack()
budget_interval = Entry(window, width=40)
budget_interval.pack()

def onclick(text):
   budget_interval.delete(0, END)
   budget_interval.insert(0,text)

# Buttons for choosing preferred time interval
daily = ttk.Button(window, text="Budget Per Day", command=lambda: onclick("daily"))
daily.pack()
monthly = ttk.Button(window, text="Budget Per Month", command=lambda: onclick("monthly"))
monthly.pack()
yearly = ttk.Button(window, text="Budget Per Year", command=lambda: onclick("yearly"))
yearly.pack()

submit = Button(window, text="Submit", command=Calc_Budget)
submit.pack(side=BOTTOM)
window.mainloop()
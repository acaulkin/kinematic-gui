# Andrew Caulkins
# Interactive GUI for Simple Kinematics based Physics Questions

import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


fields = ('Acceleration in the X-Direction', 'Acceleration in the Y-Direction', 'Initial Velocity', 'Initial Angle')


# Physics for kinematic equations:
def kinematics(entries):
    acceleration_x = (float(entries['Acceleration in the X-Direction'].get()))  # m/s^2
    acceleration_y = (float(entries['Acceleration in the Y-Direction'].get()))  # m/s^2
    velocity_initial = (float(entries['Initial Velocity'].get()))  # m/s
    velocity_initial_angle = (float(entries['Initial Angle'].get()))  # degrees
    v0_x = velocity_initial * np.cos(velocity_initial_angle * np.pi / 180)
    v0_y = velocity_initial * np.sin(velocity_initial_angle * np.pi / 180)
    time_max = 2 * v0_y / (-acceleration_y)  # sec
    time_step = .01  # sec
    t = np.arange(0, time_max, time_step)
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    for ii in range(len(t)):
        x[ii] = v0_x * t[ii] + 1 / 2.0 * acceleration_x * (t[ii]) ** 2
        y[ii] = v0_y * t[ii] + 1 / 2.0 * acceleration_y * (t[ii]) ** 2



    # Plotting the path of the projectile:
    figure1 = Figure(figsize=(5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure1, root)
    line2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
    ax1.plot(x, y, color='r')
    ax1.axis('equal')
    ax1.set_title('Path of Projectile')
    ax1.set_ylabel('Y axis [m]', fontsize=14)
    ax1.set_xlabel('X axis [m]', fontsize=14)

# Making the basics of the GUI:
def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=25, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries
    
# Adding the plotting functionality:
if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b2 = tk.Button(root, text='Calculate',
           command=(lambda e=ents: kinematics(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Exit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
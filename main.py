import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox

f1 = 0
f2 = 4 * np.pi
a = 1
step = 0.01

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

f = np.arange(f1, f2, step)
x = a*f * np.cos(f)
y = a*f * np.sin(f)
prev, = ax.plot(x, y, lw=2)
plt.title("Archimedes spiral")

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

def change_f1(text):
    f1_data = float(text)
    f = np.arange(f1_data, f2, step)
    x = a * f * np.cos(f)
    y = a * f * np.sin(f)
    prev.set_xdata(x)
    prev.set_ydata(y)
    plt.draw()

def change_f2(text):
    f2_data = float(text)
    f = np.arange(f1, f2_data, step)
    x = a * f * np.cos(f)
    y = a * f * np.sin(f)
    prev.set_xdata(x)
    prev.set_ydata(y)
    plt.draw()

def change_a(text):
    a_data = float(text)
    f = np.arange(f1, f2, step)
    x = a_data * f * np.cos(f)
    y = a_data * f * np.sin(f)
    prev.set_xdata(x)
    prev.set_ydata(y)
    plt.draw()

def change_step(text):
    step_data = float(text)
    f = np.arange(f1, f2, step_data)
    x = a * f * np.cos(f)
    y = a * f * np.sin(f)
    prev.set_xdata(x)
    prev.set_ydata(y)
    plt.draw()


f1_axe = plt.axes([0.1, 0.02, 0.1, 0.06])
f2_axe = plt.axes([0.33, 0.02, 0.1, 0.06])
a_axe = plt.axes([0.58, 0.02, 0.1, 0.06])
step_axe = plt.axes([0.8, 0.02, 0.1, 0.06])

f1_box= TextBox(f1_axe, "f1")
f2_box= TextBox(f2_axe, "f2")
a_box= TextBox(a_axe, "a")
step_box= TextBox(step_axe, "step")

f1_box.on_submit(change_f1)
f2_box.on_submit(change_f2)
a_box.on_submit(change_a)
step_box.on_submit(change_step)

plt.show()
from tkinter import *
import parser
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

root = Tk()

# titulo
root.title('Declina y 𝚫 t')

# funciones
def clear_display():
    display.delete(0, END)
    Di.delete(0, END)
    b.delete(0, END)
    qi.delete(0, END)
    q.delete(0, END)
    m1.delete(0, END)
    m2.delete(0, END)
    m3.delete(0, END)
    m4.delete(0, END)
    p1.delete(0, END)
    p2.delete(0, END)
    p3.delete(0, END)
    p4.delete(0, END)


def Calculation():
    display.delete(0, END)
    Di1=Di.get()
    b1=b.get()
    qi1=qi.get()
    q1=q.get()
    try:
        math_expression = (((float(qi1)/float(q1))**float(b1))-1)/(float(b1)*float(Di1))
        result = int(math_expression)
        display.insert(0, result)
    finally:
        pass


def Graf():
    # Data for plotting
    Di1=Di.get()
    b1=b.get()
    qi1=qi.get()
    q1=q.get()
    t1=display.get()
    m1a=m1.get()
    m2a=m2.get()
    m3a=m3.get()
    m4a=m4.get()
    p1a=p1.get()
    p2a=p2.get()
    p3a=p3.get()
    p4a=p4.get()

    m=(float(m1a),float(m2a),float(m3a),float(m4a))
    x = np.arange(0.0, float(t1)*6, 0.01)
    y1 = float(qi1)/((1+float(b1)*float(Di1)*x)**(1/float(b1)))
    y2 = (float(p1a),float(p2a),float(p3a),float(p4a))
    fig, ax = plt.subplots()
    ax.plot(x, y1, color='tab:blue', label = 'Declinación')
    ax.plot(m, y2, color='tab:red', marker='o', dashes =[1,2], label = 'Datos')
    # ax.plot(x, y2, color='tab:red', dashes =[6,2], label = 'Datos')
    ax.axvline(x=float(t1), color="black", linestyle="--")

    legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

    ax.set(xlabel='time (días)', ylabel='q (bbl/D)',
       title='Grafico')
    ax.grid()
    fig.savefig("test.png")
    plt.show()
  
    

    


# Descripcion
display = Entry(root)
display.grid(row=1, column=2, sticky=W+E)
Di= Entry(root)
Di.grid(row=3, column=1, sticky=W+E)
b= Entry(root)
b.grid(row=4, column=1, sticky=W+E)
qi= Entry(root)
qi.grid(row=5, column=1, sticky=W+E)
q= Entry(root)
q.grid(row=6, column=1, sticky=W+E)
m1= Entry(root)
m1.grid(row=5, column=4, sticky=W+E)
p1= Entry(root)
p1.grid(row=5, column=5, sticky=W+E)
m2= Entry(root)
m2.grid(row=6, column=4, sticky=W+E)
p2= Entry(root)
p2.grid(row=6, column=5, sticky=W+E)
m3= Entry(root)
m3.grid(row=7, column=4, sticky=W+E)
p3= Entry(root)
p3.grid(row=7, column=5, sticky=W+E)
m4= Entry(root)
m4.grid(row=8, column=4, sticky=W+E)
p4= Entry(root)
p4.grid(row=8, column=5, sticky=W+E)




# Buttons
Label(root, text='         Datos     de ').grid(row=3, column=4, sticky=E)
Label(root, text='control    Petroleo').grid(row=3, column=5, sticky=W)
Label(root, text='Date(días)').grid(row=4, column=4, sticky=W+E)
Label(root, text='q (bbl/D)').grid(row=4, column=5, sticky=W+E)
Label(root, text='Datos 1').grid(row=5, column=3, sticky=W+E)
Label(root, text='Datos 2').grid(row=6, column=3, sticky=W+E)
Label(root, text='Datos 3').grid(row=7, column=3, sticky=W+E)
Label(root, text='Datos 4').grid(row=8, column=3, sticky=W+E)
Button(root, text='Δt: ').grid(row=1,columnspan=2, sticky=W+E)
Label(root, text='dias').grid(row=1, column=3, sticky=W+E)
Button(root, text='Di: ').grid(row=3, columnspan=1, sticky=W+E)
Label(root, text='Constante Declinación').grid(row=3, column=2, sticky=W+E)
Button(root, text='b: ').grid(row=4, column=0, sticky=W+E)
Label(root, text='entre 0 y 1').grid(row=4, column=2, sticky=W+E)
Button(root, text='qi: ').grid(row=5, column=0, sticky=W+E)
Label(root, text='Caudal Inicial').grid(row=5, column=2, sticky=W+E)
Button(root, text='q: ').grid(row=6, column=0, sticky=W+E)
Label(root, text='Caudal Target').grid(row=6, column=2, sticky=W+E)
Button(root, text='Clear', command=lambda: clear_display()).grid(rowspan=7, column=2,sticky=W+E)
Button(root, text='Calcular', command=lambda: Calculation()).grid(rowspan=7, column=2,sticky=W+E)
Button(root, text='Graph', command=lambda: Graf()).grid(rowspan=8, column=2,sticky=W+E)

root.mainloop()

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import requests
import numpy as np
import sys
import main
import lib


class MyWindow(QMainWindow):  # dziedzicze z klasy sluzacej do tworzenia okna glownego
    def __init__(self):
        super(MyWindow, self).__init__()  # uruchamiam parametry klasy z ktorej dziedzicze
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox_gen = QLineEdit(self)
        self.textbox_part = QLineEdit(self)
        self.textbox_posmin = QLineEdit(self)
        self.textbox_posmax = QLineEdit(self)

        self.button_pso = QtWidgets.QPushButton(self)
        self.button2 = QtWidgets.QPushButton(self)

        self.canvas1 = PlotCanvas(self, width=8, height=5)

        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.label_p = QtWidgets.QLabel(self)
        self.label_f = QtWidgets.QLabel(self)
        self.label_c = QtWidgets.QLabel(self)

        self.label_gen = QtWidgets.QLabel(self)
        self.label_part = QtWidgets.QLabel(self)
        self.label_posmin = QtWidgets.QLabel(self)
        self.label_posmax = QtWidgets.QLabel(self)

        self.setGeometry(0, 0, 1800, 1000)
        self.setStyleSheet("background-color: lightgray;")
        self.setWindowTitle('PSO Andrzej Tomek Paweł')
        self.initUI()

    def initUI(self):
        self.canvas1.move(900, 400)
        # self.canvas2.update1()

        self.button_pso.setText('start PSO optimization')
        self.button_pso.adjustSize()
        self.button_pso.move(1100, 250)
        self.button_pso.resize(400, 100)
        self.button_pso.setFont(QtGui.QFont('Arial', 24))
        self.button_pso.clicked.connect(self.button_pso_press)

        self.label1.setText('Create new fodder')
        self.label1.move(10, 10)
        self.label1.setFont(QtGui.QFont('Arial', 20))
        self.label1.adjustSize()

        self.label2.setText('PSO algorithm parameters')
        self.label2.move(1000, 10)
        self.label2.setFont(QtGui.QFont('Arial', 20))
        self.label2.adjustSize()

        self.label_p.setText('protein')
        self.label_p.move(10, 75)
        self.label_p.setFont(QtGui.QFont('Arial', 10))
        self.label_p.adjustSize()

        self.label_f.setText('fat')
        self.label_f.move(110, 75)
        self.label_f.setFont(QtGui.QFont('Arial', 10))
        self.label_f.adjustSize()

        self.label_c.setText('carbohydrates')
        self.label_c.move(210, 75)
        self.label_c.setFont(QtGui.QFont('Arial', 10))
        self.label_c.adjustSize()

        self.label_gen.setText('number of generations')
        self.label_gen.move(800, 175)
        self.label_gen.setFont(QtGui.QFont('Arial', 10))
        self.label_gen.adjustSize()

        self.label_part.setText('number of particles')
        self.label_part.move(1000, 175)
        self.label_part.setFont(QtGui.QFont('Arial', 10))
        self.label_part.adjustSize()

        self.label_posmin.setText('minimal position')
        self.label_posmin.move(1200, 175)
        self.label_posmin.setFont(QtGui.QFont('Arial', 10))
        self.label_posmin.adjustSize()

        self.label_posmax.setText('maximal position')
        self.label_posmax.move(1400, 175)
        self.label_posmax.setFont(QtGui.QFont('Arial', 10))
        self.label_posmax.adjustSize()

        self.textbox1.move(10, 100)
        self.textbox1.resize(70, 40)
        self.textbox1.setFont(QtGui.QFont('Arial', 20))

        self.textbox2.move(110, 100)
        self.textbox2.resize(70, 40)
        self.textbox2.setFont(QtGui.QFont('Arial', 20))

        self.textbox3.move(210, 100)
        self.textbox3.resize(70, 40)
        self.textbox3.setFont(QtGui.QFont('Arial', 20))

        self.textbox_gen.move(800, 200)
        self.textbox_gen.resize(70, 40)
        self.textbox_gen.setFont(QtGui.QFont('Arial', 20))
        self.textbox_gen.setText('150')

        self.textbox_part.move(1000, 200)
        self.textbox_part.resize(70, 40)
        self.textbox_part.setFont(QtGui.QFont('Arial', 20))
        self.textbox_part.setText('20')

        self.textbox_posmin.move(1200, 200)
        self.textbox_posmin.resize(70, 40)
        self.textbox_posmin.setFont(QtGui.QFont('Arial', 20))
        self.textbox_posmin.setText('10')

        self.textbox_posmax.move(1400, 200)
        self.textbox_posmax.resize(70, 40)
        self.textbox_posmax.setFont(QtGui.QFont('Arial', 20))
        self.textbox_posmax.setText('80')

        self.button2.setText('Confirm')
        self.button2.resize(100, 40)
        self.button2.move(330, 100)
        self.button2.setFont(QtGui.QFont('Arial', 14))

    def button_pso_press(self):
        generations = int(self.textbox_gen.text())
        population = int(self.textbox_gen.text())
        posmin = int(self.textbox_gen.text())
        posmax = int(self.textbox_gen.text())

        self.canvas1.update1(generations, population, posmin, posmax)
        self.canvas1.draw()  # draw to update plot in mainwindow


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        super(PlotCanvas, self).__init__(fig)
        self.setParent(parent)

        self.plot1()

    def plot1(self):
        y = main.cost_changes
        self.ax = self.figure.add_subplot(111)
        self.ax.set_ylabel('Total cost')
        self.ax.set_xlabel('Iterations')
        self.ax.ticklabel_format(useOffset=False)  # to prevent scientific notation
        self.ax.plot(y, 'k-')
        self.ax.grid()

    def update1(self, generations, population, posmin, posmax):
        # tutaj odpalam pso dla podanych wartosci w textboxach i od karmy ale to pozniej

        random_solution = lib.create_random_solution()
        random_cost = lib.compute_total_cost(random_solution)
        solution, day_particle_change = lib.pso(population, 5, posmin, posmax, generations, 0.001, random_solution,
                                                hamming=0)
        cost_changes = [random_cost]

        for gen in range(len(day_particle_change[0])):
            sort_iter = []
            for day in range(len(day_particle_change)):
                sort_iter.append(day_particle_change[day][gen])
            cost_changes.append(int(lib.compute_total_cost(sort_iter)))

        # TODO ogarnąć skąd biorą się te ogromne wartości od ~2-5 iteracji
        cost_changes = [95000 if i > 110000 else i for i in cost_changes]

        self.ax.clear()
        self.ax.plot(cost_changes, 'k-')
        self.ax.set_ylabel('Total cost')
        self.ax.set_xlabel('Iterations')
        self.ax.ticklabel_format(useOffset=False)
        self.ax.grid()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    # win.showFullScreen()
    win.show()
    sys.exit(app.exec_())


window()

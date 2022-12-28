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
        self.fodd_idx = 0

        self.listwidget_fodders = QtWidgets.QListWidget(self)

        self.tablewidget_solution = QtWidgets.QTableWidget(self)

        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox_gen = QLineEdit(self)
        self.textbox_part = QLineEdit(self)
        self.textbox_posmin = QLineEdit(self)
        self.textbox_posmax = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)
        self.textbox_idx_remove = QLineEdit(self)

        self.button_pso = QtWidgets.QPushButton(self)
        self.button2 = QtWidgets.QPushButton(self)
        self.button_remove = QtWidgets.QPushButton(self)

        self.canvas1 = PlotCanvas(self, width=8, height=5)

        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.label_p = QtWidgets.QLabel(self)
        self.label_f = QtWidgets.QLabel(self)
        self.label_c = QtWidgets.QLabel(self)
        self.label_pmin = QtWidgets.QLabel(self)
        self.label_pmax = QtWidgets.QLabel(self)
        self.label_remove = QtWidgets.QLabel(self)
        self.label_solution = QtWidgets.QLabel(self)

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

        self.button2.setText('Add')
        self.button2.resize(100, 40)
        self.button2.move(570, 100)
        self.button2.setFont(QtGui.QFont('Arial', 14))
        self.button2.clicked.connect(self.button2_press)

        self.button_remove.setText('Remove')
        self.button_remove.move(660, 255)
        self.button_remove.setFont(QtGui.QFont('Arial', 14))
        self.button_remove.adjustSize()
        self.button_remove.clicked.connect(self.button_remove_press)

        self.label_remove.setText('Choose index to remove')
        self.label_remove.move(570, 220)
        self.label_remove.setFont(QtGui.QFont('Arial', 12))
        self.label_remove.adjustSize()

        self.label1.setText('Create new fodder')
        self.label1.move(10, 10)
        self.label1.setFont(QtGui.QFont('Arial', 20))
        self.label1.adjustSize()

        self.label2.setText('PSO algorithm parameters')
        self.label2.move(1100, 10)
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

        self.label_pmin.setText('price min')
        self.label_pmin.move(340, 75)
        self.label_pmin.setFont(QtGui.QFont('Arial', 10))
        self.label_pmin.adjustSize()

        self.label_pmax.setText('price max')
        self.label_pmax.move(440, 75)
        self.label_pmax.setFont(QtGui.QFont('Arial', 10))
        self.label_pmax.adjustSize()

        self.label_gen.setText('number of generations')
        self.label_gen.move(1000, 175)
        self.label_gen.setFont(QtGui.QFont('Arial', 10))
        self.label_gen.adjustSize()

        self.label_part.setText('number of particles')
        self.label_part.move(1200, 175)
        self.label_part.setFont(QtGui.QFont('Arial', 10))
        self.label_part.adjustSize()

        self.label_posmin.setText('minimal position')
        self.label_posmin.move(1400, 175)
        self.label_posmin.setFont(QtGui.QFont('Arial', 10))
        self.label_posmin.adjustSize()

        self.label_posmax.setText('maximal position')
        self.label_posmax.move(1600, 175)
        self.label_posmax.setFont(QtGui.QFont('Arial', 10))
        self.label_posmax.adjustSize()

        self.label_solution.setText('Solution - amount of fodders to buy each day')
        self.label_solution.move(10, 500)
        self.label_solution.setFont(QtGui.QFont('Arial', 20))
        self.label_solution.adjustSize()

        self.textbox1.move(10, 100)
        self.textbox1.resize(70, 40)
        self.textbox1.setFont(QtGui.QFont('Arial', 20))
        self.textbox1.setText('10')

        self.textbox2.move(110, 100)
        self.textbox2.resize(70, 40)
        self.textbox2.setFont(QtGui.QFont('Arial', 20))
        self.textbox2.setText('10')

        self.textbox3.move(210, 100)
        self.textbox3.resize(70, 40)
        self.textbox3.setFont(QtGui.QFont('Arial', 20))
        self.textbox3.setText('10')

        self.textbox4.move(340, 100)
        self.textbox4.resize(70, 40)
        self.textbox4.setFont(QtGui.QFont('Arial', 20))
        self.textbox4.setText('10')

        self.textbox5.move(440, 100)
        self.textbox5.resize(70, 40)
        self.textbox5.setFont(QtGui.QFont('Arial', 20))
        self.textbox5.setText('20')

        self.textbox_gen.move(1000, 200)
        self.textbox_gen.resize(70, 40)
        self.textbox_gen.setFont(QtGui.QFont('Arial', 20))
        self.textbox_gen.setText('150')

        self.textbox_part.move(1200, 200)
        self.textbox_part.resize(70, 40)
        self.textbox_part.setFont(QtGui.QFont('Arial', 20))
        self.textbox_part.setText('20')

        self.textbox_posmin.move(1400, 200)
        self.textbox_posmin.resize(70, 40)
        self.textbox_posmin.setFont(QtGui.QFont('Arial', 20))
        self.textbox_posmin.setText('10')

        self.textbox_posmax.move(1600, 200)
        self.textbox_posmax.resize(70, 40)
        self.textbox_posmax.setFont(QtGui.QFont('Arial', 20))
        self.textbox_posmax.setText('80')

        self.textbox_idx_remove.move(570, 250)
        self.textbox_idx_remove.resize(70, 40)
        self.textbox_idx_remove.setFont(QtGui.QFont('Arial', 20))
        self.textbox_idx_remove.setText('0')

        self.listwidget_fodders.move(10, 150)
        self.listwidget_fodders.resize(500, 300)
        self.listwidget_fodders.setFont(QtGui.QFont('Arial', 12))
        for i in lib.fodders:
            self.listwidget_fodders.addItem(f'{self.fodd_idx} fodder:  protein={i.protein},  fat={i.fat},  '
                                            f'carbohydrates={i.carbohydrates}')
            self.fodd_idx += 1

        self.tablewidget_solution.move(10, 550)
        self.tablewidget_solution.resize(700, 400)
        self.tablewidget_solution.setFont(QtGui.QFont('Arial', 12))
        self.tablewidget_solution.setRowCount(31)
        self.tablewidget_solution.setColumnCount(len(lib.fodders) + 1)
        self.tablewidget_solution.setItem(0, 0, QtWidgets.QTableWidgetItem('Day'))
        for i in range(1, 31):
            self.tablewidget_solution.setItem(i, 0, QtWidgets.QTableWidgetItem(f'{i}'))
        self.tablewidget_solution.resizeColumnsToContents()


    def button_pso_press(self):
        generations = int(self.textbox_gen.text())
        population = int(self.textbox_gen.text())
        posmin = int(self.textbox_gen.text())
        posmax = int(self.textbox_gen.text())

        random_solution = lib.create_random_solution(lib.fodders)
        random_cost = lib.compute_total_cost(random_solution)
        solution, day_particle_change = lib.pso(population, lib.fodders, posmin, posmax, generations, 0.001,
                                                random_solution,
                                                hamming=0)
        cost_changes = [random_cost]

        for gen in range(len(day_particle_change[0])):
            sort_iter = []
            for day in range(len(day_particle_change)):
                sort_iter.append(day_particle_change[day][gen])
            cost_changes.append(int(lib.compute_total_cost(sort_iter)))

        self.canvas1.update1(cost_changes)
        self.canvas1.draw()  # draw to update plot in mainwindow

        self.tablewidget_solution.setColumnCount(len(lib.fodders) + 1)
        for i in range(1, len(lib.fodders) + 1):
            self.tablewidget_solution.setItem(0, i, QtWidgets.QTableWidgetItem(f'fodder_{i-1}'))
        for idx_sol, elem in enumerate(solution):
            for ix, f in enumerate(elem):
                row = idx_sol + 1
                col = ix + 1
                self.tablewidget_solution.setItem(row, col, QtWidgets.QTableWidgetItem(f'{f}'))
        self.tablewidget_solution.resizeColumnsToContents()

    def button2_press(self):
        protein = int(self.textbox1.text())
        fat = int(self.textbox2.text())
        carbohydrates = int(self.textbox3.text())
        posmin = int(self.textbox4.text())
        posmax = int(self.textbox5.text())

        lib.create_new_fodder(protein, fat, carbohydrates, posmin, posmax)
        self.listwidget_fodders.addItem(f'{self.fodd_idx} fodder:  protein={protein},  fat={fat},  carbohydrates={carbohydrates}')
        self.fodd_idx += 1
        print(lib.fodders)

    def update_index(self):
        self.listwidget_fodders.clear()
        for i in lib.fodders:
            self.listwidget_fodders.addItem(
                f'{self.fodd_idx} fodder:  protein={i.protein},  fat={i.fat},  carbohydrates={i.carbohydrates}')
            self.fodd_idx += 1

    def button_remove_press(self):
        index = int(self.textbox_idx_remove.text())
        lib.fodders.pop(index)
        self.listwidget_fodders.takeItem(index)
        self.fodd_idx = 0
        self.update_index()





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

    def update1(self, cost_changes):
        # tutaj odpalam pso dla podanych wartosci w textboxach i od karmy ale to pozniej



        # TODO ogarnąć skąd biorą się te ogromne wartości od ~2-5 iteracji
        #cost_changes = [95000 if i > 110000 else i for i in cost_changes]

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

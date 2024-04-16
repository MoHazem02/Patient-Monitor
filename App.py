from serial import *
from PyQt5 import QtCore
import pandas as pd, numpy as np

class ApplicationManager:
    def __init__(self,UI):
        self.ui = UI
        #self.serial_port = Serial('COM4', 9600)
        self.sum = 0
        self.count = 0
        self.X_Points_Plotted = 0
        self.sample_rate = 44100
        #self.start()
        self.load_signal()
           
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500) 

    def read_data(self):
        temprature = int(self.serial_port.readline().decode('utf-8').strip())

        if temprature:
            self.sum += temprature
            self.count += 1
            average = (self.sum // self.count)

            self.ui.current_temp_LCD.display(temprature)
            self.ui.average_temp_LCD.display(average)

    def load_signal(self):
        data_header_rows = ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"]
        data = pd.read_csv("Omar's ECG.txt", delim_whitespace=True, usecols=data_header_rows)
        self.Y_coordinates = data["A2"]
        self.X_Coordinates = list(np.arange(len(self.Y_coordinates)))
        self.plot_signal()

    def plot_signal(self):
        self.data_line = self.ui.ECG_Graph.plot(self.X_Coordinates[:1], self.Y_coordinates[:1], pen='w')
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.X_Points_Plotted += 1
        self.ui.ECG_Graph.setLimits(xMin=0, xMax=float('inf'))
        self.data_line.setData(self.X_Coordinates[0 : self.X_Points_Plotted + 1], self.Y_coordinates[0 : self.X_Points_Plotted + 1]) 
        self.ui.spectrogram.canvas.plot_spectrogram(self.Y_coordinates[0 : self.X_Points_Plotted + 1], self.sample_rate)

        if self.X_Points_Plotted < len(self.Y_coordinates):
            self.ui.ECG_Graph.getViewBox().setXRange(max(self.X_Coordinates[0: self.X_Points_Plotted + 1]) - 100, max(self.X_Coordinates[0: self.X_Points_Plotted + 1]))
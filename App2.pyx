from serial import Serial
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber
from pyqtgraph import PlotWidget
import pandas as pd
import numpy as np
import soundfile as sf
import sounddevice as sd

# Declare types for variables and functions
ctypedef long long int64_t

cdef class ApplicationManager:
    cdef object ui
    cdef object serial_port
    cdef int sum
    cdef int count
    cdef int X_Points_Plotted
    cdef int sample_rate
    cdef object timer
    cdef object data
    cdef object Y_coordinates
    cdef object X_Coordinates
    cdef object data_line

    def __init__(self, UI):
        self.ui = UI
        # self.serial_port = Serial('COM4', 9600)
        self.sum = 0
        self.count = 0
        self.X_Points_Plotted = 0
        self.sample_rate = 44100
        # self.start()
        self.load_signal()
        self.data, self.sample_rate = sf.read("alert_sound.wav")

    cpdef start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500)

    cpdef read_data(self):
        cdef int temprature
        temprature = int(self.serial_port.readline().decode('utf-8').strip())
        cdef int average

        if temprature:
            self.sum += temprature
            self.count += 1
            average = (self.sum // self.count)

            self.ui.current_temp_LCD.display(temprature)
            self.ui.average_temp_LCD.display(average)

            if temprature > 38:
                self.show_warning()
            else:
                self.hide_warning()

    cpdef load_signal(self):
        cdef list data_header_rows
        data_header_rows = ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"]
        cdef object data
        data = pd.read_csv("Omar's ECG.txt", delim_whitespace=True, usecols=data_header_rows)
        self.Y_coordinates = data["A2"]
        self.X_Coordinates = list(np.arange(len(self.Y_coordinates)))
        self.plot_signal()

    cpdef plot_signal(self):
        self.data_line = self.ui.ECG_Graph.plot(self.X_Coordinates[:1], self.Y_coordinates[:1], pen='w')
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    cpdef update_plot_data(self):
        self.X_Points_Plotted += 1
        self.ui.ECG_Graph.setLimits(xMin=0, xMax=float('inf'))
        self.data_line.setData(self.X_Coordinates[0: self.X_Points_Plotted + 1], self.Y_coordinates[0: self.X_Points_Plotted + 1])
        self.ui.spectrogram.canvas.plot_spectrogram(self.Y_coordinates[0: self.X_Points_Plotted + 1], self.sample_rate)

        if self.X_Points_Plotted < len(self.Y_coordinates):
            self.ui.ECG_Graph.getViewBox().setXRange(max(self.X_Coordinates[0: self.X_Points_Plotted + 1]) - 100, max(self.X_Coordinates[0: self.X_Points_Plotted + 1]))

    cpdef show_warning(self):
        sd.play(self.data, self.sample_rate)
        self.ui.status_ok_label.setVisible(False)
        self.ui.status_warning_label.setVisible(True)

    cpdef hide_warning(self):
        sd.stop()
        self.ui.status_warning_label.setVisible(False)
        self.ui.status_ok_label.setVisible(True)

# imports
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import pyvisa
import time
from pyvisa.resources import MessageBasedResource

class DC2200_controller(QDialog):
    def __init__(self):
        super(DC2200_controller, self).__init__()
        loadUi('DC2200_brightness.ui', self)
        self.run_button.clicked.connect(self.run())

        # get the LED resource loaded.
        rm = pyvisa.ResourceManager()
        self.DC2200 = rm.open_resource('USB0::0x1313::0x80C8::M00585134::INSTR', resource_pyclass=MessageBasedResource)
        self.DC2200.timeout = 20

        # general set up and warm up of the LED
        self.DC2200.write("SOUR:MOD 2")
        self.DC2200.write("OUTP:STAT ON")
        self.DC2200.write("SOUR:CBR:BRIG 100")



    @pyqtSlot()
    def run(self):
        pre_illumination_time = int(self.DarkTimeLine.currentText())  # in seconds
        illumination_time = int(self.IlluminationTimeLine.currentText())   # illumination time in seconds
        time_between_samples = int(self.StepSizeLine.currentText())   # in seconds
        step_size = illumination_time // time_between_samples

        # general set up and warm up of the LED
        self.DC2200.write("SOUR:MOD 2")
        self.DC2200.write("OUTP:STAT ON")
        self.DC2200.write("SOUR:CBR:BRIG 100")

        # this takes place during the dark illumination phase.
        time.sleep(pre_illumination_time)

        # creates a list for each step that will be taking place
        steps = [i for i in range(0, int(step_size))]

        # for loop to go through each step.
        for s in steps:
            if s == 0:
                v_step = 100 // step_size # first step will be the smallest step.
            else:
                v_step += 100 // step_size # adds upwards until reaching 100.
            self.CurrentPercentLine.setText(v_step)
            inp = "SOUR:CBR:BRIG {}".format(v_step)
            self.DC2200.write(inp)
            time.sleep(time_between_samples)

        # is the reverse count also checked?
        if self.rev_Check.isChecked():
            for s in steps:
                if s == 0:
                    v_step = 100 # first step is always 100% brightness (%)
                else:
                    v_step -= 100 // step_size # steps in brightness intervals (%)
                self.CurrentPercentLine.setText(v_step)
                inp = "SOUR:CBR:BRIG {}".format(v_step) # string to be sent to DC2200 (%)
                self.DC2200.write(inp) # sends the string to the DC2200
                time.sleep(time_between_samples) # sleeps between changes (s)

        self.DC2200.write("OUTP:STAT OFF") # turns the LED off


app = QApplication(sys.argv)
widget = DC2200_controller()
widget.show()
sys.exit(app.exec_())
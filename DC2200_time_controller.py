import pyvisa
import time
from pyvisa.resources import MessageBasedResource

rm = pyvisa.ResourceManager()
DC2200 = rm.open_resource('USB0::0x1313::0x80C8::M00585134::INSTR', resource_pyclass=MessageBasedResource)
DC2200.timeout = 20

pre_illumination_time = 5  # in seconds
illumination_time = 60  # illumination time in seconds
time_between_samples = 15  # in seconds
step_size = illumination_time // time_between_samples
h_to_l = True

print(step_size)
DC2200.write("SOUR:MOD 2")
DC2200.write("OUTP:STAT ON")
DC2200.write("SOUR:CBR:BRIG 100")
time.sleep(pre_illumination_time)

steps = [i for i in range(0, int(step_size))]
for s in steps:
    if s == 0:
        v_step = 100 // step_size
    else:
        v_step += 100 // step_size
    print(v_step)
    inp = "SOUR:CBR:BRIG {}".format(v_step)
    DC2200.write(inp)
    time.sleep(time_between_samples)

if h_to_l == True:  # high to low sweep after low to high sweep
    for s in steps:
        if s == 0:
            v_step = 100
        else:
            v_step -= 100 // step_size
        print(v_step)
        inp = "SOUR:CBR:BRIG {}".format(v_step)
        DC2200.write(inp)
        time.sleep(time_between_samples)

DC2200.write("OUTP:STAT OFF")
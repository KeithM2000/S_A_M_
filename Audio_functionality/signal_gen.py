import numpy as np
from waves import Wave
import matplotlib.pyplot as plt

def create_sinusoid(freq, phase, amp, empty_wave: Wave, sweep = 1):
    Tp = empty_wave.time_step
    data_array = empty_wave.data
    elements = empty_wave.samples
    if sweep == 1:
        for i in range(elements):
            data_array[i] = np.sin(i*Tp*freq + phase)
    else:
        for i in range(elements):
            data_array[i] = np.sin(i*Tp*freq + phase)
            freq *= sweep
    data_array = amp * data_array

# total_samples = (time_ms/1000)*sampling_freq
# time_ms = sample*1000*period
def create_sawtooth(period_ms, amp, empty_wave: Wave, sweep = 1):
    period_ms_round = int(np.ceil(period_ms))
    Tp_ms_round = int(np.ceil(1000*empty_wave.time_step))
    wave_data = empty_wave.data
    if sweep == 1:
        for i in range(empty_wave.samples):
            wave_data[i] = amp*2*((((i*Tp_ms_round) % period_ms_round)/period_ms_round) - np.floor(0.5 + (((i*Tp_ms_round) % period_ms_round)/period_ms_round))) 
    else:
        for i in range(empty_wave.samples):
            wave_data[i] = amp*2*((((i*Tp_ms_round) % period_ms_round)/period_ms_round) - np.floor(0.5 + (((i*Tp_ms_round) % period_ms_round)/period_ms_round))) 
            period_ms = period_ms * sweep
            period_ms_round = int(np.ceil(period_ms))

def create_pwm_wave(empty_wave: Wave, duty_cycle, freq, amp = 1):
    period = 1/freq
    time_high = duty_cycle*period
    time_low = (period - time_high)
    Fs = empty_wave.Fs
    steps_high = int(np.floor(time_high*Fs))
    steps_low = int(np.floor(time_low*Fs))
    wave_data = empty_wave.data
    max_int = empty_wave.samples
    i = 0
    while i < max_int:
        a = 0
        while a < steps_high and i < max_int:
            wave_data[i] = 1
            a += 1
            i += 1
        b = 0
        while b < steps_low and i < max_int:
            wave_data[i] = -1
            b += 1
            i += 1
    wave_data *= amp
        
def create_triangle(empty_wave: Wave, rise_time, fall_time, amp = 1):
    Fs = empty_wave.Fs
    rise_time /=1000
    fall_time /=1000
    steps_rise = int(np.floor(rise_time*Fs))
    steps_fall = int(np.floor(fall_time*Fs))
    delta_y_rise = 2/steps_rise
    delta_y_fall = 2/steps_fall
    wave_data = empty_wave.data
    max_int = empty_wave.samples
    i = 0
    while i < max_int:
        a = 0
        mag = -1
        while a < steps_rise and i < max_int:
            wave_data[i] = mag
            mag += delta_y_rise
            a += 1
            i += 1
        b = 0
        mag = 1
        while b < steps_fall and i < max_int:
            wave_data[i] = mag
            mag -= delta_y_fall
            b += 1
            i += 1
    wave_data *= amp


#a = Wave(2000, 40000)
#create_sinusoid(1, 0.5, 2, a, 1.000075)

#b = Wave(10000, 1000)
#create_sawtooth(1000, 2, b, 0.9999)

#c = Wave(2000, 40000)
#create_pwm_wave(c, 0.25, 5)
#c.data += 1

d = Wave(2000, 40000)
create_triangle(d, 20, 80)
plt.plot(d.data)
plt.show()

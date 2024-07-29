import numpy as np


class Wave:
    def __init__(self, length, sampling_frequency):
        self.samples = int(np.floor(length*sampling_frequency/1000))
        self.data = np.zeros(self.samples)
        self.time_step = 1/sampling_frequency
        self.Fs = sampling_frequency
        self.tag = ""
    
    def sum_wave(self, starting_index, input_wave):
        post_ = self.samples - starting_index
        if input_wave.samples > post_:
            res_len = starting_index + input_wave.samples
            end_sum = self.samples - 1
        else:
            res_len = self.samples
            end_sum = starting_index + input_wave.samples - 1
        
        sum_wave = Wave(res_len*1000, self.Fs)
        sum_arr = sum_wave.data
        for i in range(starting_index):
            sum_arr[i] = self.data[i]
        k = 0
        for i in range(starting_index, end_sum + 1):
            sum_arr[i] = self.data[i] + input_wave.data[k]
            k+=1
        l = end_sum + 1
        while k < input_wave.samples:
            sum_arr[l] = input_wave.data[k]
            k+=1
            l+=1
        while l < self.samples:
            sum_arr[l] = self.data[l]
            l+=1
        return sum_wave


a = Wave(5000, 1)
a.data[0] = 3
a.data[1] = 2
a.data[2] = 1
a.data[3] = 4
a.data[4] = 1
b = Wave(5000, 1)
b.data[0] = 5
b.data[1] = 5
b.data[2] = 6
b.data[3] = 2
b.data[4] = 1
print(a.data)

c = a.sum_wave(2, b)
print(c.data)


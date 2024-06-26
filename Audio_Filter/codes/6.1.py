import soundfile as sf
from scipy import signal, fft
import numpy as np
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    num_channels = input_signal.shape[1] if input_signal.ndim > 1 else 1
    output_signal = np.zeros_like(input_signal)
    
    for i in range(num_channels):
        X = fft.fft(input_signal[:, i]) if num_channels > 1 else fft.fft(input_signal)
        w = np.linspace(0, 1, len(X) + 1)
        W = np.exp(2j * np.pi * w[:-1])
        B = np.abs(np.polyval(b, W)) ** 2
        A = np.abs(np.polyval(a, W)) ** 2
        Y = B * (1 / A) * X
        output_signal[:, i] = np.real(fft.ifft(Y)) if num_channels > 1 else np.real(fft.ifft(Y))[0]
    
    return output_signal

# Read .wav file 
input_signal, fs = sf.read('audi.wav') 
print(len(input_signal))
np.savetxt("in.txt", input_signal)

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 1kHz
cutoff_freq = 4000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal, padlen=1)
print(sampl_freq)
op1 = myfiltfilt(b, a, input_signal)
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'blue', label='Output by built-in function')
plt.plot(x_plt[1000:10000], op1[1000:10000], 'red', label='Output by custom function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("Audio_Filter_verf.png")


import os
import wave
import numpy as np
import matplotlib.pyplot as plt

def create_waveform_signal_graph(load, save):
    wav = wave.load(load)
    freq = wav.getframerate()
    n_samples = wav.getnframes()
    t = n_samples/freq
    time = np.linspace(0, t, n_samples)
    signal = wav.readframes(n_samples)
    signal = np.frombuffer(signal, dtype=np.int16)
    signal = signal/signal.max()
    if wav.getchannels() == 2:
        left_channel = signal[0::2]
        right_channel = signal[1::2]
        fig, axs = plt.subplots(2)
        axs[0].plot(time, left_channel, 'k-')
        axs[1].plot(time, right_channel, 'k-')
        for ax in axs.flat:
            ax.set(xlabel="Czas [s]", ylabel="Amplituda", xlim=(0, t), ylim=(-1, 1))
        plt.savefig(os.path.join(save, 'sygnal_przed_obrobka.png'))
        plt.show()
    else:
        plt.figure(figsize=(10,5))
        plt.plot(time, signal, 'k-')
        plt.xlabel("Czas [s]")
        plt.ylabel("Amplituda")
        plt.xlim(0, t)
        plt.ylim(-1, 1)
        plt.savefig(os.path.join(save, 'sygnal_po_obrobce.png'))
        plt.show()


if __name__ == "__main__":

    load_path = r'D:\Folders\_Engineering_Thesis\Papers\Images\Eurasian Teal-44.wav'
    save_path = r'D:\Folders\_Engineering_Thesis\Papers\Images'

    create_waveform_signal_graph(load_path, save_path)

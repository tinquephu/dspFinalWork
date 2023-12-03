import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

def load_vowels(filename):
    sr, signal = wavfile.read(filename)
    vowels = {
        'A': signal[4500:12500],
        'E': signal[14000:23000],
        'I': signal[23000:34000],
        'O': signal[33000:46000],
        'U': signal[46000:58000]
    }
    return vowels, sr

def extract_formants(signal, sr):
    from praatio import pitch_and_formant

    formant_times, formant_values = pitch_and_formant.getFormantValues(signal, sr)
    return formant_values[:, :3]

def analyze_vowels(vowels, sr):
    formants = {vowel: extract_formants(signal, sr) for vowel, signal in vowels.items()}

    fig, axs = plt.subplots(5, 1, sharex=True, sharey=True)

    for i, (vowel, freqs) in enumerate(formants.items()):
        freqs = np.mean(freqs, axis=0)
        axs[i].plot(freqs)
        axs[i].set_title(vowel)

    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

def generate_spectrogram(signal, sr):
    f, t, Sxx = spectrogram(signal, sr)
    plt.pcolormesh(t, f, Sxx, shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram')
    plt.show()

# Select one speaker for analysis
speaker_number = 1

for speaker in range(1, 5):
    if speaker != speaker_number:
        continue

    vowels, sr = load_vowels(f'NguyenAmHuanLuyen-16k/spk{speaker:02d}.wav')

    for vowel, signal in vowels.items():
        print(f'\n{vowel} of speaker {speaker}')

        generate_spectrogram(signal, sr)

        formants = extract_formants(signal, sr)
        formants = np.mean(formants, axis=0)

        print(f'Formant Frequencies (F1, F2, F3): {formants}')
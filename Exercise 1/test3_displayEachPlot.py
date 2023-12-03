import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram_with_formants(audio_file, formants, formant_labels):
    plt.figure(figsize=(12, 8))
    y, sr = librosa.load(audio_file)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    for formant, label in zip(formants, formant_labels):
        plt.axhline(y=formant, color='r', linestyle='--', linewidth=2)
        plt.text(0.5, formant, f'{label}', color='white', fontsize=10, ha='center', va='bottom')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram with Formants')
    plt.tight_layout()
    plt.show()

formant_labels = ['F1', 'F2', 'F3']

# Display the spectrogram with formants and labels for vowel /a/
formant_a = [805, 1541, 3673]
audio_file_path_a = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\a.wav'
plot_spectrogram_with_formants(audio_file_path_a, formant_a, formant_labels)

# Display the spectrogram with formants and labels for vowel /e/
formant_e = [502, 2140, 3574]
audio_file_path_e = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\e.wav'
plot_spectrogram_with_formants(audio_file_path_e, formant_e, formant_labels)

# Display the spectrogram with formants and labels for vowel /i/
formant_i = [390, 2130, 3566]
audio_file_path_i = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\i.wav'
plot_spectrogram_with_formants(audio_file_path_i, formant_i, formant_labels)

# Display the spectrogram with formants and labels for vowel /o/
formant_o = [764, 1192, 3474]
audio_file_path_o = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\o.wav'
plot_spectrogram_with_formants(audio_file_path_o, formant_o, formant_labels)

# Display the spectrogram with formants and labels for vowel /u/
formant_u = [428, 771, 3509]
audio_file_path_u = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\u.wav'
plot_spectrogram_with_formants(audio_file_path_u, formant_u, formant_labels)
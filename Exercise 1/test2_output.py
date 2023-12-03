import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram_with_formants(audio_file, formants, formant_labels):
    # Đọc file âm thanh
    y, sr = librosa.load(audio_file)

    # Tính spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Vẽ spectrogram
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')

    # Đánh dấu formants trên spectrogram
    for formant, label in zip(formants, formant_labels):
        plt.axhline(y=formant, color='r', linestyle='--', linewidth=2)
        plt.text(0.5, formant, f'{label}', color='white', fontsize=10, ha='center', va='bottom')

    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram with Formants')

formant_labels = ['F1', 'F2', 'F3']

# Bộ 3 tần số formant nguyên âm /a/
formant_a = [805, 1541, 3673]
audio_file_path_a = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\a.wav'
plot_spectrogram_with_formants(audio_file_path_a, formant_a, formant_labels)

# Bộ 3 tần số formant nguyên âm /e/
formant_e = [502, 2140, 3574]
audio_file_path_e = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\e.wav'
plot_spectrogram_with_formants(audio_file_path_e, formant_e, formant_labels)

# Bộ 3 tần số formant nguyên âm /i/
formant_i = [390, 2130, 3566]
audio_file_path_i = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\i.wav'
plot_spectrogram_with_formants(audio_file_path_i, formant_i, formant_labels)

# Bộ 3 tần số formant nguyên âm /o/
formant_o = [764, 1192, 3474]
audio_file_path_o = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\o.wav'
plot_spectrogram_with_formants(audio_file_path_o, formant_o, formant_labels)

# Bộ 3 tần số formant nguyên âm /u/
formant_u = [428, 771, 3509]
audio_file_path_u = 'signals\\NguyenAmHuanLuyen-16k\\25MLM\\u.wav'
plot_spectrogram_with_formants(audio_file_path_u, formant_u, formant_labels)

plt.show()
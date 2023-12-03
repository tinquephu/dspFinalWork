import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram_with_formants(audio_file, formants):
    # Đọc file âm thanh
    y, sr = librosa.load(audio_file)

    # Tính spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Vẽ spectrogram
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')

    # Đánh dấu formants trên spectrogram
    for formant in formants:
        plt.axhline(y=formant, color='r', linestyle='--', linewidth=2)

    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram with Formants')
    plt.show()

# Bộ 3 tần số formant cho ví dụ (cần thay đổi dựa trên dữ liệu thực tế)
formants_example = [500, 1500, 2500]

# Đường dẫn đến file âm thanh
audio_file_path = 'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Digital signal Processing\\6. Group Work\\signals\\NguyenAmKiemThu-16k\\02FVA\\a.wav'

# Hiển thị spectrogram với formants
plot_spectrogram_with_formants(audio_file_path, formants_example)

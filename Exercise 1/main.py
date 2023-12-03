from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import numpy as np

# Hàm để vẽ wideband spectrogram
def plot_spectrogram(audio_data, title):
    _, _, Sxx, _ = spectrogram(audio_data.samples, audio_data.frame_rate)
    plt.pcolormesh(Sxx)
    plt.title(title)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

# Hàm để đo tần số formant
def measure_formants(audio_data, vowels):
    formants = []

    for vowel in vowels:
        print(f"Đo tần số formant cho nguyên âm {vowel}")
        play(audio_data)
        start_time = float(input("Nhập thời điểm bắt đầu (giây): "))
        end_time = float(input("Nhập thời điểm kết thúc (giây): "))

        # Lấy mẫu tín hiệu trong khoảng thời gian đã nhập
        segment = audio_data[int(start_time * 1000):int(end_time * 1000)]

        # Vẽ spectrogram của đoạn tín hiệu vừa lấy
        plot_spectrogram(segment, f"Spectrogram - {vowel}")

        # Đo tần số formant thủ công hoặc sử dụng đoạn thẳng nằm ngang
        f1 = float(input("Nhập tần số formant F1: "))
        f2 = float(input("Nhập tần số formant F2: "))
        f3 = float(input("Nhập tần số formant F3: "))

        formants.append({'Vowel': vowel, 'F1': f1, 'F2': f2, 'F3': f3})

    return formants

# Thay đổi đường dẫn và tên file âm thanh tương ứng
audio_file_paths = [
    'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Signal Processing\\6. Group Work\\signals\\NguyenAmHuanLuyen-16k\\23MTL\\a.wav',
    'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Signal Processing\\6. Group Work\\signals\\NguyenAmHuanLuyen-16k\\23MTL\\e.wav',
    'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Signal Processing\\6. Group Work\\signals\\NguyenAmHuanLuyen-16k\\23MTL\\i.wav',
    'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Signal Processing\\6. Group Work\\signals\\NguyenAmHuanLuyen-16k\\23MTL\\o.wav',
    'D:\\Dinh Tin 2023 - 2024\\3rd_year\\5. Signal Processing\\6. Group Work\\signals\\NguyenAmHuanLuyen-16k\\23MTL\\u.wav'
]

vowels_to_measure = ['a', 'e', 'i', 'o', 'u']

formants_data = []

for audio_file_path in audio_file_paths:
    audio_data = AudioSegment.from_wav(audio_file_path)
    plot_spectrogram(audio_data, f"Wideband Spectrogram - {audio_file_path}")

    formants_data.append({
        'Speaker': audio_file_path.split('_')[2],
        'Formants': measure_formants(audio_data, vowels_to_measure)
    })

# In ra bảng dữ liệu formants
for data in formants_data:
    print(f"\nDữ liệu formants cho người nói {data['Speaker']}:")
    print("{:<6} {:<6} {:<6} {:<6}".format('Vowel', 'F1', 'F2', 'F3'))
    for formant in data['Formants']:
        print("{:<6} {:<6} {:<6} {:<6}".format(
            formant['Vowel'], formant['F1'], formant['F2'], formant['F3']
        ))

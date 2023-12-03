import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import random

# Đường dẫn đến thư mục chứa file âm thanh huấn luyện
training_folder = "signals\\NguyenAmHuanLuyen-16k"

# Lấy danh sách tất cả các file trong thư mục
all_files = os.listdir(training_folder)

# Chọn ngẫu nhiên 4 người từ tổng số 21 người
selected_people = random.sample(all_files, 4)

# Lặp qua từng người được chọn
for person in selected_people:
    person_folder = os.path.join(training_folder, person)

    # Lấy danh sách tất cả các file của người này
    person_files = os.listdir(person_folder)

    # Chọn ngẫu nhiên một file từ danh sách
    selected_file = random.choice(person_files)

    # Đường dẫn đầy đủ đến file âm thanh
    file_path = os.path.join(person_folder, selected_file)

    # Sử dụng Librosa để đọc file âm thanh
    y, sr = librosa.load(file_path)

    # Tính toán phổ băng rộng
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Hiển thị ảnh phổ băng rộng
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram for {} - {}'.format(person, selected_file))
    plt.show()

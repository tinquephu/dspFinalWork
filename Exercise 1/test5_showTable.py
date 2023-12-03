# Display 3D-plot of 5 Vietnamese vowels with formant frequencies, x-axis: F1, y-axis: F2, z-axis: F3

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


# Bộ 3 tần số formant nguyên âm /a/
formant_a = [805, 1541, 3673]

# Bộ 3 tần số formant nguyên âm /e/
formant_e = [502, 2140, 3574]

# Bộ 3 tần số formant nguyên âm /i/
formant_i = [390, 2130, 3566]

# Bộ 3 tần số formant nguyên âm /o/
formant_o = [764, 1192, 3474]

# Bộ 3 tần số formant nguyên âm /u/
formant_u = [428, 771, 3509]

# Tạo bảng
# plt.figure(figsize=(12, 8))
# plt.axis('off')
# plt.table(cellText=[formant_a, formant_e, formant_i, formant_o, formant_u],
#           rowLabels=['/a/', '/e/', '/i/', '/o/', '/u/'],
#           colLabels=['F1', 'F2', 'F3'],
#           loc='center')
# plt.show()

# Tạo 3D-plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(formant_a[0], formant_a[1], formant_a[2], c='r', marker='o', label='/a/')
ax.scatter(formant_e[0], formant_e[1], formant_e[2], c='g', marker='o', label='/e/')
ax.scatter(formant_i[0], formant_i[1], formant_i[2], c='b', marker='o', label='/i/')
ax.scatter(formant_o[0], formant_o[1], formant_o[2], c='y', marker='o', label='/o/')
ax.scatter(formant_u[0], formant_u[1], formant_u[2], c='m', marker='o', label='/u/')
ax.set_xlabel('F1')
ax.set_ylabel('F2')
ax.set_zlabel('F3')
ax.legend()
plt.show()



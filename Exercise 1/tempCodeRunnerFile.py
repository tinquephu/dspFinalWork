    # Đánh dấu formants trên spectrogram
    for formant, label in zip(formants, formant_labels):
        plt.axhline(y=formant, color='r', linestyle='--', linewidth=2)
        plt.text(0.5, formant, f'{label}', color='r', fontsize=10, ha='center', va='bottom')

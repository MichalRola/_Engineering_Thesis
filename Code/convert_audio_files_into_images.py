import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import gc


def change_suffix(file_name):
    """
    change_suffix zmienia rozszerzenie nazwy pliku na png.
    :param file_name: Nazwa pliku z rozszerzeniem wave (np. Mallard-0.wav)
    :return: img_name: Nazwa pliku z rozszerzeniem png (np. Mallard-0.png)
    """
    # Podzielenie nazwy pliku na części w miejscach wystąpienia kropek
    parts = file_name.split(".")
    # Wybranie odpowiedniej części nazwy oraz nadanie rozszerzenia png
    img_name = parts[len(parts) - 2] + ".png"
    return img_name


def audio_to_melspectrogram(file_name):
    """
    audio_to_melspectrogram przekształca plik audio na melspectrogram.
    Uzupełnia również melspectrogramy o ciszę, jeśli plik jest zbyt krótki.
    :param file_name:
    :return: melspectogram:
    """
    audio_timeseries, sampling_rate = librosa.load(file_name, sr=None)
    if len(audio_timeseries) < 44077:
        padding = 44077 - len(audio_timeseries)
        audio_timeseries = np.pad(audio_timeseries, (0, padding), 'constant')
    melspectrogram = librosa.feature.melspectrogram(y=audio_timeseries, sr=sampling_rate)
    melspectrogram = librosa.power_to_db(melspectrogram).astype(np.float32)
    return melspectrogram


def save_image_from_sound(save_path, load_path, file_name):
    new_file_name = change_suffix(file_name)
    melspectrogram = audio_to_melspectrogram(os.path.join(load_path, file_name))

    plt.imsave(os.path.join(save_path, new_file_name), melspectrogram, cmap='gray')
    del melspectrogram
    gc.collect()


def main():
    load_path = r"D:\Folders\_Engineering_Thesis\Done_Done"
    save_path = r"D:\Folders\_Engineering_Thesis\Melspectrograms"

    try:
        os.mkdir(save_path)
    except OSError:
        print("Melspectrograms folder already exists.")
        return 1

    for file_name in os.listdir(load_path):
        save_image_from_sound(save_path, load_path, file_name)


if __name__ == "__main__":
    main()

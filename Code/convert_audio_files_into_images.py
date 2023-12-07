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


def audio_to_melspectrogram(path, htk_on=0):
    """
    audio_to_melspectrogram przekształca plik audio na melspectrogram.
    Uzupełnia również melspectrogramy o ciszę, jeśli plik jest zbyt krótki.
    :param path:
    :param htk_on:
    :return: melspectogram:
    """
    audio_timeseries, sampling_rate = librosa.load(path, sr=None)
    n_of_samples = 44200
    if len(audio_timeseries) < n_of_samples:
        padding = n_of_samples - len(audio_timeseries)
        audio_timeseries = np.pad(audio_timeseries, (0, padding), 'constant')
    melspectrogram = librosa.feature.melspectrogram(y=audio_timeseries, sr=sampling_rate, htk=htk_on)
    melspectrogram = librosa.power_to_db(melspectrogram).astype(np.float32)
    return melspectrogram


def save_image_from_sound(load, save, file_name, htk_on=0):
    new_file_name = change_suffix(file_name)
    melspectrogram = audio_to_melspectrogram(os.path.join(load, file_name), htk_on)

    # plt.imshow(melspectrogram, interpolation='nearest')
    # plt.savefig(os.path.join(save, new_file_name))

    plt.imsave(os.path.join(save, new_file_name), melspectrogram, cmap='gray')
    del melspectrogram
    gc.collect()


if __name__ == "__main__":
    load_path_training = r"D:\Folders\_Engineering_Thesis\Data\Done_Done_Training"
    load_path_testing = r"D:\Folders\_Engineering_Thesis\Data\Done_Done_Testing"

    mel_type = r"Slaney"

    save_path_training = r"D:\Folders\_Engineering_Thesis\Data\\" + mel_type + "_Training_Melspectrograms"
    save_path_testing = r"D:\Folders\_Engineering_Thesis\Data\\" + mel_type + "_Testing_Melspectrograms"

    try:
        os.mkdir(save_path_training)
    except OSError:
        print("Melspectrograms folder already exists.")

    try:
        os.mkdir(save_path_testing)
    except OSError:
        print("Melspectrograms folder already exists.")

    for file in os.listdir(load_path_training):
        save_image_from_sound(load_path_training, save_path_training, file, 0)

    for file in os.listdir(load_path_testing):
        save_image_from_sound(load_path_testing, save_path_testing, file, 0)

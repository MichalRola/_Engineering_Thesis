import os
import numpy as np
import matplotlib.pyplot as plt


def create_image_dataset(load, save):
    dataset = []
    labels = []
    # Pętla po obrazach przedstawiających Mel Spektrogramy
    for file_name in os.listdir(load):
        # Kod odpowiedzialny za wydzielenie  nazwy gatunku ptaka na nagraniu
        parts = file_name.split("-")
        if parts[len(parts) - 3].count('.') == 0:
            species_name = parts[len(parts) - 3] + "-" + parts[len(parts) - 2]
        else:
            species_name = parts[len(parts) - 2]

        # Wczytanie obrazu oraz ograniczenie jego wymiarów do 1
        image = plt.imread(os.path.join(load, file_name))[:, :, 1]

        # Dodawania wczytanych danych do odpowiednich list
        dataset.append([image])
        labels.append([species_name])

    # Zapis kompletnych list do odpowiedniego folderu
    np.save(os.path.join(save, 'features_training_HTK'), np.array(dataset))
    np.save(os.path.join(save, 'labels_training_HTK'), np.array(labels))


if __name__ == "__main__":
    # Ścieżka zawierająca obrazy Mel Spektrogramów
    load_path = r"D:\Folders\_Engineering_Thesis\Data\Melspectrograms_Training_HTK"
    # Docelowa ścieżka zapisu zbiorów danych
    save_path = r"D:\Folders\_Engineering_Thesis\Data\Datasets"
    
    # Sprawdzenie czy już istnieje folder zapisu
    try:
        os.mkdir(save_path)
    except OSError:
        print("Datasets folder already exists.")

    create_image_dataset(load_path, save_path)

import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Ścieżka zawierająca obrazy Mel Spektrogramów
    load_path = r"D:\Folders\_Engineering_Thesis\Melspectrograms"
    # Docelowa ścieżka zapisu zbiorów danych
    save_path = r"D:\Folders\_Engineering_Thesis\Datasets"

    # Sprawdzenie czy już istnieje folder zapisu
    try:
        os.mkdir(save_path)
    except OSError:
        print("Datasets folder already exists.")

    dataset = []
    labels = []
    # Pętla po obrazach przedstawiających Mel Spektrogramy
    for file_name in os.listdir(load_path):
        # Kod odpowiedzialny za wydzielenie  nazwy gatunku ptaka na nagraniu
        parts = file_name.split("-")
        if parts[len(parts) - 3].count('.') == 0:
            species_name = parts[len(parts) - 3] + "-" + parts[len(parts) - 2]
        else:
            species_name = parts[len(parts) - 2]

        # Wczytanie obrazu oraz ograniczenie jego wymiarów do 1
        image = plt.imread(os.path.join(load_path, file_name))[:, :, 1]

        # Dodawania wczytanych danych do odpowiednich list
        labels.append([species_name])
        dataset.append([image])

    # Zapis kompletnych list do odpowiedniego folderu
    np.save(os.path.join(save_path, 'labels'), np.array(labels))
    np.save(os.path.join(save_path, 'features'), np.array(dataset))


if __name__ == "__main__":
    main()

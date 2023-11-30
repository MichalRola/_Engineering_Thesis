import os
import shutil


def numerate_data(load, save, species_folders):
    for species_folder in species_folders:
        i = 0
        for file_name in os.listdir(os.path.join(load, species_folder)):
            parts = file_name.split("-")
            if parts[len(parts)-3].strip().isnumeric() is False:
                new_species_name = (parts[len(parts) - 3].strip() + "-" + parts[len(parts) - 2].strip() + "-"
                                    + str(i) + ".wav")
            else:
                new_species_name = parts[len(parts) - 2].strip() + "-" + str(i) + ".wav"
            i += 1

            shutil.copy(os.path.join(load, species_folder, file_name), os.path.join(save, new_species_name))


if __name__ == "__main__":
    load_path = r"D:\Folders\_Engineering_Thesis\Data\Done_Mono_Training"
    save_path = r"D:\Folders\_Engineering_Thesis\Data\Done_Done_Training"
    species = ["Common Crane", "Common Cuckoo", "Corn Crake", "Eurasian Stone-curlew", "Eurasian Teal",
                       "Mallard", "Mandarin Duck", "Spotted Crake", "Stock Dove", "Tundra Swan"]

    try:
        os.mkdir(save_path)
    except OSError:
        print("Done_Done folder already exists.")

    numerate_data(load_path, save_path, species)

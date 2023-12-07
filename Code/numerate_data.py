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
    load_path_training = r"D:\Folders\_Engineering_Thesis\Data\Done_Mono_Training"
    load_path_testing = r"D:\Folders\_Engineering_Thesis\Data\Done_Mono_Testing"

    save_path_training = r"D:\Folders\_Engineering_Thesis\Data\Done_Done_Training"
    save_path_testing = r"D:\Folders\_Engineering_Thesis\Data\Done_Done_Testing"

    species = ["Common Crane", "Common Cuckoo", "Corn Crake", "Eurasian Stone-curlew", "Eurasian Teal",
                       "Mallard", "Mandarin Duck", "Spotted Crake", "Stock Dove", "Tundra Swan"]

    try:
        os.mkdir(save_path_training)
    except OSError:
        print("Done_Done folder already exists.")

    try:
        os.mkdir(save_path_testing)
    except OSError:
        print("Done_Done folder already exists.")

    numerate_data(load_path_training, save_path_training, species)
    numerate_data(load_path_testing, save_path_testing, species)

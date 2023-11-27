import os
import shutil


def main():
    load_path = r"D:\Folders\_Engineering_Thesis\Done_Mono"
    save_path = r"D:\Folders\_Engineering_Thesis\Done_Done"
    species_folders = ["Common Crane", "Common Cuckoo", "Corn Crake", "Eurasian Stone-curlew", "Eurasian Teal",
                       "Mallard", "Mandarin Duck", "Spotted Crake", "Stock Dove", "Tundra Swan"]

    try:
        os.mkdir(save_path)
    except OSError:
        print("Done_Done folder already exists.")

    for species_folder in species_folders:
        i = 0
        for file_name in os.listdir(os.path.join(load_path, species_folder)):
            parts = file_name.split("-")
            if parts[len(parts)-3].strip().isnumeric() is False:
                new_species_name = (parts[len(parts) - 3].strip() + "-" + parts[len(parts) - 2].strip() + "-"
                                    + str(i) + ".wav")
            else:
                new_species_name = parts[len(parts) - 2].strip() + "-" + str(i) + ".wav"
            i += 1

            shutil.copy(os.path.join(load_path, species_folder, file_name), os.path.join(save_path, new_species_name))


if __name__ == "__main__":
    main()

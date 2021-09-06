import numpy as np
import cv2
import os


def determine_padding(location):
    if location == "1":
        padding_top_bottom = (0, 4096)
        padding_left_right = (0, 4096)
    elif location == "2":
        padding_top_bottom = (0, 4096)
        padding_left_right = (4096, 0)
    elif location == "3":
        padding_top_bottom = (4096, 0)
        padding_left_right = (0, 4096)
    elif location == "4":
        padding_top_bottom = (4096, 0)
        padding_left_right = (4096, 0)
    elif location == "5":
        padding_top_bottom = (2048, 2048)
        padding_left_right = (2048, 2048)
    else:
        padding_top_bottom = (0, 0)
        padding_left_right = (0, 0)
    return padding_top_bottom, padding_left_right


def rescale(image, location):
    padding_top_bottom, padding_left_right = determine_padding(location)
    if len(image.shape) == 3:
        out_image = np.pad(image, (padding_top_bottom, padding_left_right, (0, 0)), mode='constant', constant_values=(0, 0))
    else:
        out_image = np.pad(image, (padding_top_bottom, padding_left_right), mode='constant',
                           constant_values=(0, 0))
    return out_image


def menu():
    print("Where would you like the old map to be located in the new map?")
    print("1: In the upper left corner")
    print("2: In the upper right corner")
    print("3: In the lower left corner")
    print("4: In the lower right corner")
    print("5: In the middle")
    selection = input("Please enter your selection: ")
    return selection


def find_all_files():
    file_list = []
    for file in os.listdir('./png/'):
        if file.endswith(".png"):
            file_list.append(os.path.join("./png/", file))
    return file_list


def do_image_work(filename, location):
    input_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    return_image = rescale(input_image, location)
    return return_image


def main():
    selection = menu()
    file_list = find_all_files()
    print(file_list)
    for file in file_list:
        new_image = do_image_work(file, selection)
        cv2.imwrite(file, new_image)


if __name__ == "__main__":
    main()

import numpy as np
import cv2


def rescale(image, location):
    out_image = np.pad(image, ((0,4096), (0, 4096), (0, 0)), mode='constant', constant_values=(0, 0))
    return out_image


def menu():
    print("Where would you like the old map files to be located?")
    print("1: In the upper left corner")
    print("2: In the upper right corner")
    print("3: In the lower left corner")
    print("4: In the lower right corner")
    print("5: In the middle")
    selection = input("Please enter your selection: ")
    return selection


def main():
        selection = menu()

        image = cv2.imread('testdem.png', cv2.IMREAD_UNCHANGED)
        newImage = rescale(image)
        cv2.imwrite('newdem.png', newImage)


if __name__ == "__main__":
    main()

# import site
"""
for k, v in {"cv2":"cv", "numpy":"np", "glob":"glob"}.items():
    globals()[v]=__import__(k)
"""
import cv2 as cv
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# constants are defined below
input_size_to_use = (32, 32)
color_range = 255.0
path_2_dataset = r"C:\Users\User04\Desktop\re_wrriten_code\data_set\*\*"
number_of_stars_in_path = list(path_2_dataset).count("*")


# funtions are defined below


def return_label_from_path(currecnt_iteration_path):
    return currecnt_iteration_path.split("\\")[number_of_stars_in_path * -1]

def print_the_percantage(n_total,currecnt_n):
    print(f"{currecnt_n+1} out of {n_total} were processed")

def load_data():
    all_data = []
    all_labels = []
    le = LabelEncoder()
    number_of_all = glob.glob(path_2_dataset).__len__()
    last_percantage = 0

    for i, item in enumerate(glob.glob(path_2_dataset)):
        # this loop doenst even iterate throught anything then its empty
        img = cv.imread(item)
        img = cv.resize(img, input_size_to_use)
        img = img / color_range
        img = img.flatten()
        all_data.append(img)
        label = return_label_from_path(item)
        all_labels.append(label)
        print_this = f"{i + 1}/{number_of_all}"


        if i % (number_of_all//10) == 0:
            print_the_percantage(number_of_all, i)
            continue

    print_the_percantage(number_of_all, i)








    all_data = np.array(all_data)
    X_train, X_test, y_train, y_test = train_test_split(all_data, all_labels, test_size=0.2, random_state=42)
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    return X_train, X_test, y_train, y_test


"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# what code actually does happens below
if __name__ == "__main__":
    load_data()

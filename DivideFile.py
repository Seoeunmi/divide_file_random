import os
import random
import shutil

train_folder_path = "C:/Users/deluv/Desktop/VCTK_dataset/train"
test_folder_path = "C:/Users/deluv/Desktop/VCTK_dataset/test"
valid_folder_path = "C:/Users/deluv/Desktop/VCTK_dataset/valid"

folder_list = os.listdir(train_folder_path)
sampling_rate = 16000

for folder in folder_list:
    train_path = os.path.join(train_folder_path, folder)
    test_path = os.path.join(test_folder_path, folder)
    valid_path = os.path.join(valid_folder_path, folder)

    file_list = os.listdir(train_path)
    num_all_file = len(file_list)
    num_test_file = num_all_file // 10
    num_valid_file = (num_all_file - num_test_file) // 10

    random_list = random.sample(file_list, num_test_file + num_valid_file)
    cnt = 0
    for file in random_list:
        train_file_path = os.path.join(train_path, file)
        cnt += 1
        if cnt <= num_test_file:
            test_file_path = os.path.join(test_path, file)
            os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
            shutil.copy(train_file_path, test_file_path)
        else:
            valid_file_path = os.path.join(valid_path, file)
            os.makedirs(os.path.dirname(valid_file_path), exist_ok=True)
            shutil.copy(train_file_path, valid_file_path)
        os.remove(train_file_path)


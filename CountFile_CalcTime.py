import os
import librosa


def read_audio_file(file_path, sampling_rate=None, different_sampling_rate_detect=False):
    if different_sampling_rate_detect:
        x, sr = librosa.load(file_path, sr=None)
        if sr != sampling_rate:
            raise Exception(f"Different sampling rate detected ! -> {file_path} ({sr})")
    else:
        x, _ = librosa.load(file_path, sr=sampling_rate)
    return x


def second_to_dhms_string(second, second_round=True):
    d, left = divmod(second, 86400)
    h, left = divmod(left, 3600)
    m, s = divmod(left, 60)
    str = ""
    d, h, m, s = int(d), int(h), int(m), int(s) if second_round else int(s) + second - int(second)
    if d!=0:
        str+=f"{d:d}d "
    if h!=0 or d!=0:
        str+=f"{h:02d}h "
    if m!=0 or h!=0 or d!=0:
        str+=f"{m:02d}m "
    str += f"{s:02d}s" if second_round else f"{s:2.2f}s"
    return str


def count_file(folder_path):
    folder_list = os.listdir(folder_path)
    for folder in folder_list:
        path = os.path.join(folder_path, folder)
        file_list = os.listdir(path)
        print(len(file_list))


def calc_file_time(folder_path, sampling_rate):
    folder_list = os.listdir(folder_path)
    total_sample_length = 0
    for folder in folder_list:
        path = os.path.join(folder_path, folder)
        file_list = os.listdir(path)

        sample_length = 0
        for file in file_list:
            file_path = os.path.join(path, file)
            _, ext = os.path.splitext(file_path)
            if ext != '.wav':
                continue
            sample_length += len(read_audio_file(file_path, sampling_rate=sampling_rate))
        print(second_to_dhms_string(sample_length / sampling_rate))
        total_sample_length += sample_length
    print(second_to_dhms_string(total_sample_length / sampling_rate))


folder_path = "C:/Users/deluv/Desktop/VCTK_dataset/train"
count_file(folder_path)
calc_file_time(folder_path, 16000)
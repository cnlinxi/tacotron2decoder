# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 9:01
# @Author  : MengnanChen
# @FileName: select_audio_samples.py
# @Software: PyCharm

import random


def select_samples_with_metadata(input_path, output_path, sample_size=300):
    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        lines = fin.readlines()
        lines = random.sample(lines, k=sample_size)
        fout.writelines(lines)


if __name__ == '__main__':
    input_path = '../training_data/train.txt'
    output_path = '../training_data/train2.txt'
    select_samples_with_metadata(input_path=input_path, output_path=output_path)

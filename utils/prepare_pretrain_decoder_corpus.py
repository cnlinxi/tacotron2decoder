# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 16:12
# @Author  : MengnanChen
# @FileName: prepare_pretrain_decoder_corpus.py
# @Software: PyCharm

import os
import shutil
import glob

from tqdm import tqdm


def generate_corpus(input_dirs, output_path, all_wavs_dir='wavs'):
    output_dir = os.path.dirname(output_path)
    all_wavs_dir = os.path.join(output_dir, all_wavs_dir)
    os.makedirs(all_wavs_dir, exist_ok=True)
    all_wav_names = set()
    with open(output_path, 'wb') as fout:
        for input_dir in input_dirs:
            # input_dir: wav dir
            print('process {}...'.format(input_dir))
            wavs = glob.glob(os.path.join(input_dir, '*.wav'))
            for wav in tqdm(wavs):
                basename = os.path.basename(wav)
                index = 0
                while basename in all_wav_names:
                    basename = '{}_{}.wav'.format(basename[:-4], index)
                    index += 1
                all_wav_names.add(basename)
                shutil.copyfile(wav, os.path.join(all_wavs_dir, basename))
                fout.write('{}|t\n'.format(basename[:-4]).encode('utf-8'))


if __name__ == '__main__':
    # wav input dirs
    input_dirs = ['../decoder_pretrain_wavs/1', '../decoder_pretrain_wavs/2', '../decoder_pretrain_wavs/3']
    output_path = '../decoder_pretrain_wavs/decoder_pretrain.corpus'
    generate_corpus(input_dirs, output_path)

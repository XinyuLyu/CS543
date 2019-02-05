import numpy as np
import scipy.io as scio
import os
from keras.preprocessing import sequence
from sklearn import preprocessing

audio_path = ''
output_path = ''

num = 2199

def get_mat_data(path):
    res = []
    i = 0
    while i < num:
        files = os.listdir(path + str(i) + '/')
        sent = []
        for file in files:
            tmp = scio.loadmat(path + str(i) + '/' + file)
            tmp = tmp['z1']
            tmp = sequence.pad_sequences(tmp, padding='post', truncating='post', dtype='float32', maxlen=535)
            # print(tmp.shape)
            tmp = tmp.transpose()
            sent.append(tmp)
        print(np.array(sent).shape)
        res.append(sent)
        i += 1
    #res = np.array(res)
    return res


def output_mat_data(path, res):
    i = 0
    while i < num:
        scio.savemat(path+str(i)+".mat", {'z1': res[i]})
        i += 1


res = get_mat_data(audio_path)
output_mat_data(output_path, res)
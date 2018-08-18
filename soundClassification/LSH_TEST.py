"""
 스크립트 구동 방법
 $ export FLASK_APP=urban_sound_classifier.py
 $ flask run
 ... Running on http://127.0.0.1:5000
"""

import numpy as np
import tensorflow as tf
import librosa
from flask import Flask, request
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def extract_feature(file_name):
    print("extract")
    print(file_name)
    X, sample_rate = librosa.load(file_name)
    print("load")
    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
    return mfccs,chroma,mel,contrast,tonnetz

# 텐서플로우 모델 생성
n_dim = 193
n_classes = 4
n_hidden_units_one = 300
n_hidden_units_two = 200
n_hidden_units_three = 100
sd = 1 / np.sqrt(n_dim)



X = tf.placeholder(tf.float32,[None,n_dim])
Y = tf.placeholder(tf.float32,[None,n_classes])

W_1 = tf.Variable(tf.random_normal([n_dim, n_hidden_units_one], mean=0, stddev=sd), name="w1")
b_1 = tf.Variable(tf.random_normal([n_hidden_units_one], mean=0, stddev=sd), name="b1")
h_1 = tf.nn.sigmoid(tf.matmul(X, W_1) + b_1)

W_2 = tf.Variable(tf.random_normal([n_hidden_units_one, n_hidden_units_two], mean=0, stddev=sd), name="w2")
b_2 = tf.Variable(tf.random_normal([n_hidden_units_two], mean=0, stddev=sd), name="b2")
h_2 = tf.nn.tanh(tf.matmul(h_1, W_2) + b_2)

W_3 = tf.Variable(tf.random_normal([n_hidden_units_two, n_hidden_units_three], mean=0, stddev=sd), name="w3")
b_3 = tf.Variable(tf.random_normal([n_hidden_units_three], mean=0, stddev=sd), name="b3")
h_3 = tf.nn.sigmoid(tf.matmul(h_2, W_3) + b_3)

W = tf.Variable(tf.random_normal([n_hidden_units_three, n_classes], mean=0, stddev=sd), name="w")
b = tf.Variable(tf.random_normal([n_classes], mean = 0, stddev=sd), name="b")
print("b is"+str(b))
z = tf.matmul(h_3, W) + b
y_sigmoid = tf.nn.sigmoid(z)
y_ = tf.nn.softmax(z)

init = tf.global_variables_initializer()

# 모델 파라메타 로드
saver = tf.train.Saver(tf.trainable_variables())
sess = tf.Session()
sess.run(init)
saver.restore(sess, 'Newmodel_LSH.ckpt')


def analyzingFile(filename):
#if __name__ == "__main__":
    mfccs, chroma, mel, contrast,tonnetz = extract_feature(filename)
    x_data = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
    y_hat, sigmoid = sess.run([y_, y_sigmoid], feed_dict={X: x_data.reshape(1,-1)})
    index = np.argmax(y_hat)

    if index ==0:
       return 0
    elif index==1:
        return 1
    elif index==2:
        return 2
    elif index == 3:
        return 3


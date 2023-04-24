from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import Embedding
from keras.layers import LSTM
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn import preprocessing
from method_text_encode import  method_text_encode
from method_generate_data_save import  generate_data_save
import os
import datetime
import tensorflow as tf
from tensorflow.keras.layers import GRU
from tensorflow.keras.layers import TimeDistributed



from tensorflow.keras.optimizers import Adam





methods = method_text_encode()
methods.encode_main()
train_x = methods.label_all_phrases_x
train_y = methods.label_all_phrases_y
lengthwords = methods.LengthWords
embedingcount = methods.EmbedingCount
maxseqtext = methods.MaxSeqText


model = keras.Sequential()

model.add(Embedding(lengthwords, embedingcount, input_length=maxseqtext))
model.add(LSTM(128, use_bias=True, recurrent_dropout=0.2, return_sequences=True, activation="tanh"))
model.add(LSTM(64, use_bias=True, recurrent_dropout=0.2, activation="tanh"))
model.add(Dropout(0.2))
model.add(Dense(maxseqtext, activation="relu", use_bias=True))
model.compile(optimizer=Adam(0.0001), loss='mse', metrics=['mae'])



#Adadelta

train_x_ = []
train_y_ = []
for iter in range(len(train_x)):
    for i in range(len(train_x[iter])):
        train_x_.append(train_x[iter][i])
        train_y_.append(train_y[iter][i])
history = model.fit(train_x_, train_y_, epochs=1000 ,verbose=2)

model.save('for_save/model_save_1.h5')
def matrix_transform(matrix):
     return [[i] for i in matrix]

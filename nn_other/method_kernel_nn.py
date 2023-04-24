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


class main_methods:
    def __init__(self, system_bool, id_):
        self.system_bool = system_bool
        if id_ != 0:
            data_give_config = {
                "text":f"../Users_data/{id_}_data.json",
                "words":"dataset_words/dataset.json",
            }
        else:
            data_give_config = 0
        methods = method_text_encode(data_give_config)
        self.methods = methods
        self.methods.encode_main()
        self.train_x = methods.label_all_phrases_x
        self.train_y = methods.label_all_phrases_y
        self.lengthwords = methods.LengthWords
        self.embedingcount = methods.EmbedingCount
        self.maxseqtext = methods.MaxSeqText
        #directory = "for_save"
        #files = os.listdir(directory)
        #num = len(files)
        #model = keras.Sequential()
        #model.add(Embedding(self.lengthwords, self.embedingcount, input_length = self.maxseqtext))
        #model.add(LSTM(500, activation='tanh', return_sequences=True))
        #model.add(LSTM(250, activation='tanh', return_sequences=True))
        #model.add(SimpleRNN(80, activation='tanh'))
        #model.add(Dropout(0.3))
        #model.add(Dense(self.maxseqtext, activation='relu'))
        #model.compile(optimizer='sgd', loss='mse', metrics=['mae'])

        with open("for_save/about_use", "r", encoding="utf-8") as f:
            name_ = f.read()
            f.close()
        model = keras.models.load_model("for_save/"+name_)
        #model.load_weights("for_save/"+name_)
        self.model = model


    def predict_method(self, text):
        matrix_text = self.methods.text_in_matrix(text)
        results = self.methods.matrix_decode_in_text(self.model.predict(matrix_text))
        return results


    def __log_method(self):
        directory = "log_nn"
        files = os.listdir(directory)
        num = len(files)
        with open("log_nn/log_nn_"+str(num)+".log","r",encoding="utf-8") as f:
            data_ = f.read()
            f.close()

        if len(data_.split("\n")) > 20:
            num+=1
            data_ = ""

        data_text = ""

        for iter in range(len(self.log_loss)):
            data_text += f"loss - {self.log_loss[iter]} metrics - {self.log_metrics[iter]}\n"


        data_+=data_text

        with open("log_nn/log_nn_"+str(num)+".log","w",encoding="utf-8") as f:
            f.write(data_)
            f.close()


    def __save_method_nn(self):
        directory = "for_save"
        files = os.listdir(directory)
        num = len(files)+1
        name = f"model_save_{num}.h5"
        self.model.save("for_save/"+name)
        if self.system_bool == True:
            with open("for_save/about_use", "w", encoding="utf-8") as f:
                f.write(name)
                f.close()

    def train_method(self):
        data_loss = []
        data_metrics = []
        train_x = self.train_x
        train_y = self.train_y
        def matrix_transform(matrix):
            return [[i] for i in matrix]
        train_x_ = []
        train_y_ = []
        for iter in range(len(train_x)):
            for i in range(len(train_x[iter])):
                train_x_.append(train_x[iter][i])
                train_y_.append(train_y[iter][i])
        history = self.model.fit(train_x_, train_y_, epochs=100 ,verbose=2)
        #for cycle in range(2):
        #    for iter in range(len(train_x)-1):
        #        for i in range(len(train_x[iter])-1):
        #            for iter_ in range(2):
        #                history = model.fit([train_x[iter][i]], [train_y[iter][i]], batch_size=32 ,epochs=150 ,verbose=2, shuffle=True)
        data_loss.append(np.mean(history.history['loss']))
        data_metrics.append(np.mean(history.history['mae']))
        self.log_loss = data_loss
        self.log_metrics = data_metrics
        self.__log_method()
        self.__save_method_nn()

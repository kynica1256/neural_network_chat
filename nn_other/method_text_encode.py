import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing

#from data_give_method import give_data

import json



class method_text_encode:
    all_words = [None]
    all_phrases = []
    MaxCount = 10
    MaxSeq = 7

    range_data = []
    range_coef = 0.1


    EmbedingCount = 30
    MaxSeqText = 10

    label_all_phrases_x = []
    label_all_phrases_y = []


    config = {
        "text":"dataset_text/dataset.json",
        "words":"dataset_words/dataset.json"
    }


    def __init__(self, config_):
        #self.matrix_words = preprocessing.normalize(np.random.randint(100, size=(1,len(self.all_words))))
        self.config = config_ if config_ != 0 else self.config
        self.__parse_main_words()
        self.__parse_main_phrase()
        label_encoder = preprocessing.LabelEncoder()
        self.label_encode_words = sorted(label_encoder.fit_transform(self.all_words).tolist())
        self.LengthWords = len(self.all_words)
        self.encode_label = self.__run_encode_label()
        #self.matrix_words = np.random.randint(100, size=(1,len(self.all_words)))
        #self.train_x = np.zeros((1, self.MaxSeq, self.MaxCount)).astype(np.float32)
        #self.train_y = np.zeros((1, self.MaxSeq, self.MaxCount)).astype(np.float32)


    def encode_main(self):
        np.random.seed(1)
        data_x = []
        data_y = []
        for iter in self.all_phrases:
            data_x_1 = []
            data_y_1 = []
            for x, y in iter.items():
                data_x_2 = []
                data_y_2 = []
                words_x = list(filter(None, x.split(" ")))
                for i in range(len(words_x)):
                    if words_x[i] in self.all_words:
                        index_ = self.all_words.index(words_x[i])
                        data_x_2.append(self.label_encode_words[index_])
                words_y = list(filter(None, y.split(" ")))
                for i in range(len(words_y)):
                    if words_y[i] in self.all_words:
                        index_ = self.all_words.index(words_y[i])
                        data_y_2.append(self.label_encode_words[index_])
                data_x_1.append(data_x_2)
                data_y_1.append(data_y_2)
            data_x.append(data_x_1)
            data_y.append(data_y_1)
        self.label_all_phrases_x.append(data_x)
        self.label_all_phrases_y.append(data_y)
        self.label_all_phrases_x = self.label_all_phrases_x[0]
        self.label_all_phrases_y = self.label_all_phrases_y[0]
        self.__y_encode()


    def __y_encode(self):
        work_data_y = self.label_all_phrases_y
        work_data_y_ = self.label_all_phrases_y
        cicle_data = work_data_y
        length_cicle_data = len(cicle_data)
        for i in range(len(cicle_data)):
            cicle_data_1 = cicle_data[i]
            length_cicle_data_1 = len(cicle_data_1)
            for i_ in range(len(cicle_data_1)):
                cicle_data_2 = cicle_data_1[i_]
                length_cycle_data_2 = len(cicle_data_2)
                for iter in range(len(cicle_data_2)):
                    id_word = cicle_data_2[iter]
                    index_word = self.label_encode_words.index(id_word)
                    total = self.encode_label[index_word]
                    #total = index_word/1000
                    total = self.__choice_range(index_word)
                    work_data_y_[i][i_][iter] = total
        self.label_all_phrases_y = work_data_y_
        #print(self.label_all_phrases_x)
        self.__add_zero()

    def __add_zero(self):

        func_transform_data = lambda data, coef: [*data, *[0]*coef]


        def mini_method_1(data_cycle_1):
            mini_data = []
            for iter in range(len(data_cycle_1)):
                data_cycle_2 = data_cycle_1[iter]
                zero_data = self.MaxSeqText - len(data_cycle_2)
                mini_data.append(func_transform_data(data_cycle_2, zero_data))
            return mini_data


        new_data_y = []
        new_data_x = []


        for i in range(len(self.label_all_phrases_x)):
            data_cycle_y_1 = self.label_all_phrases_y[i]
            data_cycle_x_1 = self.label_all_phrases_x[i]
            new_data_y.append(mini_method_1(data_cycle_y_1))
            new_data_x.append(mini_method_1(data_cycle_x_1))

        self.label_all_phrases_y = new_data_y
        self.label_all_phrases_x = new_data_x



    #######
    def __mini_encode(self, text):
        data_ = np.zeros((1, self.MaxCount))
        #if position >= len(text):
        #    return data_[0].tolist()
        mini_text = list(filter(None, text.split(" ")))
        for iter in range(len(mini_text)):
            symbols = mini_text[iter].lower()
            if symbols in self.all_words:
                index_ = self.all_words.index(symbols)
                data_[0][iter] = self.label_encode_words[index_]
        return data_[0].tolist()
    #######

    def matrix_decode_in_text(self, matrix):
        def for_filter(a):
            if a == 0:
                return False
            else:
                return True
        matrix_ = list(filter(for_filter, matrix[0]))
        string_matrix = [str(i) for i in matrix_]
        total_string = ""
        for iter in string_matrix:
            try:
                #index_ = int(float(iter[0:5])*1000)
                index_ = self.__decode_range(iter)
                total_string += self.all_words[index_]+" "
            except Exception as e:
                pass
        return total_string


    def __parse_main_words(self):
        #method = give_data()
        data_ = self.__check_method("words")

        for a,b in data_.items():
            if type(b[0]) == list:
                for iter in b:
                    for i in iter:
                        self.all_words.append(i)
            else:
                for i in b:
                    self.all_words.append(i)

    def __parse_main_phrase(self):
        #method = give_data()
        data_ = self.__check_method("text")
        for a, b in data_.items():
            self.all_phrases.append(b)




    def __run_encode_label(self):
        all_ = []
        for i in self.label_encode_words:
            total_ = self.__choice_range(i)
            all_.append(total_)
        return all_



    def __choice_range(self, index_):
        range_data_ = self.range_data
        k = self.range_coef
        if index_ == 0:
            num_total = k/2
            start_par = 0
        else:
            start_par = range_data_[index_-1][1]
            num_total = range_data_[index_-1][1]+(k/2)
        finish_par = start_par+k
        self.range_data.append([start_par, finish_par])
        return num_total



    def __decode_range(self, num):
        num = float(num)
        range_data_ = self.range_data
        for i in range(len(range_data_)):
            data_0 = range_data_[i][0]
            data_1 = range_data_[i][1]
            if num > data_0 and num < data_1:
                index_ = i
                break
        return index_

    def __check_method(self, type_):
        with open(self.config[type_], "r", encoding="utf-8") as f:
            result = json.loads(f.read())
            f.close()
        return result


    def text_in_matrix(self, text):
        #main_data = np.array([[ self.__mini_encode(i, text) for i in range(self.MaxSeq) ]])
        main_data = [self.__mini_encode(text)]
        #for i in range(self.MaxSeq):
        #    d = data[0][i]
        #    for iter in range(self.MaxCount-len(d)):
        return main_data

    def change_train_data(self, id_):
        self.config = {
            "text":f"../Users_data/{id_}_data.json",
            "words":"dataset_words/dataset.json",
        }

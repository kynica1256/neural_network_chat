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


methods = method_text_encode(0)
methods.encode_main()
train_x = methods.label_all_phrases_x
train_y = methods.label_all_phrases_y
#maxcount = methods.MaxCount
#maxseq = methods.MaxSeq
lengthwords = methods.LengthWords
embedingcount = methods.EmbedingCount
maxseqtext = methods.MaxSeqText


with open("for_save/about_use", "r", encoding="utf-8") as f:
    name_ = f.read()
    f.close()
model = keras.models.load_model("for_save/"+name_)

total = model.predict(methods.text_in_matrix("приветик"))
print(total)
print(methods.matrix_decode_in_text(total))

total = model.predict(methods.text_in_matrix("как дела ?"))
print(total)
print(methods.matrix_decode_in_text(total))

total = model.predict(methods.text_in_matrix("пока"))
print(total)
print(methods.matrix_decode_in_text(total))

#total = model.predict(methods.text_in_matrix("пока"))
#print(total)
#print(methods.matrix_decode_in_text(total))

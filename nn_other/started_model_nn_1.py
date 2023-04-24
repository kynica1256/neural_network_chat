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
#label_encoder = preprocessing.LabelEncoder()
#token_words = label_encoder.fit_transform(methods.all_words)
#print(token_words)


from tensorflow.keras.optimizers import Nadam



#tokenizer.fit_on_texts(methods.)



methods = method_text_encode(0)
methods.encode_main()
train_x = methods.label_all_phrases_x
train_y = methods.label_all_phrases_y
#maxcount = methods.MaxCount
#maxseq = methods.MaxSeq
lengthwords = methods.LengthWords
embedingcount = methods.EmbedingCount
maxseqtext = methods.MaxSeqText
#pred_data = methods.text_in_matrix(["Привет как дела ?", "у меня нормально", "пока"])
#print(methods.text_in_matrix(["Привет"]))
#print(pred_data[0])

print(train_x)
print(train_y)


print(lengthwords)
print(embedingcount)
print(maxseqtext)

#sys.exit()



#train_x = np.random.random([32, 10, 8]).astype(np.float32)
#train_y = np.random.random([32, 10, 10]).astype(np.float32)




model = keras.Sequential()

model.add(Embedding(lengthwords, embedingcount, input_length=maxseqtext))
#model.add(Dropout(0.2))
#model.add(GRU(128, recurrent_activation="tanh", activation="sigmoid", use_bias=True, recurrent_dropout=0.3, return_sequences=True))
model.add(LSTM(128, use_bias=True, recurrent_dropout=0.2, return_sequences=True, activation="tanh"))
model.add(LSTM(64, use_bias=True, recurrent_dropout=0.2, activation="tanh"))
#model.add(LSTM(128, use_bias=True))
#model.add(LSTM(64, return_sequences=True, activation="tanh"))
#model.add(LSTM(64, activation="tanh"))
model.add(Dropout(0.2))
#model.add(SimpleRNN(32, use_bias=True, recurrent_dropout=0.3, activation="tanh"))
#model.add(LSTM(64, use_bias=True, recurrent_dropout=0.3))
#model.add(LSTM(32))
#model.add(BatchNormalization())
model.add(Dense(maxseqtext, activation="relu", use_bias=True))
model.compile(optimizer=Adam(0.0001), loss='mse', metrics=['mae'])
#Adam(0.0001)
"""
model.add(LSTM(256, return_sequences=True, input_shape=(10, 8)))
model.add(LSTM(128))
#model.add(SimpleRNN(38, return_sequences=True, activation='relu'))
model.add(Dense(10, activation='relu'))
#model.add(Dense(50, activation='tanh', input_shape=(100,)))
#model.add(Dense(10, activation='sigmoid', input_shape=(10,)))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
#history = model.fit(train_x, train_y, epochs=100, batch_size=30, verbose=2)
print(model.summary())




a = np.random.random([1, 10, 8]).astype(np.float32)
print(a)
total = model.predict(a)
print(total)
total = model.predict(np.random.random([1, 10, 8]).astype(np.float32))
print(total)
total = model.predict(np.random.random([1, 10, 8]).astype(np.float32))
print(total)

"""



#Adadelta

train_x_ = []
train_y_ = []
for iter in range(len(train_x)):
    for i in range(len(train_x[iter])):
        train_x_.append(train_x[iter][i])
        train_y_.append(train_y[iter][i])
print(train_x_)
print(train_y_)
history = model.fit(train_x_, train_y_, epochs=1000 ,verbose=2)
#history = model.fit([train_x[1][1]], [train_y[1][1]], epochs=200 ,verbose=2, shuffle=True)
#total = model.predict(methods.text_in_matrix("пока"))
#print(total)
plt.plot(history.history['loss'])

plt.show()
#model.fit(train_x[0], train_y[0], epochs=100 ,verbose=2, shuffle=True)
#for i in range(1):
#    for i in range(len(train_x[0])):
#        model.fit([train_x[0][i]], [train_y[0][i]], batch_size=1 ,epochs=2 ,verbose=2, shuffle=True)




"""
for cycle in range(1):
    for iter in range(len(train_x)):
        for i in range(len(train_x[iter])):
            for iter_ in range(1):
                print([list(filter(lambda num: num != 0, train_x[iter][i]))])
                print([list(filter(lambda num: num != 0, train_y[iter][i]))])
                #history = model.fit([list(filter(lambda num: num != 0, train_x[iter][i]))], [list(filter(lambda num: num != 0, train_y[iter][i]))], batch_size=32 ,epochs=150 ,verbose=2, shuffle=True)
                print(train_x[iter][i])
                #model.fit([list(reversed(train_x[iter][i]))], [list(reversed(train_y[iter][i]))], batch_size=32 ,epochs=50 ,verbose=2, shuffle=True)

for cycle in range(2):
    for i in range(len(train_x[1])-1):
        for iter_ in range(3):
            print([list(filter(lambda num: num != 0, train_x[1][i]))])
            print([list(filter(lambda num: num != 0, train_y[1][i]))])
            #history = model.fit([list(filter(lambda num: num != 0, train_x[iter][i]))], [list(filter(lambda num: num != 0, train_y[iter][i]))], batch_size=32 ,epochs=150 ,verbose=2, shuffle=True)
            model.fit([list(reversed(train_x[1][i]))], [list(reversed(train_y[1][i]))], batch_size=32 ,epochs=100 ,verbose=2, shuffle=True)
"""

#total = model.predict([[0.3,0,0,0,0,0,0,0,0,0]])
#print(total)
#print(methods.matrix_decode_in_text(total))
total = model.predict(methods.text_in_matrix("привет"))
print(total)
#print(methods.matrix_decode_in_text(total))

total = model.predict(methods.text_in_matrix("машина понял ?"))
print(total)

total = model.predict(methods.text_in_matrix("пока"))
print(total)
print(methods.matrix_decode_in_text(total))

#print(methods.matrix_decode_in_text(model.predict(methods.text_in_matrix("привет"))))
#print(methods.matrix_decode_in_text(model.predict(methods.text_in_matrix("как дела ?"))))
#print(methods.matrix_decode_in_text(model.predict(methods.text_in_matrix("какая погода ?"))))
#model.save_weights('for_save/model_save_1.h5')
model.save('for_save/model_save_1.h5')
def matrix_transform(matrix):
     return [[i] for i in matrix]

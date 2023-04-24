from method_text_encode import method_text_encode

methods = method_text_encode()
methods.encode_main()
#print(methods.all_phrases)
#print(methods.all_words)
print(methods.label_encode_words)
train_x = methods.label_all_phrases_x
print(train_x)
train_y = methods.label_all_phrases_y
print(train_y)
lengthwords = methods.LengthWords
embedingcount = methods.EmbedingCount
maxseqtext = methods.MaxSeqText
#print(methods.encode_label)
#print(methods.range_data)
#print(methods.text_in_matrix("привет"))
#print(methods.matrix_decode_in_text([[0.12345, 0.045676, 0, 0, 0, 0, 0, 0, 0, 0]]))

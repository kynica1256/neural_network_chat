import sys
from sklearn import preprocessing

from method_text_encode import  method_text_encode

from method_kernel_nn import main_methods

import base64

def construct_func_predict(method):
    res = method.predict_method(text)
    #func_add_data(text, res, id_user)
    return res

def construct_func_train(method):
    method.train_method()
    return None



def func_add_data(text, result, id_):
    with open("id_res/"+str(id_), "w", encoding="utf-8") as f:
        f.write(text+"\n"+result)
        f.close()



if  __name__ == "__main__":
    use_func_dict = {
        "predict":lambda a: construct_func_predict(a),
        "train":lambda a: construct_func_train(a)
    }
    type_operation = sys.argv[1] #predict or train
    text = sys.argv[2] # base 64


    enc1 = text.encode("UTF-8")
    r1 = base64.b64decode(enc1)
    text = r1.decode("UTF-8")


    id_user = sys.argv[3] #1234
    id_in_main_meth = 0 if type_operation == "predict" else id_user
    method = main_methods(True, id_in_main_meth)
    res = use_func_dict[type_operation](method)
    if res == None:
        sys.exit()

    enc = res.encode("UTF-8")
    r = base64.b64encode(enc)
    res = r.decode("UTF-8")
    print("{"+res+"}")

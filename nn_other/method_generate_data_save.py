import json
import datetime

class generate_data_save:
    def __init__(self):
        with open("id_and_save.json","r",encoding="utf-8") as f:
            data_ = json.loads(f.read())
            f.close()
        self.name = str(len(data["all_data"]))+"_save"
    def data_generate(self):
        now = datetime.datetime.now()
        with open("id_and_save.json","r",encoding="utf-8") as f:
            data_ = json.loads(f.read())
            f.close()
        data_["all_data"].append([now, self.name])
        with open("id_and_save.json","w",encoding="utf-8") as f:
            f.write(json.dumps(data_, indent=4, ensure_ascii=False))
            f.close()

    def data_generate(self):
        directory = "log_nn"
        files = os.listdir(directory)
        num = len(files)
        with open("for_save/log_nn_"+str(num)+".log","r",encoding="utf-8") as f:
            data_ = f.read()
            f.close()
        if len(data_.split("\n")) > 20:
            num+=1
            data_ = ""
        data_text = f"loss - ${self.log_loss} metrics - ${self.metrics}\n"
        data_+=data_text
        with open("for_save/log_nn_"+str(num)+".log","w",encoding="utf-8") as f:
            f.write(data_)
            f.close()

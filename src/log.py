from datetime import datetime
from io import TextIOWrapper

def log(message:str):
    date = datetime.now()
    log_file.write(date.strftime("\n[%X] ")+message)

def log_open():
    date = datetime.now()
    log_name = date.strftime("%d-%m-%y")
    global log_file
    log_file = open("./log/"+log_name+".log", mode="a")
    log("Log opened")
    print(log_name)

def log_close():
    log("Log closed")
    log_file.close()
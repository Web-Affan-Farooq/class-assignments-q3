class Logger:
    def __init__(self):
        print("Instance created ...")

    def __del__(self):
        print("Instance deleted ...")

log1 = Logger() 
del log1
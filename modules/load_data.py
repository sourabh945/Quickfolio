from json import load as ld

data_file = "./data/data.json"

def load() -> dict:
    with open(data_file,"r") as file:
        return ld(file)
import csv
from .tsla import TSLA

def run():
    with open("TSLA.csv") as f:
        reader = csv.reader(f)
        columns = next(reader)
        for row in reader:
            print (row)


        

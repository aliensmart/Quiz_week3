from app import TSLA
from app import insertion_csv
import os


DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'tsla.db')

TSLA.dbpath = DBPATH
insertion_csv.run()

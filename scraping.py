import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import csv
from warnings import warn
import mysql.connector as msql
# pip install mysql-connector-python
from mysql.connector import Error
from time import sleep
from random import randint
import numpy as np
import seaborn as sns

# the data we need: names, year_of_release, imdb_rating, meta_score, genre, etc.
# we will extract data from IMDB database using html tags by find, findall


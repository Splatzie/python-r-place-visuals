"""read txt file inside zip and return the string of index"""
import zipfile
import pandas as pd
def getcsvindex(zippy,ziple, txtfile):
    with zipfile.ZipFile(zippy, mode="r") as zip_file:
        with zipfile.ZipFile(ziple, mode="r") as zip_file:
            with zip_file.open(txtfile) as text_file:
                meow = pd.read_table(text_file, sep=",", header=None, names=["timestamp", "user_id", "colord", "cords"])
                ko = meow[0:]
                return ko
def getcount(ziple, txtfile):
    with zipfile.ZipFile(ziple, mode="r") as zip_file:
        with zip_file.open(txtfile) as text_file:
            meow = pd.read_table(text_file, sep=",", header=None, names=["timestamp", "user_id", "colord", "cords"])
            ko = meow[0:]
            return len(ko)
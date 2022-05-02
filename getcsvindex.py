"""read txt file inside zip and return the string of index"""
import zipfile
import pandas as pd
import io
def getcsvindex(ziple, txtfile, zipfilr):
    with zipfile.ZipFile(ziple, mode="r") as z:
        with z.open(zipfilr) as z2:
            z2filedata = io.BytesIO(z2.read())
            with zipfile.ZipFile(z2filedata, mode="r") as z3:
                with z3.open(txtfile) as txt:
                    meow = pd.read_table(txt, sep=",", header=None, names=["timestamp", "user_id", "colord", "cords"])
                    ko = meow[0:]
                    return ko
def getcount(ziple, txtfile):
    with zipfile.ZipFile(ziple, mode="r") as zip_file:
        with zip_file.open(txtfile) as text_file:
            meow = pd.read_table(text_file, sep=",", header=None, names=["timestamp", "user_id", "colord", "cords"])
            ko = meow[0:]
            return len(ko)
